#include <Wire.h>
#include <Adafruit_ICM20948.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_SSD1306.h>

#define SDA_PIN 6
#define SCL_PIN 7
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_ICM20948 icm;
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(115200);
  delay(1000);
  Wire.begin(SDA_PIN, SCL_PIN);

  // 初始化 ICM20948
  if (!icm.begin_I2C(0x69, &Wire)) {
    Serial.println("Failed to find ICM20948 chip");
    while (1) delay(10);
  }

  icm.setAccelRange(ICM20948_ACCEL_RANGE_8_G);
  icm.setGyroRange(ICM20948_GYRO_RANGE_500_DPS);
  icm.setMagDataRate(AK09916_MAG_DATARATE_100_HZ);

  // 初始化 OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 allocation failed");
    while (1);
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("ICM20948 Ready!");
  display.display();
  delay(1000);
}

void loop() {
  sensors_event_t accel, gyro, mag, temp;
  icm.getEvent(&accel, &gyro, &temp, &mag);

  display.clearDisplay();
  display.setCursor(0, 0);
  display.printf("A X:%.1f Y:%.1f", accel.acceleration.x, accel.acceleration.y);
  display.setCursor(0, 10);
  display.printf("A Z:%.1f", accel.acceleration.z);
  display.setCursor(0, 20);
  display.printf("G X:%.1f Y:%.1f", gyro.gyro.x, gyro.gyro.y);
  display.setCursor(0, 30);
  display.printf("G Z:%.1f", gyro.gyro.z);
  display.setCursor(0, 40);
  display.printf("T:%.1fC", temp.temperature);
  display.display();

  delay(500);
}
