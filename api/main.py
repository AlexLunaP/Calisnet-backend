import datetime
import os

from flask import Flask
from flask_cors import CORS
from flask_mail import Mail

from .src import competition, exercise, participant, result, user
from .src.competition.infrastructure.competition_providers import CompetitionProviders
from .src.competition.infrastructure.controller.competition_controller import (
    competition_flask_blueprint,
)
from .src.config.config import Config
from .src.exercise.infrastructure.controller.exercise_controller import (
    exercise_flask_blueprint,
)
from .src.exercise.infrastructure.exercise_providers import ExerciseProviders
from .src.participant.infrastructure.controller.participant_controller import (
    participant_flask_blueprint,
)
from .src.participant.infrastructure.participant_providers import ParticipantProviders
from .src.result.infrastructure.controller.result_controller import (
    result_flask_blueprint,
)
from .src.result.infrastructure.result_providers import ResultProviders
from .src.shared.infrastructure.json_web_token_conf import jwt_manager
from .src.user.infrastructure.controller.user_controller import user_flask_blueprint
from .src.user.infrastructure.user_providers import UserProviders

# Dependency injection wiring
user_provider = UserProviders()
user_provider.wire(packages=[user])
competition_provider = CompetitionProviders()
competition_provider.wire(packages=[competition])
exercise_provider = ExerciseProviders()
exercise_provider.wire(packages=[exercise])
participant_provider = ParticipantProviders()
participant_provider.wire(packages=[participant])
result_provider = ResultProviders()
result_provider.wire(packages=[result])

mail = Mail()


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user_flask_blueprint)
    app.register_blueprint(competition_flask_blueprint)
    app.register_blueprint(exercise_flask_blueprint)
    app.register_blueprint(participant_flask_blueprint)
    app.register_blueprint(result_flask_blueprint)

    CORS(app)

    app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=14)
    jwt_manager.init_app(app)

    mail.init_app(app)

    return app


def main():
    app = create_app()
    if os.environ["FLASK_ENV"] == "development":
        app.run(host="localhost", port=8080)


if __name__ == "__main__":
    main()
