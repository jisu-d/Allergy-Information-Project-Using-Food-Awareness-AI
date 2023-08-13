import traceback
import os
from flask import Flask
from flask_cors import CORS
from routes.ai_route import AiView
from utils.insert_database_allergy.db import init_db

app = Flask(__name__)

CORS(app)

app.add_url_rule('/foodinfo', view_func=AiView.as_view("check_food"))

if __name__ == "__main__":
    init_db()
    app.run("0.0.0.0")