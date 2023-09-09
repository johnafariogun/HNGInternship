from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

class Response:
    def __init__(self, slack_name, current_day, utc_time, track, github_file_url, github_repo_url, status_code):
        self.slack_name = slack_name
        self.current_day = current_day
        self.utc_time = utc_time
        self.track = track
        self.github_file_url = github_file_url
        self.github_repo_url = github_repo_url
        self.status_code = status_code

@app.route('/api', methods=['GET'])
def handle():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    now = datetime.datetime.utcnow()
    day = now.strftime('%A')
    github_file = "https://github.com/joey1123455/nzuri_server_week1/blob/main/api/index.go"
    github_repo = "https://github.com/joey1123455/nzuri_server_week1"
    status_code = 200
    res = Response(
        slack_name,
        day,
        now.strftime('%Y-%m-%dT%H:%M:%SZ'),
        track,
        github_file,
        github_repo,
        status_code
    )
    return jsonify(res.__dict__)

if __name__ == '__main__':
    app.run()
