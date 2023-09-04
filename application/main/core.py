import time
from application.config.broker_config import broker_mqtt_configs
from application.main.mqtt_connection.broker_connection import MQTTConnection


def running():
    """Start connection with broker MQTT"""

    mqtt = MQTTConnection(
        broker_mqtt_configs['HOST'],
        broker_mqtt_configs['PORT'],
        broker_mqtt_configs['APP_NAME'],
        broker_mqtt_configs['KEEPALINE'],
    )
    mqtt.start_connection()
    while True:
        time.sleep(0.001)
