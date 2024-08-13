import datetime
import os

from flask import Flask, jsonify
from flask_cors import CORS
from src import user
from src.shared.infrastructure.json_web_token_conf import jwtManager
from src.user.infrastructure.controller.user_controller import userFlaskBlueprint
from src.user.infrastructure.user_providers import UserProviders

# Dependency injection wiring
userProvider = UserProviders()
userProvider.wire(packages=[user])


def create_app():

    app = Flask(__name__)
    app.register_blueprint(userFlaskBlueprint)

    CORS(app)

    app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=14)
    jwtManager.__init__(app)

    return app


def main():
    app = create_app()
    if os.environ["FLASK_ENV"] == "development":
        app.run(host="localhost", port=8080)


if __name__ == "__main__":
    main()
