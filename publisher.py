import json

if __name__ == "__main__":
    from paho.mqtt import client as mqtt
    mqtt_client = mqtt.Client()
    mqtt_client.connect(host="localhost", port=1883)
    mqtt_client.publish("/messages", json.dumps({"message": "hello world"}))
