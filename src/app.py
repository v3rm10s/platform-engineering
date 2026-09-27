from flask import Flask, jsonify
import os
import platform
from datetime import datetime
from zoneinfo import ZoneInfo
import socket

app = Flask(__name__)
current_date_time = datetime.now(ZoneInfo("Asia/Singapore"))

@app.route("/")
def hello_world():
    return jsonify ({
        'message': 'Hello World!'
    })

@app.route("/api/v1/health")
def health_check():
    return jsonify ({
        'status':'healthy',
        'time': current_date_time,
        'message': 'This is a new message, i think :D'
    }), 200
    
@app.route("/api/v1//details")
def system_info():
    return jsonify({
        "system":os.name,
        "operating system":platform.system(),
        "os version":platform.version(),
        "architecture":platform.machine(),
        "hostname":socket.gethostname(),
        "address":platform.platform()
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
