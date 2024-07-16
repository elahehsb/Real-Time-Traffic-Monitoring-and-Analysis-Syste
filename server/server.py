from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/traffic_data', methods=['POST'])
def traffic_data():
    file = request.files['frame']
    np_img = np.fromstring(file.read(), np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    
    # Further processing and analytics
    # Example: Counting vehicles, speed estimation, etc.
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
