import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Good morning, " + name + "!\n"
    return message

if __name__ == "__main__":
    port = int(os.environ.get("PORT"))
    app.run(host='0.0.0.0', port=5000)
