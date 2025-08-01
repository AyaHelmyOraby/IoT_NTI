# ESP32 Microcontroller Project: Sensor Input and Output Control

This project demonstrates a simple embedded system using the **ESP32** microcontroller. The ESP32 reads data from an input sensor and controls two output devices: an LED and a relay.

---

##  Components Used

| Component     | Type          | Description                        |
|---------------|---------------|------------------------------------|
| ESP32         | Microcontroller | Main controller of the system      |
| LED           | Output Device  | Visual indicator (e.g., ON/OFF)    |
| Relay Module  | Output Device  | Controls high-voltage appliances   |
| Sensor (e.g., DHT11, PIR) | Input Device   | Sends data to the ESP32 (e.g., temp, motion) |

---

## ⚙ System Description

- **Sensor** provides input data to the **ESP32**.
- The **ESP32** processes the sensor input.
- Based on the logic, it turns **ON/OFF the LED** or **activates the relay**.
- This can be used for smart home, automation, or environmental monitoring systems.

---

##  Roles of Each Component

- **Sensor** → Input Device (e.g., temperature, motion)
- **LED** → Output Device (status indicator)
- **Relay** → Output Device (to control external appliances)
- **ESP32** → Controller (handles logic and signal control)

---

