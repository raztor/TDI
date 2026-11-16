# Inventario de dependencias y versiones

Fecha de inventario: **16 de noviembre de 2026**. Complementa las tablas de [FUENTES.md](../../FUENTES.md). Los grupos distinguen ejecución de la estación, elaboración de documentos y compilación del firmware.

Las versiones de primer nivel se fijan en [station/requirements.txt](../../station/requirements.txt), [firmware/requirements-build.txt](../../firmware/requirements-build.txt), [tools/planos/requirements.txt](../../tools/planos/requirements.txt) y [prepare.py](../../firmware/meshtastic/prepare.py). Las demás versiones son las resueltas en los entornos utilizados: este inventario no modifica los manifiestos ni convierte todas las dependencias transitivas en versiones fijadas.

Las bibliotecas de sensores, GPS, pantallas, BLE o MQTT presentes en un grafo de dependencias no acreditan que esos periféricos o funciones estén activos. La estación del proyecto recibe por USB y el frontend utiliza JavaScript/SVG; las bibliotecas de visualización del entorno CAD no se sirven al navegador.

## Dependencias resueltas del firmware RAK4631

Base: [Meshtastic v2.7.26.54e0d8d](https://github.com/meshtastic/firmware/tree/v2.7.26.54e0d8d), commit `54e0d8d0ab2ff56b3a9ce967e53f79e49af560fb`. Entorno `cerroseguro-rak4631`. Inventario contrastado con el grafo de la compilación del firmware usado en banco y los manifiestos de sus bibliotecas. Fuentes base: [platformio.ini](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/platformio.ini), [nrf52.ini](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/variants/nrf52840/nrf52.ini) y [RAK4631](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/variants/nrf52840/rak4631/platformio.ini).

ArduinoThread se identifica por commit: su versión local generada por el gestor no representa una versión publicada. TinyUSB se identifica por el manifiesto del framework fijado. BSEC conserva la [licencia de Bosch](https://github.com/boschsensortec/Bosch-BSEC2-Library/blob/master/LICENSE.md), incluidos sus binarios; no se sustituye por la licencia del código de integración.

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| ESP8266 and ESP32 OLED driver for SSD1306 displays | 4.4.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/esp8266-oled-ssd1306/archive/2e26010040e028baee72e2093402fa7b3c59e430.zip |
| OneButton | 2.6.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/OneButton/archive/fa352d668c53f290cfa480a5f79ad422cd828c70.zip |
| arduino-fsm | 2.2.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/arduino-fsm/archive/7db3702bf0cfe97b783d6c72595e3f38e0b19159.zip |
| TinyGPSPlus | 1.0.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/TinyGPSPlus/archive/71a82db35f3b973440044c476d4bcdc673b104f4.zip |
| ArduinoThread | commit b841b0415721f1341ea41cccfb4adccfaf951567 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/ArduinoThread/archive/b841b0415721f1341ea41cccfb4adccfaf951567.zip |
| Nanopb | 0.4.9+1 | Codificación protobuf embebida del protocolo Meshtastic. | https://github.com/nanopb/nanopb/archive/refs/tags/nanopb-0.4.9.1.zip |
| ErriezCRC32 | 1.0.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/Erriez/ErriezCRC32/archive/refs/tags/1.0.1.zip |
| NonBlockingRTTTL | 1.4.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/end2endzone/NonBlockingRTTTL/archive/refs/tags/1.4.0.zip |
| RadioLib | 7.6.0 | Control del transceptor SX1262 y transporte radio del firmware base. | https://github.com/jgromes/RadioLib/archive/refs/tags/7.6.0.zip |
| Crypto | 0.4.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/rweather/arduinolibs.git |
| Adafruit BusIO | 1.17.4 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_BusIO/archive/refs/tags/1.17.4.zip |
| Adafruit Unified Sensor | 1.1.15 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_Sensor/archive/refs/tags/1.1.15.zip |
| Adafruit GFX Library | 1.12.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit-GFX-Library/archive/refs/tags/1.12.6.zip |
| Adafruit NeoPixel | 1.15.5 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_NeoPixel/archive/1.15.5.zip |
| Adafruit SSD1306 | 2.5.17 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_SSD1306/archive/2.5.17.zip |
| Adafruit BMP280 Library | 3.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_BMP280_Library/archive/refs/tags/3.0.0.zip |
| Adafruit BMP085 Library | 1.2.4 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit-BMP085-Library/archive/refs/tags/1.2.4.zip |
| Adafruit BME280 Library | 2.3.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_BME280_Library/archive/refs/tags/2.3.0.zip |
| Adafruit DPS310 | 1.1.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_DPS310/archive/refs/tags/1.1.6.zip |
| Adafruit SH110X | 2.1.14 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_SH110x/archive/refs/tags/2.1.14.zip |
| Adafruit MCP9808 Library | 2.0.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_MCP9808_Library/archive/refs/tags/2.0.2.zip |
| Adafruit INA260 Library | 1.5.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_INA260/archive/refs/tags/1.5.3.zip |
| Adafruit INA219 | 1.2.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_INA219/archive/refs/tags/1.2.3.zip |
| Adafruit MPU6050 | 2.2.9 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_MPU6050/archive/refs/tags/2.2.9.zip |
| Adafruit LIS3DH | 1.3.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_LIS3DH/archive/refs/tags/1.3.0.zip |
| Adafruit AHTX0 | 2.0.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_AHTX0/archive/refs/tags/2.0.6.zip |
| Adafruit LSM6DS | 4.7.4 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_LSM6DS/archive/refs/tags/4.7.4.zip |
| Adafruit TSL2591 Library | 1.4.5 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_TSL2591_Library/archive/refs/tags/1.4.5.zip |
| EmotiBit MLX90632 | 1.0.8 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/EmotiBit/EmotiBit_MLX90632/archive/refs/tags/v1.0.8.zip |
| Adafruit MLX90614 Library | 2.1.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit-MLX90614-Library/archive/refs/tags/2.1.6.zip |
| INA3221 | 1.0.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/sgtwilko/INA3221/archive/bb03d7e9bfcc74fc798838a54f4f99738f29fc6a.zip |
| QMC5883LCompass | 1.2.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/mprograms/QMC5883LCompass/archive/refs/tags/v1.2.3.zip |
| DFRobot_RTU | 1.0.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/DFRobot/DFRobot_RTU/archive/refs/tags/V1.0.6.zip |
| DFRobot_RainfallSensor | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/DFRobot/DFRobot_RainfallSensor/archive/38fea5e02b40a5430be6dab39a99a6f6347d667e.zip |
| INA226 | 0.6.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/RobTillaart/INA226/archive/refs/tags/0.6.6.zip |
| SparkFun MAX3010x Pulse and Proximity Sensor Library | 1.1.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/sparkfun/SparkFun_MAX3010x_Sensor_Library/archive/refs/tags/v1.1.2.zip |
| SparkFun 9DoF IMU Breakout - ICM 20948 - Arduino Library | 1.3.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/sparkfun/SparkFun_ICM-20948_ArduinoLibrary/archive/refs/tags/v1.3.2.zip |
| ICM42670P | 1.0.8 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/tdk-invn-oss/motion.arduino.ICM42670P/archive/refs/tags/1.0.8.zip |
| Adafruit LTR390 Library | 1.1.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_LTR390/archive/refs/tags/1.1.2.zip |
| Adafruit PCT2075 | 1.0.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_PCT2075/archive/refs/tags/1.0.6.zip |
| DFRobot_BMM150 | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/DFRobot/DFRobot_BMM150/archive/refs/tags/V1.0.0.zip |
| SparkFun MMC5983MA Magnetometer Arduino Library | 1.1.5 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/sparkfun/SparkFun_MMC5983MA_Magnetometer_Arduino_Library/archive/v1.1.5.zip |
| Adafruit TSL2561 | 1.1.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_TSL2561/archive/refs/tags/1.1.3.zip |
| BH1750_WE | 1.1.10 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/wollewald/BH1750_WE/archive/refs/tags/1.1.10.zip |
| Adafruit SHTC3 Library | 1.0.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_SHTC3/archive/refs/tags/1.0.2.zip |
| Adafruit BMP3XX Library | 2.1.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_BMP3XX/archive/refs/tags/2.1.6.zip |
| Adafruit MAX1704X | 1.0.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_MAX1704X/archive/refs/tags/1.0.3.zip |
| Adafruit LPS2X | 2.0.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_LPS2X/archive/refs/tags/2.0.6.zip |
| Adafruit SHT31 Library | 2.2.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_SHT31/archive/refs/tags/2.2.2.zip |
| Adafruit VEML7700 Library | 2.1.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_VEML7700/archive/refs/tags/2.1.6.zip |
| Adafruit SHT4x Library | 1.0.5 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_SHT4X/archive/refs/tags/1.0.5.zip |
| SparkFun Qwiic Scale NAU7802 Arduino Library | 1.0.6 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/sparkfun/SparkFun_Qwiic_Scale_NAU7802_Arduino_Library/archive/refs/tags/v1.0.6.zip |
| ClosedCube OPT3001 | 1.1.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/closedcube/ClosedCube_OPT3001_Arduino |
| DFRobot_LarkWeatherStation | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/meshtastic/DFRobot_LarkWeatherStation/archive/4de3a9cadef0f6a5220a8a906cf9775b02b0040d.zip |
| Sensirion Core | 0.7.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/Sensirion/arduino-core/archive/refs/tags/0.7.3.zip |
| Sensirion I2C SCD4x | 1.1.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/Sensirion/arduino-i2c-scd4x/archive/refs/tags/1.1.0.zip |
| Sensirion I2C SFA3x | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/Sensirion/arduino-i2c-sfa3x/archive/refs/tags/1.0.0.zip |
| Sensirion I2C SCD30 | 1.1.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/Sensirion/arduino-i2c-scd30/archive/1.1.1.zip |
| bsec2 | 1.10.2610 | Control/procesamiento del BME680 mediante el sensor upstream; no es una calibración del prototipo. | https://github.com/boschsensortec/Bosch-BSEC2-Library/archive/refs/tags/1.10.2610.zip |
| BME68x Sensor library | 1.3.40408 | Control/procesamiento del BME680 mediante el sensor upstream; no es una calibración del prototipo. | https://github.com/boschsensortec/Bosch-BME68x-Library/archive/refs/tags/v1.3.40408.zip |
| Adafruit nRFCrypto | 0.0.5 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_nRFCrypto |
| TBPubSubClient | 2.12.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/thingsboard/pubsubclient/archive/refs/tags/v2.12.1.zip |
| NTPClient | 3.2.1 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/arduino-libraries/NTPClient/archive/refs/tags/3.2.1.zip |
| Melopero RV3028 | 1.2.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/melopero/Melopero_RV-3028_Arduino_Library |
| RAK13800-W5100S | 1.0.2 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/RAKWireless/RAK13800-W5100S/archive/1.0.2.zip |
| RAKwireless NCP5623 RGB LED library | 1.0.3 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/RAKWireless/RAK14001-NCP5623-Library |
| RAK12035_SoilMoisture | 1.0.4 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/rakwireless/RAK12035_SoilMoisture.git |
| RAKwireless RAK12034 | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/RAKWireless/RAK12034-BMX160/archive/dcead07ffa267d3c906e9ca4a1330ab989e957e2.zip |
| SPI | 1.0 | Bus de radio/sensor o USB del framework nRF52. | http://www.arduino.cc/en/Reference/SPI |
| SoftwareSerial | 1.0.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | http://arduino.cc/en/Reference/SoftwareSerial |
| Wire | 1.0 | Bus de radio/sensor o USB del framework nRF52. | http://www.arduino.cc/en/Reference/Wire |
| Rotary Encoder | 0.8.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_nRF52_Arduino |
| Adafruit Bluefruit nRF52 Libraries | 0.21.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_nRF52_Arduino |
| Adafruit TinyUSB Library | 3.1.3 | Bus de radio/sensor o USB del framework nRF52. | https://github.com/adafruit/Adafruit_TinyUSB_Arduino |
| Adafruit Internal File System on Bluefruit nRF52 | 0.11.0 | Componente de la base Meshtastic; ejecución condicionada por hardware y configuración. | https://github.com/adafruit/Adafruit_nRF52_Arduino |

## Paquetes del framework y toolchain

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| framework-arduinoadafruitnrf52 | 1.10601.0 | Paquete del toolchain/framework usado en compilación. | https://github.com/meshtastic/Adafruit_nRF52_Arduino/tree/9ddcbc9568b12f102f9e88bd4d1b88ea789213a4 |
| framework-cmsis | 2.50700.210515 | Paquete del toolchain/framework usado en compilación. | http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php |
| tool-adafruit-nrfutil | 1.503.0 | Paquete del toolchain/framework usado en compilación. | https://registry.platformio.org/tools/platformio/tool-adafruit-nrfutil |
| tool-scons | 4.40801.0 | Paquete del toolchain/framework usado en compilación. | http://www.scons.org |
| tool-sreccat | 1.164.0 | Paquete del toolchain/framework usado en compilación. | http://srecord.sourceforge.net |
| toolchain-gccarmnoneeabi | 1.90301.200702 | Paquete del toolchain/framework usado en compilación. | https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm |

## Entorno de estación USB en macOS

Python 3.11.9. Versiones instaladas observadas el 16-11-2026.

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| bleak | 3.1.0 | Dependencia BLE de Meshtastic; la estación del proyecto usa USB. | https://github.com/hbldh/bleak |
| certifi | 2026.10.23 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/certifi/python-certifi |
| charset-normalizer | 3.5.2 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/jawah/charset_normalizer |
| idna | 3.20 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/kjd/idna |
| meshtastic | 2.7.11 | API serie, mensajes y telemetría de la estación. | https://pypi.org/project/meshtastic/ |
| packaging | 26.3 | Interpretación de versiones en dependencias. | https://github.com/pypa/packaging |
| protobuf | 7.36.2 | Decodificación de paquetes y configuración Meshtastic. | https://developers.google.com/protocol-buffers/ |
| pyobjc-core | 13.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-Cocoa | 13.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-CoreBluetooth | 13.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-libdispatch | 13.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/ronaldoussoren/pyobjc |
| Pypubsub | 4.0.7 | Eventos de recepción y pérdida de conexión; no es MQTT. | https://github.com/schollii/pypubsub |
| pyserial | 3.5 | USB serie y enumeración de puertos del iniciador. | https://github.com/pyserial/pyserial |
| PyYAML | 6.0.3 | Perfiles YAML de radio y pruebas de configuración. | https://github.com/yaml/pyyaml |
| requests | 2.34.2 | Cliente HTTP disponible en Meshtastic; no es el servidor del dashboard. | https://github.com/psf/requests |
| tabulate | 0.9.0 | Presentación tabular de la CLI de Meshtastic. | https://github.com/astanin/python-tabulate |
| typing_extensions | 4.16.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/python/typing_extensions |
| urllib3 | 2.8.0 | Dependencia transitiva instalada de Meshtastic; no es una biblioteca del frontend. | https://github.com/urllib3/urllib3 |

## Entorno de generación de planos

Python 3.12.14. Versiones instaladas observadas el 16-11-2026.

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| aiohappyeyeballs | 2.7.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/aiohappyeyeballs |
| aiohttp | 3.14.5 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/aiohttp |
| aiosignal | 1.4.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/aiosignal |
| attrs | 26.1.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/python-attrs/attrs |
| cadquery | 2.8.0 | Lectura y proyección de los STEP del Gill. | https://github.com/CadQuery/cadquery |
| cadquery-ocp | 7.9.3.1.1 | Bindings OCP/Open CASCADE usados por el generador de planos. | https://pypi.org/project/cadquery-ocp/ |
| cadquery-ocp-proxy | 7.9.3.1.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/cadquery-ocp-proxy/ |
| casadi | 3.8.2 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/casadi/casadi |
| charset-normalizer | 3.5.2 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/jawah/charset_normalizer |
| contourpy | 1.4.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/contourpy/contourpy |
| cycler | 0.12.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/matplotlib/cycler |
| ezdxf | 1.4.5 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/mozman/ezdxf |
| fonttools | 4.68.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/fonttools/ |
| frozenlist | 1.8.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/frozenlist |
| idna | 3.20 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/kjd/idna |
| kiwisolver | 1.5.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/nucleic/kiwi |
| llvmlite | 0.50.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/numba/llvmlite |
| matplotlib | 3.11.2 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/matplotlib/matplotlib |
| more-itertools | 11.2.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/more-itertools/more-itertools |
| msgpack | 1.2.4 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/msgpack/msgpack-python/ |
| multidict | 7.2.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/multidict |
| multimethod | 1.12 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/coady/multimethod |
| nlopt | 2.11.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/DanielBok/nlopt-python |
| numba | 0.68.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://numba.pydata.org |
| numpy | 2.5.5 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/numpy/numpy |
| packaging | 26.3 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/pypa/packaging |
| pillow | 13.0.0 | Procesamiento de imágenes en herramientas de elaboración/verificación. | https://github.com/python-pillow/Pillow |
| propcache | 0.5.4 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/propcache |
| pyparsing | 3.3.3 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/pyparsing/pyparsing.git |
| python-dateutil | 4.0.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/dateutil/dateutil |
| PyYAML | 6.0.3 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/yaml/pyyaml |
| reportlab | 5.1.0 | Composición de hojas técnicas y exportación PDF. | https://www.reportlab.com/ |
| runtype | 0.5.3 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/erezsh/runtype |
| scipy | 1.18.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/scipy/scipy |
| trame | 4.0.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame/ |
| trame-client | 4.1.4 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-client/ |
| trame-common | 1.2.9 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-common/ |
| trame-components | 2.5.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-components/ |
| trame-server | 4.1.2 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-server/ |
| trame-vtk | 2.11.17 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-vtk/ |
| trame-vuetify | 3.3.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/trame-vuetify/ |
| typing_extensions | 4.16.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/python/typing_extensions |
| tzdata | 2026.6 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/python/tzdata |
| vtk | 9.6.2 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://vtk.org |
| wslink | 2.6.0 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://pypi.org/project/wslink/ |
| yarl | 1.25.1 | Dependencia instalada del entorno CadQuery/ReportLab; no se ejecuta en el dashboard. | https://github.com/aio-libs/yarl |

## Entorno Python de compilación y configuración

Python 3.11.9. Versiones instaladas observadas el 16-11-2026. Este entorno también contiene el cliente Meshtastic utilizado para configurar los equipos; no todas sus bibliotecas son requisitos del compilador.

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| ajsonrpc | 1.2.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/pavlov99/ajsonrpc |
| anyio | 4.16.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/agronholm/anyio |
| bleak | 3.1.0 | Dependencia BLE de Meshtastic; la estación del proyecto usa USB. | https://github.com/hbldh/bleak |
| bottle | 0.13.4 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/bottlepy/bottle |
| certifi | 2026.10.23 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/certifi/python-certifi |
| chardet | 5.2.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://chardet.readthedocs.io/ |
| charset-normalizer | 3.5.2 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/jawah/charset_normalizer |
| click | 8.1.7 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/pallets/click/ |
| colorama | 0.4.6 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/tartley/colorama |
| grpcio | 1.85.1 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/grpc/grpc |
| grpcio-tools | 1.85.1 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/grpc/grpc/tree/master/tools/distrib/python/grpcio_tools |
| h11 | 0.16.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/python-hyper/h11 |
| idna | 3.20 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/kjd/idna |
| marshmallow | 3.26.2 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/marshmallow-code/marshmallow |
| meshtastic | 2.7.11 | API serie, mensajes y telemetría de la estación. | https://pypi.org/project/meshtastic/ |
| packaging | 26.3 | Interpretación de versiones en dependencias. | https://github.com/pypa/packaging |
| platformio | 6.1.18 | Compilación y gestión del entorno nRF52840. | https://platformio.org |
| protobuf | 7.36.2 | Decodificación de paquetes y configuración Meshtastic. | https://developers.google.com/protocol-buffers/ |
| pyelftools | 0.33 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/eliben/pyelftools.git |
| pyobjc-core | 13.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-Cocoa | 13.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-CoreBluetooth | 13.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/ronaldoussoren/pyobjc |
| pyobjc-framework-libdispatch | 13.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/ronaldoussoren/pyobjc |
| Pypubsub | 4.0.7 | Eventos de recepción y pérdida de conexión; no es MQTT. | https://github.com/schollii/pypubsub |
| pyserial | 3.5 | USB serie y enumeración de puertos del iniciador. | https://github.com/pyserial/pyserial |
| PyYAML | 6.0.3 | Perfiles YAML de radio y pruebas de configuración. | https://github.com/yaml/pyyaml |
| requests | 2.34.2 | Cliente HTTP disponible en Meshtastic; no es el servidor del dashboard. | https://github.com/psf/requests |
| semantic-version | 2.10.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/rbarrois/python-semanticversion |
| starlette | 0.46.2 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/encode/starlette |
| tabulate | 0.9.0 | Presentación tabular de la CLI de Meshtastic. | https://github.com/astanin/python-tabulate |
| typing_extensions | 4.16.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/python/typing_extensions |
| urllib3 | 2.8.0 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/urllib3/urllib3 |
| uvicorn | 0.34.3 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/encode/uvicorn |
| wsproto | 1.3.2 | Herramienta o dependencia del entorno de compilación/configuración; no se utiliza para servir el dashboard. | https://github.com/python-hyper/wsproto/ |

## Gestión de los entornos

pip, setuptools y wheel son herramientas de instalación y empaquetado del entorno, no bibliotecas importadas por la aplicación. Sus fuentes son [pip](https://github.com/pypa/pip), [setuptools](https://github.com/pypa/setuptools) y [wheel](https://github.com/pypa/wheel). Python aporta su biblioteca estándar; no se distribuye una copia independiente de cada módulo. Las licencias originales de cada dependencia siguen siendo aplicables.
