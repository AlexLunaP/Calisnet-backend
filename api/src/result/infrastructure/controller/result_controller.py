from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from .....src.competition.infrastructure.controller.competition_controller import (
    CompetitionService,
)
from ..service.result_service import ResultService

result_flask_blueprint = Blueprint("result", __name__, url_prefix="/result")


@result_flask_blueprint.route("/create/", methods=["POST"])
@jwt_required()
def create_result():
    result_service: ResultService = ResultService()

    if request.json is None:
        raise BadRequest("No result was specified")

    result_json = request.json.get("result", False)
    if not result_json:
        raise BadRequest("No result was specified")

    print(result_json.get("rank"))

    result_service.create_result(result_json)
    return jsonify({}), 200


@result_flask_blueprint.route("/get/<string:result_id>/", methods=["GET"])
def get_result(result_id: str):
    result_service: ResultService = ResultService()

    if not result_id:
        raise BadRequest("Result ID is required")

    result = result_service.get_result(result_id)

    if not result:
        raise NotFound("Result was not found")

    return jsonify(result), 200


@result_flask_blueprint.route("/competition/<string:competition_id>/", methods=["GET"])
def get_all_by_competition_id(competition_id):
    result_service: ResultService = ResultService()

    print(competition_id)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    if not competition_id:
        raise BadRequest("Competition ID is required")

    results = result_service.get_results_by_competition(competition_id)
    if not results:
        raise NotFound("No results were found for this competition")

    return jsonify(results), 200


@result_flask_blueprint.route("/participant/<string:participant_id>/", methods=["GET"])
def get_all_by_participant_id(participant_id):
    result_service: ResultService = ResultService()

    if not participant_id:
        raise BadRequest("Participant ID is required")

    results = result_service.get_results_by_participant(participant_id)
    if not results:
        raise NotFound("No results were found for this participant_id")

    return jsonify(results), 200


@result_flask_blueprint.route("/update/<string:result_id>/", methods=["PUT"])
@jwt_required()
def update_result(result_id):

    current_user_id: str = get_current_user()

    if not current_user_id:
        raise Unauthorized("Only logged users can update a result")

    if not result_id:
        raise BadRequest("Result ID is required")

    result_service: ResultService = ResultService()
    result = result_service.get_result(result_id)

    if not result:
        raise NotFound("Result was not found")

    competition_id = result["competition_id"]
    competition_service: CompetitionService = CompetitionService()
    competition = competition_service.get_competition(competition_id)

    if not competition:
        raise NotFound("Competition was not found")

    if current_user_id != competition["organizer_id"]:
        raise Unauthorized(
            "Not allowed to modify the competition results of another user."
        )

    if request.json is None:
        raise BadRequest("No data provided for update")

    result_service.update_result(request.json)

    return jsonify({"message": "Result updated successfully"}), 200
