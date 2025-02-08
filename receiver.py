import PIL.Image as Image
from PIL import ImageTk, Image
import time
import socket
import io
import cv2
import numpy as np

# window.mainloop()

def start_udp_server(host='', port=10113):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    try:
        while True:
            # Receive data and address from client
            data, client_address = server_socket.recvfrom(60000)
            print(len(data))
            print(f"Received image from {client_address}")
            pil_image = Image.open(io.BytesIO(data)).convert('RGB')
            image = np.array(pil_image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # image = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow('image', image)
            cv2.waitKey(1)


            
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally: 
        server_socket.close()

if __name__ == "__main__":
    start_udp_server()
