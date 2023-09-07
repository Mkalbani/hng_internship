from flask import Flask, request, jsonify
import datetime, pytz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def data_info():
    slack_name = request.args.get('Musa Muhammad Khalid')
    track = request.args.get('backend')
    
    current_day = datetime.now(pytz.utc).strftime('%A')
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    res = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Mkothm/hng_internship/app.py",
        "github_repo_url": "https://github.com/Mkothm/hng_internship",
        "status_code": 200
    }

    return jsonify(res)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)