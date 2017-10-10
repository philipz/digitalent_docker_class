# Example of using the MQTT client class to subscribe to and publish feed values.
# Author: Tony DiCola

# Import standard python modules.
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
from subprocess import check_output


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = 'YOUR_KEY'
ADAFRUIT_IO_USERNAME = 'YOUR_NAME'  # See https://accounts.adafruit.com
                                                    # to find your username.


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for CPU_Temp changes...')
    # Subscribe to changes on a feed named CPU_Temp.
    client.subscribe('CPU_Temp')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

def get_temp():
    temp = check_output(["cat","/sys/class/thermal/thermal_zone0/temp"])
    return(str(float(temp)/1000))

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# Now send new values every 10 seconds.
print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
while True:
    value = get_temp()
    print('Publishing {0} to CPU_Temp.'.format(value))
    client.publish('CPU_Temp', value)
    time.sleep(10)

