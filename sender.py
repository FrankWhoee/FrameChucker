from picamera2 import Picamera2
import io
import time
import socket

picam2 = Picamera2()

# print(picam2.sensor_modes)

mode = picam2.sensor_modes[0]
config = picam2.create_preview_configuration(sensor={'bit_depth':5, 'output_size': (768,432)})
# config['main']['format']
# config["raw"]['size'] = (2304,1296)
# print(config)
# print(mode['size'])
picam2.options["quality"] = 50
picam2.configure(config)
picam2.start()

# picam2.start()
time.sleep(1)



i = 0

# soc = socket.create_connection(("192.168.10.68", 10113))
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        data = io.BytesIO()
        print(f"Sending frame {i}")
        picam2.capture_file(data, format='jpeg')
        # with open('output.jpeg', 'rb') as f:
        #     data.write(f.read())
        # data.seek(0)
        print("Captured image")
        tosend = data.getvalue()
        print(len(tosend))

        # sender_socket
        # server_socket.sendto(tosend, ("192.252.230.149", 10113))
        soc.sendto(tosend, ("192.168.10.68", 10113))
        data.close()
        i += 1
        time.sleep(0.033)
        
except KeyboardInterrupt:
    print("\nShutting down server...")
finally:
    soc.close()