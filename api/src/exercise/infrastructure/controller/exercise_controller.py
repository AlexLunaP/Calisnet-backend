from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequest, NotFound

from ..service.exercise_service import ExerciseService

exercise_flask_blueprint = Blueprint("exercise", __name__, url_prefix="/exercise")


@exercise_flask_blueprint.route("/create/", methods=["POST"])
@jwt_required()
def create_exercise():
    exercise_service: ExerciseService = ExerciseService()

    if request.json is None:
        raise BadRequest("No exercise was specified")

    exercise_json = request.json.get("exercise", False)
    if not exercise_json:
        raise BadRequest("No exercise was specified")

    exercise_service.create_exercise(exercise_json)
    return jsonify({}), 200


@exercise_flask_blueprint.route("/get/<string:exercise_id>/", methods=["GET"])
def get_exercise(exercise_id: str):
    exercise_service: ExerciseService = ExerciseService()

    if not exercise_id:
        raise BadRequest("Exercise ID is required")

    exercise = exercise_service.get_exercise(exercise_id)

    if not exercise:
        raise NotFound("Exercise was not found")

    return jsonify(exercise), 200


@exercise_flask_blueprint.route(
    "/competition/<string:competition_id>/", methods=["GET"]
)
def get_all_by_competition_id(competition_id):
    exercise_service: ExerciseService = ExerciseService()

    if not competition_id:
        raise BadRequest("Competition ID is required")

    exercises = exercise_service.get_exercises_by_competition(competition_id)
    if not exercises:
        raise NotFound("No exercises were found for this competition")

    return jsonify(exercises), 200
