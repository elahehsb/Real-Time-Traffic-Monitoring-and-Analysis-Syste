import cv2
import numpy as np
import requests
import time

def process_frame(frame):
    # Example vehicle detection logic
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')
    detected_vehicles = vehicles.detectMultiScale(gray, 1.1, 1)
    return detected_vehicles

def main():
    cap = cv2.VideoCapture(0)
    server_url = 'http://your_server_url/traffic_data'

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_vehicles = process_frame(frame)
        for (x, y, w, h) in detected_vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        response = requests.post(server_url, files={'frame': buffer.tobytes()})

        cv2.imshow('Traffic Monitor', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
