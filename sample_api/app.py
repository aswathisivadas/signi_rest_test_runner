from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return {"message": "Hello from Aswathi's API!"}, 200

if __name__ == '__main__':
    app.run(port=5000)
