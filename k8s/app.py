from flask import Flask, jsonify
import datetime

app = Flask(__name__)

traffic_data = []

@app.route('/api/traffic_data')
def get_traffic_data():
    now = datetime.datetime.now()
    vehicle_count = len(traffic_data)
    data = {'time': now.isoformat(), 'vehicle_count': vehicle_count}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
