import paho.mqtt.client as mqtt
from .callbacks import on_connect, on_subscribe, on_message

class MQTTConnection:
    """Implement of MQTT"""

    def __init__(self, host: str, port: int, app_name: str, keepaline: int) -> None:
        self.__host = host
        self.__port = port
        self.__app_name = app_name
        self.__keepaline = keepaline
        self.__mqtt_client = None

    def start_connection(self):
        """Method for start connection """
        self.__mqtt_client = mqtt.Client(self.__app_name)

        # callbacks
        self.__mqtt_client.on_connect = on_connect
        self.__mqtt_client.on_subscribe = on_subscribe
        self.__mqtt_client.on_message = on_message

        self.__mqtt_client.connect(
            self.__host,
            self.__port,
            self.__keepaline
        )
        self.__mqtt_client.loop_start()

    def end_connection(self):
        """Close connection"""
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            return True
        except Exception:
            return False
