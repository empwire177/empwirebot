/*
  EmpwireBot ESP32 Sensor Serial Firmware v2.1

  Board: ESP32 DevKit V1

  Features:
  - Front VL53L1X distance sensor
  - Left VL53L0X distance sensor
  - Right VL53L0X distance sensor
  - Back VL53L0X distance sensor
  - AHT10 temperature/humidity sensor
  - MPU6050 IMU using raw I2C
  - Left/right wheel encoder pulse counting
  - Serial SENSOR line output for Raspberry Pi / ROS 2

  Current EmpwireBot stage:
  v0.5-dev - LiDAR and Camera Upgrade
*/

#include <Wire.h>
#include <Adafruit_VL53L0X.h>
#include <Adafruit_VL53L1X.h>
#include <Adafruit_AHTX0.h>

// -------------------- I2C Pins --------------------
#define I2C_SDA 21
#define I2C_SCL 22

// -------------------- ToF XSHUT Pins --------------------
#define FRONT_XSHUT 12
#define LEFT_XSHUT  13
#define RIGHT_XSHUT 14
#define BACK_XSHUT  15

// -------------------- VL53 I2C Addresses --------------------
#define FRONT_ADDR 0x29   // VL53L1X stays at default address
#define LEFT_ADDR  0x31
#define RIGHT_ADDR 0x32
#define BACK_ADDR  0x33

// -------------------- Encoder Pins --------------------
#define LEFT_ENCODER_PIN  35
#define RIGHT_ENCODER_PIN 36

// -------------------- MPU6050 --------------------
#define MPU6050_ADDR 0x68

// -------------------- Timing --------------------
#define SENSOR_OUTPUT_INTERVAL_MS 1000

// -------------------- Sensor Objects --------------------
Adafruit_VL53L1X frontToF = Adafruit_VL53L1X(FRONT_XSHUT, -1);
Adafruit_VL53L0X leftToF;
Adafruit_VL53L0X rightToF;
Adafruit_VL53L0X backToF;
Adafruit_AHTX0 aht;

// -------------------- Sensor Status Flags --------------------
bool frontOK = false;
bool leftOK = false;
bool rightOK = false;
bool backOK = false;
bool ahtOK = false;
bool mpuOK = false;

// -------------------- Encoder Counters --------------------
volatile long leftEncoderCount = 0;
volatile long rightEncoderCount = 0;

// -------------------- Timing Variable --------------------
unsigned long lastSensorOutput = 0;

// -------------------- Encoder ISR --------------------
void IRAM_ATTR leftEncoderISR() {
  leftEncoderCount++;
}

void IRAM_ATTR rightEncoderISR() {
  rightEncoderCount++;
}

// -------------------- I2C Scanner --------------------
void scanI2C() {
  Serial.println();
  Serial.println("========== I2C SCAN ==========");

  byte count = 0;

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("I2C device found at 0x");

      if (address < 16) {
        Serial.print("0");
      }

      Serial.println(address, HEX);
      count++;
    }
  }

  if (count == 0) {
    Serial.println("No I2C devices found");
  }

  Serial.println("================================");
  Serial.println();
}

// -------------------- MPU6050 Helpers --------------------
bool writeMPURegister(byte reg, byte value) {
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(reg);
  Wire.write(value);
  return Wire.endTransmission() == 0;
}

bool initMPU6050() {
  // Wake up MPU6050
  bool ok1 = writeMPURegister(0x6B, 0x00);

  // Gyro full scale: +/-250 deg/s
  bool ok2 = writeMPURegister(0x1B, 0x00);

  // Accel full scale: +/-2g
  bool ok3 = writeMPURegister(0x1C, 0x00);

  delay(100);

  return ok1 && ok2 && ok3;
}

