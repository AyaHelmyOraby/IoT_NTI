import paho.mqtt.client as mqtt
import time

BROKER = "broker.hivemq.com"
TOPIC_TEMP = "ESP32/temp1"
TOPIC_MODE = "ESP32/mode1"
TOPIC_THRESHOLD = "ESP32/set_threshold1"

client = mqtt.Client("PC_controller")

def on_connect(client, userdata, flags, rc):
    print("Connected:", rc)
    client.subscribe(TOPIC_TEMP)

def on_message(client, userdata, msg):
    print(f"[ESP32] {msg.topic} → {msg.payload.decode()}")

client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_start()

def set_manual_mode():
    client.publish(TOPIC_MODE, "manual")
    print("Set to MANUAL mode (default threshold on ESP32)")
    
    print("Please wait... Preparing manual control...")
    time.sleep(5)  # Wait 5 seconds before allowing ON/OFF control

    while True:
        cmd = input("Enter 'on' to turn ON or 'off' to turn OFF (or 'exit' to quit): ").strip().lower()
        if cmd in ["on", "off"]:
            client.publish(TOPIC_MODE, cmd)
            print(f"Sent command: {cmd}")
        elif cmd == "exit":
            print("Exiting manual control...")
            break
        else:
            print("Invalid input. Please enter 'on', 'off', or 'exit'.")

def set_auto_mode():
    client.publish(TOPIC_MODE, "auto")
    print("Set to AUTOMATIC mode")

def set_threshold(value):
    client.publish(TOPIC_THRESHOLD, str(value))
    print(f"Custom threshold sent: {value}°C")

while True:
    print("\nChoose Mode:")
    print("1. Manual")
    print("2. Automatic")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        set_manual_mode()
        break
    elif choice == "2":
        set_auto_mode()
        while True:
            try:
                value = float(input("Enter custom threshold (e.g., 42.5): ").strip())
                set_threshold(value)
                break
            except ValueError:
                print("Invalid number. Try again.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
