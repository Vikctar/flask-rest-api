from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from the other side'


app.run(port=5000, debug=True)
