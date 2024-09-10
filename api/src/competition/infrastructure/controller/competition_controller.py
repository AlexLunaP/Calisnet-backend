from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ..service.competition_service import CompetitionService

competition_flask_blueprint = Blueprint(
    "competition", __name__, url_prefix="/competition"
)


@competition_flask_blueprint.route("/create/", methods=["POST"])
@jwt_required()
def create_competition():
    competition_service: CompetitionService = CompetitionService()

    if request.json is None:
        raise BadRequest("No competition was specified")

    print(request.json)
    competition_json = request.json.get("competition", False)
    if not competition_json:
        raise BadRequest("No competition was specified")

    print("\n")
    print(request.json)

    competition_service.create_competition(competition_json)
    return jsonify({}), 200


@competition_flask_blueprint.route("/get/<string:competition_id>/", methods=["GET"])
def get_competition(competition_id):
    competition_service: CompetitionService = CompetitionService()

    if not competition_id:
        raise BadRequest("Competition ID is required")

    competition = competition_service.get_competition(competition_id)
    if not competition:
        raise NotFound("Competition was not found")

    return jsonify(competition), 200


@competition_flask_blueprint.route("/competitions/", methods=["GET"])
def get_all_competitions():
    competition_service: CompetitionService = CompetitionService()

    competitions = competition_service.get_all_competitions()
    if not competitions:
        raise NotFound("No competitions were found")

    return jsonify(competitions), 200


@competition_flask_blueprint.route("/user/<string:user_id>/", methods=["GET"])
def get_all_by_organizer_id(user_id):
    competition_service: CompetitionService = CompetitionService()

    if not user_id:
        raise BadRequest("Organizer ID is required")

    competitions = competition_service.get_competitions_by_organizer(user_id)
    if not competitions:
        raise NotFound("No competitions were found for this user")

    return jsonify(competitions), 200


@competition_flask_blueprint.route(
    "/status/<string:competition_status>/", methods=["GET"]
)
def get_all_by_status(competition_status):
    competition_service: CompetitionService = CompetitionService()

    if not competition_status:
        raise BadRequest("Competition status is required")

    competitions = competition_service.get_competitions_by_status(competition_status)
    if not competitions:
        raise NotFound("No competitions were found for this status")

    return jsonify(competitions), 200


@competition_flask_blueprint.route("/update/<string:competition_id>/", methods=["PUT"])
@jwt_required()
def update_competition(competition_id):

    current_user_id: str = get_current_user()

    if not current_user_id:
        raise Unauthorized("Only logged users can update a competition")

    if not competition_id:
        raise BadRequest("Competition ID is required")

    competition_service: CompetitionService = CompetitionService()
    competition = competition_service.get_competition(competition_id)

    if not competition:
        raise NotFound("Competition was not found")

    if current_user_id != competition["organizer_id"]:
        raise Unauthorized("Not allowed to modify the competition of another user.")

    if request.json is None:
        raise BadRequest("No data provided for update")

    competition_service.update_competition(request.json)

    return jsonify({"message": "Competition updated successfully"}), 200
