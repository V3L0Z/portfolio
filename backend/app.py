from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
import json

app = Flask(__name__)
REQUEST_COUNT = Counter('request_count', 'Total Number of Requests')

@app.route('/api/posts')
def posts():
    REQUEST_COUNT.inc()
    with open("blog_posts.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
