from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def data_info():
    slack_name = str("Musa Muhammad Khalid")
    track = str('backend')
    
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    res = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Mkothm/hng_internship/blob/main/app.py",
        "github_repo_url": "https://github.com/Mkothm/hng_internship",
        "status_code": 200
    }

    return jsonify(res)
if __name__ == '__main__':
    app.run()