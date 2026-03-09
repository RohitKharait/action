from flask import Flask, jsonify

app = Flask(__name__)

todos = ["Buy groceries", "Learn DevOps", "Build CI/CD pipeline"]

@app.route('/')
def home():
    return jsonify({"message": "Hello from DevOps become devops Engineer Soon!", "status": "running"})

@app.route('/todos')
def get_todos():
    return jsonify({"todos": todos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)