bool readMPU6050(
  float &accX,
  float &accY,
  float &accZ,
  float &gyroX,
  float &gyroY,
  float &gyroZ,
  float &mpuTempC
) {
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x3B);

  if (Wire.endTransmission(false) != 0) {
    return false;
  }

  Wire.requestFrom(MPU6050_ADDR, 14, true);

  if (Wire.available() < 14) {
    return false;
  }

  int16_t rawAccX = Wire.read() << 8 | Wire.read();
  int16_t rawAccY = Wire.read() << 8 | Wire.read();
  int16_t rawAccZ = Wire.read() << 8 | Wire.read();

  int16_t rawTemp = Wire.read() << 8 | Wire.read();

  int16_t rawGyroX = Wire.read() << 8 | Wire.read();
  int16_t rawGyroY = Wire.read() << 8 | Wire.read();
  int16_t rawGyroZ = Wire.read() << 8 | Wire.read();

  accX = rawAccX / 16384.0;
  accY = rawAccY / 16384.0;
  accZ = rawAccZ / 16384.0;

  gyroX = rawGyroX / 131.0;
  gyroY = rawGyroY / 131.0;
  gyroZ = rawGyroZ / 131.0;

  mpuTempC = rawTemp / 340.0 + 36.53;

  return true;
}

// -------------------- Distance Sensor Helpers --------------------
int readVL53L0X(Adafruit_VL53L0X &sensor, bool sensorOK) {
  if (!sensorOK) {
    return -1;
  }

  VL53L0X_RangingMeasurementData_t measure;
  sensor.rangingTest(&measure, false);

  if (measure.RangeStatus != 4) {
    return measure.RangeMilliMeter;
  }

  return -1;
}

int readFrontVL53L1X() {
  if (!frontOK) {
    return -1;
  }

  if (frontToF.dataReady()) {
    int distance = frontToF.distance();

    if (distance == -1) {
      frontToF.clearInterrupt();
      return -1;
    }

    frontToF.clearInterrupt();
    return distance;
  }

  return -1;
}

// -------------------- ToF Initialisation --------------------
void initDistanceSensors() {
  Serial.println("Initialising distance sensors...");

  pinMode(FRONT_XSHUT, OUTPUT);
  pinMode(LEFT_XSHUT, OUTPUT);
  pinMode(RIGHT_XSHUT, OUTPUT);
  pinMode(BACK_XSHUT, OUTPUT);

  // Turn all ToF sensors off first
  digitalWrite(FRONT_XSHUT, LOW);
  digitalWrite(LEFT_XSHUT, LOW);
  digitalWrite(RIGHT_XSHUT, LOW);
  digitalWrite(BACK_XSHUT, LOW);
  delay(50);

  /*
    Important:
    Keep front VL53L1X OFF first.
    Start VL53L0X sensors one by one and move them away from default 0x29.
    Then start the front VL53L1X last at default 0x29.
  */

  // Left VL53L0X
  digitalWrite(LEFT_XSHUT, HIGH);
  delay(100);
  if (leftToF.begin(LEFT_ADDR, false, &Wire)) {
    leftOK = true;
    Serial.println("Left VL53L0X OK at 0x31");
  } else {
    Serial.println("Left VL53L0X FAILED");
  }

  // Right VL53L0X
  digitalWrite(RIGHT_XSHUT, HIGH);
  delay(100);
  if (rightToF.begin(RIGHT_ADDR, false, &Wire)) {
    rightOK = true;
    Serial.println("Right VL53L0X OK at 0x32");
  } else {
    Serial.println("Right VL53L0X FAILED");
  }

  // Back VL53L0X
  digitalWrite(BACK_XSHUT, HIGH);
  delay(100);
  if (backToF.begin(BACK_ADDR, false, &Wire)) {
    backOK = true;
    Serial.println("Back VL53L0X OK at 0x33");
  } else {
    Serial.println("Back VL53L0X FAILED");
  }

  // Front VL53L1X last
  digitalWrite(FRONT_XSHUT, HIGH);
  delay(100);
  if (frontToF.begin(FRONT_ADDR, &Wire)) {
    frontOK = true;
    Serial.println("Front VL53L1X OK at 0x29");

    if (frontToF.startRanging()) {
      Serial.println("Front VL53L1X ranging started");
    } else {
      Serial.println("Front VL53L1X ranging failed to start");
      frontOK = false;
    }
  } else {
    Serial.println("Front VL53L1X FAILED");
  }

  Serial.println("Distance sensor initialisation complete");
  Serial.println();
}

