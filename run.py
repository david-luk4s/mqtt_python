"""App Sub MQTT"""

if __name__ == '__main__':
    print("Listening from of broker **:1883 ")
    import application.main.core as core
    core.running()
