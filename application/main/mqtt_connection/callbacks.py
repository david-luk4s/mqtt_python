from application.config.broker_config import broker_mqtt_configs

def on_connect(client, userdata, flags, rc):
    """Callback connected"""
    if rc == 0:
        print(f"Connected with sucess: {client}")
        client.subscribe(broker_mqtt_configs['TOPIC'])
    else:
        print("Fail connected")

def on_subscribe(client, userdata, mid, granted_qos):
    """Call subscribe"""
    print(f"Client: {client} - subscribe in: {broker_mqtt_configs['TOPIC']}")
    print(f"QOS: {granted_qos}")

def on_message(client, userdata, message):
    """Load messages"""
    print(f"{message.payload}")
