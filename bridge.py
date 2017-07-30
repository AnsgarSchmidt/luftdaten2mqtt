import os
from   flask import Flask
from   flask import request
import paho.mqtt.client as mqtt

MQTT_SERVER = os.environ['MQTT_SERVER']
MQTT_PORT   = int(os.environ['MQTT_PORT'])

app      = Flask(__name__)
mqclient = mqtt.Client("luftdaten", clean_session=True)
mqclient.connect(MQTT_SERVER, MQTT_PORT, 60)
mqclient.loop_start()


@app.route('/', methods=['GET', 'POST'])
def index():
    content = request.get_json(silent=True)
    id = content['esp8266id']
    mqclient.publish("luftdaten/%s/software_version" % id, content['software_version'])

    for i in content['sensordatavalues']:
        mqclient.publish("luftdaten/%s/%s" % (id, i['value_type']), i['value'])

    return "Done"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8206)