// -------------------- Setup --------------------
void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println();
  Serial.println("==============================================");
  Serial.println(" EmpwireBot ESP32 Sensor Serial Firmware v2.1 ");
  Serial.println("==============================================");

  Wire.begin(I2C_SDA, I2C_SCL);
  Wire.setClock(400000);

  scanI2C();

  initDistanceSensors();

  Serial.println("Initialising AHT10...");
  if (aht.begin()) {
    ahtOK = true;
    Serial.println("AHT10 OK");
  } else {
    Serial.println("AHT10 FAILED");
  }

  Serial.println("Initialising MPU6050...");
  if (initMPU6050()) {
    mpuOK = true;
    Serial.println("MPU6050 OK");
  } else {
    Serial.println("MPU6050 FAILED");
  }

  pinMode(LEFT_ENCODER_PIN, INPUT);
  pinMode(RIGHT_ENCODER_PIN, INPUT);

  attachInterrupt(digitalPinToInterrupt(LEFT_ENCODER_PIN), leftEncoderISR, RISING);
  attachInterrupt(digitalPinToInterrupt(RIGHT_ENCODER_PIN), rightEncoderISR, RISING);

  Serial.println("Encoders OK");
  Serial.println();
  Serial.println("EmpwireBot sensor firmware started");
  Serial.println();
}

// -------------------- Loop --------------------
void loop() {
  unsigned long now = millis();

  if (now - lastSensorOutput >= SENSOR_OUTPUT_INTERVAL_MS) {
    lastSensorOutput = now;

    int frontMM = readFrontVL53L1X();
    int leftMM = readVL53L0X(leftToF, leftOK);
    int rightMM = readVL53L0X(rightToF, rightOK);
    int backMM = readVL53L0X(backToF, backOK);

    float tempC = -999.0;
    float humidity = -999.0;

    if (ahtOK) {
      sensors_event_t humidityEvent;
      sensors_event_t tempEvent;

      aht.getEvent(&humidityEvent, &tempEvent);

      tempC = tempEvent.temperature;
      humidity = humidityEvent.relative_humidity;
    }

    float accX = 0.0;
    float accY = 0.0;
    float accZ = 0.0;
    float gyroX = 0.0;
    float gyroY = 0.0;
    float gyroZ = 0.0;
    float mpuTempC = 0.0;

    bool mpuReadOK = false;

    if (mpuOK) {
      mpuReadOK = readMPU6050(accX, accY, accZ, gyroX, gyroY, gyroZ, mpuTempC);
    }

    long leftCount;
    long rightCount;

    noInterrupts();
    leftCount = leftEncoderCount;
    rightCount = rightEncoderCount;
    interrupts();

    Serial.print("SENSOR,");
    Serial.print("F_MM=");
    Serial.print(frontMM);
    Serial.print(",");
    Serial.print("L_MM=");
    Serial.print(leftMM);
    Serial.print(",");
    Serial.print("R_MM=");
    Serial.print(rightMM);
    Serial.print(",");
    Serial.print("B_MM=");
    Serial.print(backMM);
    Serial.print(",");
    Serial.print("TEMP_C=");
    Serial.print(tempC, 2);
    Serial.print(",");
    Serial.print("HUM_PCT=");
    Serial.print(humidity, 2);
    Serial.print(",");
    Serial.print("MPU_OK=");
    Serial.print(mpuReadOK ? 1 : 0);
    Serial.print(",");
    Serial.print("AX_G=");
    Serial.print(accX, 3);
    Serial.print(",");
    Serial.print("AY_G=");
    Serial.print(accY, 3);
    Serial.print(",");
    Serial.print("AZ_G=");
    Serial.print(accZ, 3);
    Serial.print(",");
    Serial.print("GX_DPS=");
    Serial.print(gyroX, 3);
    Serial.print(",");
    Serial.print("GY_DPS=");
    Serial.print(gyroY, 3);
    Serial.print(",");
    Serial.print("GZ_DPS=");
    Serial.print(gyroZ, 3);
    Serial.print(",");
    Serial.print("MPU_TEMP_C=");
    Serial.print(mpuTempC, 2);
    Serial.print(",");
    Serial.print("ENC_L=");
    Serial.print(leftCount);
    Serial.print(",");
    Serial.print("ENC_R=");
    Serial.print(rightCount);
    Serial.print(",");
    Serial.print("UPTIME_MS=");
    Serial.println(now);
  }
}
