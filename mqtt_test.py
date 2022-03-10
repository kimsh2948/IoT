import paho.mqtt.client as mqtt



def on_message(client, userdata, message):

    print("message received " ,str(message.payload.decode("utf-8")))

    print("message topic=",message.topic)

    print("message qos=",message.qos)

    print("message retain flag=",message.retain)

                      

# subscriber

broker_address="192.168.0.56"

client1 = mqtt.Client("ClientSubscriber")

client1.connect(broker_address)

client1.subscribe("vds1/data")

client1.on_message = on_message

client1.loop_forever()

