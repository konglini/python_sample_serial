import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("completely connected")
    else:
        print("Bad connection Returned code = ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid = ", mid)


broker_address = "192.168.0.1"
broker_port = 1883
client_mqtt = mqtt.Client("client2")
client_mqtt.on_connect = on_connect
client_mqtt.on_disconnect = on_disconnect
client_mqtt.on_publish = on_publish

client_mqtt.connect(broker_address, broker_port)
client_mqtt.loop_start()
client_mqtt.publish("test/data", "test", 1)
client_mqtt.loop_stop()

client_mqtt.disconnect()
