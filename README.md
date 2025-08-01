# ESP32 Microcontroller Project: Sensor Input and Output Control

This project demonstrates a simple embedded system using the **ESP32** microcontroller. The ESP32 reads data from an input sensor and controls two output devices: an LED and a relay.

---

## 🔧 Components Used

| Component     | Type          | Description                        |
|---------------|---------------|------------------------------------|
| ESP32         | Microcontroller | Main controller of the system      |
| LED           | Output Device  | Visual indicator (e.g., ON/OFF)    |
| Relay Module  | Output Device  | Controls high-voltage appliances   |
| Sensor (e.g., DHT11, PIR) | Input Device   | Sends data to the ESP32 (e.g., temp, motion) |

---

## ⚙️ System Description

- **Sensor** provides input data to the **ESP32**.
- The **ESP32** processes the sensor input.
- Based on the logic, it turns **ON/OFF the LED** or **activates the relay**.
- This can be used for smart home, automation, or environmental monitoring systems.

---

## 🔁 Roles of Each Component

- **Sensor** → Input Device (e.g., temperature, motion)
- **LED** → Output Device (status indicator)
- **Relay** → Output Device (to control external appliances)
- **ESP32** → Controller (handles logic and signal control)

---

## 🛠 Example Use Case

> A motion sensor detects movement → ESP32 turns ON the LED  
> If temperature exceeds threshold → ESP32 activates the relay (e.g., fan or AC)

---

## 🚀 Getting Started

1. Connect the components to the ESP32 according to your schematic.
2. Flash the ESP32 with code written in Arduino IDE or PlatformIO.
3. Upload the code and open Serial Monitor to observe sensor data and control logic.

---

## 📝 Notes

- Ensure the relay module is properly powered and can handle the voltage/current of the external device.
- Use appropriate resistors for LED.
- Handle GPIO pin limitations and configurations on the ESP32.

---

## 📚 Learn More

- [ESP32 Official Docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [Relay with ESP32 Tutorial](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/)
- [Sensor Interfacing Examples](https://randomnerdtutorials.com/projects-esp32/)
