from flask import Flask
from config.config import DefaultConfig
from logger import logger

app = Flask(__name__)
app.config.from_object(DefaultConfig)



@app.route("/")
def index():
    return "Welcome Book-Api"

if __name__ == "__main__":
    app.run()