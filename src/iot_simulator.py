import time
import random
import json
from datetime import datetime

# List of sample shipping containers carrying perishable commodities
CONTAINERS = [
    {"container_id": "CONT-101", "commodity": "Avocados", "target_temp": 5.0, "target_humidity": 85.0},
    {"container_id": "CONT-102", "commodity": "Pharmaceuticals", "target_temp": 2.0, "target_humidity": 60.0},
    {"container_id": "CONT-103", "commodity": "Berries", "target_temp": 1.5, "target_humidity": 90.0}
]

def generate_sensor_data():
    """Generates mock IoT telemetry data for shipping containers."""
    sensor_records = []
    
    for container in CONTAINERS:
        temp_offset = random.uniform(-1.5, 3.5)
        humidity_offset = random.uniform(-5.0, 8.0)
        vibration_level = random.uniform(0.1, 4.5)
        
        current_temp = round(container["target_temp"] + temp_offset, 2)
        current_humidity = round(container["target_humidity"] + humidity_offset, 2)
        
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "container_id": container["container_id"],
            "commodity": container["commodity"],
            "temperature_c": current_temp,
            "humidity_percent": current_humidity,
            "vibration_g": round(vibration_level, 2),
            "status": "AT_RISK" if current_temp > (container["target_temp"] + 2.0) else "NORMAL"
        }
        sensor_records.append(record)
        
    return sensor_records

if __name__ == "__main__":
    print("Starting AtmoSync IoT Sensor Simulator...")
    try:
        for i in range(3):
            data = generate_sensor_data()
            print(f"\n--- Batch {i+1} Telemetry Stream ---")
            print(json.dumps(data, indent=4))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nSimulator stopped.")
