from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from EC2 - Version 2!"

@app.route('/version')
def version():
    return jsonify({
        "app": "EC2 Flask App",
        "version": "2.0",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
