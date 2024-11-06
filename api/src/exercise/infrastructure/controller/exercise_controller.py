from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ..service.exercise_service import ExerciseService

exercise_flask_blueprint = Blueprint("exercises", __name__, url_prefix="/exercises")


@exercise_flask_blueprint.route("", methods=["POST"])
@jwt_required()
def create_exercise():
    if request.json is None:
        raise BadRequest("No exercise was specified")

    exercise_json = request.json.get("exercise", False)

    if not exercise_json:
        raise BadRequest("No exercise was specified")

    exercise_service: ExerciseService = ExerciseService()
    exercise_service.create_exercise(exercise_json)
    return jsonify({}), 200


@exercise_flask_blueprint.route("/id/<string:exercise_id>", methods=["GET"])
def get_exercise(exercise_id: str):
    if not exercise_id:
        raise BadRequest("Exercise ID is required")

    exercise_service: ExerciseService = ExerciseService()
    exercise = exercise_service.get_exercise(exercise_id)

    if not exercise:
        raise NotFound("Exercise was not found")

    return jsonify(exercise), 200


@exercise_flask_blueprint.route("", methods=["GET"])
def get_exercises():
    competition_id = request.args.get("competition_id")
    if not competition_id:
        raise BadRequest("Competition ID is required")

    exercise_service: ExerciseService = ExerciseService()
    exercises = exercise_service.get_exercises(competition_id=competition_id)

    if not exercises:
        raise NotFound("No exercises were found")

    return jsonify(exercises), 200


@exercise_flask_blueprint.route("/<string:exercise_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise(exercise_id: str):
    if not exercise_id:
        raise BadRequest("Exercise ID is required")

    current_user_id: str = get_current_user()
    if not current_user_id:
        raise Unauthorized("Only logged users can delete an exercise")

    exercise_service: ExerciseService = ExerciseService()
    exercise_service.delete_exercise(exercise_id=exercise_id)

    return jsonify({}), 200
