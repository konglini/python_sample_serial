import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code = ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed : " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print("received ", str(msg.payload.decode("utf-8")))
    print("topic ", msg.topic)
    print("qos ", msg.qos)
    print("retain flag ", msg.retain)


broker_address = "192.168.0.1"
broker_port = 1883
client_mqtt = mqtt.Client("client1")
client_mqtt.on_connect = on_connect
client_mqtt.on_disconnect = on_disconnect
client_mqtt.on_subscribe = on_subscribe
client_mqtt.on_message = on_message

client_mqtt.connect(broker_address, broker_port)
client_mqtt.subscribe("test/data", 1)

client_mqtt.loop_forever()
