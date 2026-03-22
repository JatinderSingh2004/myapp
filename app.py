from flask import Flask, jsonify
import redis

app = Flask(__name__)

# "redis" is the service name from docker-compose.yml
r = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    count = r.incr("visits")
    return jsonify({
        "message": "Hello from Docker!",
        "visits": int(count)
    })

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
