from iot_utils import SensorDevice, SmartSensor, write_to_csv, process_sensor_data

def main():

    sensor1 = SensorDevice("sensor1", "Lab 1")
    sensor1.generate_readings(10)
    sensor1.save_to_file("sensor1_data.csv")

    sensor2 = SmartSensor("sensor2", "Lab 2")
    sensor3 = SmartSensor("sensor3", "Lab 3")
    sensor2.generate_readings(10)
    sensor3.generate_readings(10)

    all_readings = sensor1.readings + sensor2.readings + sensor3.readings

    write_to_csv(all_readings, "all_sensor_data.csv")

    anomalies_sensor2 = sensor2.detect_anomaly()
    anomalies_sensor3 = sensor3.detect_anomaly()
    print("Anomalies in sensor2:", anomalies_sensor2)
    print("Anomalies in sensor3:", anomalies_sensor3)

    process_sensor_data("all_sensor_data.csv")

if __name__ == "__main__":
    main()
