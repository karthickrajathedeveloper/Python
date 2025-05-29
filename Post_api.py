from flask import Flask, request
import csv
from datetime import datetime
import os

app = Flask(__name__)
csv_path = 'file_path/rfid_log.csv'

@app.route('/rfid', methods=['POST'])
def receive_rfid():
    data = request.json
    uid = data.get('uid')

    if uid:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            # If file not exist, create and add header
            file_exists = os.path.isfile(csv_path)

            with open(csv_path, 'a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Date Time', 'UID'])
                writer.writerow([now, uid])

            return {'status': 'success', 'message': 'Data saved'}

        except PermissionError:
            return {'status': 'failed', 'message': 'Permission Denied! Close file if opened elsewhere.'}

    else:
        return {'status': 'failed', 'message': 'UID missing'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
