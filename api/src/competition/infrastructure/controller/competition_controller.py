from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ...application.service.competition_service import CompetitionService

competition_flask_blueprint = Blueprint(
    "competitions", __name__, url_prefix="/competitions"
)


@competition_flask_blueprint.route("", methods=["POST"])
@jwt_required()
def create_competition():
    if request.json is None:
        raise BadRequest("No competition was specified")

    competition_json = request.json.get("competition", False)
    if not competition_json:
        raise BadRequest("No competition was specified")

    competition_service: CompetitionService = CompetitionService()
    user_id = competition_service.create_competition(competition_json)

    return jsonify(user_id), 200


@competition_flask_blueprint.route("/<string:competition_id>", methods=["GET"])
def get_competition(competition_id):
    if not competition_id:
        raise BadRequest("Competition ID is required")

    competition_service: CompetitionService = CompetitionService()
    competition = competition_service.get_competition(competition_id)
    if not competition:
        raise NotFound("Competition was not found")

    return jsonify(competition), 200


@competition_flask_blueprint.route("", methods=["GET"])
def get_competitions():
    organizer_id = request.args.get("organizer_id")
    competition_status = request.args.get("status")

    competition_service = CompetitionService()
    competitions = competition_service.get_competitions(
        organizer_id=organizer_id, competition_status=competition_status
    )
    if not competitions:
        raise NotFound("No competitions were found")

    return jsonify(competitions), 200


@competition_flask_blueprint.route("/<string:competition_id>/", methods=["PUT"])
@jwt_required()
def update_competition(competition_id):
    current_user_id: str = get_current_user()
    if not current_user_id:
        raise Unauthorized("Only logged users can update a competition")

    if not competition_id:
        raise BadRequest("Competition ID is required")

    if request.json is None:
        raise BadRequest("No data provided for update")

    competition_service: CompetitionService = CompetitionService()
    competition_service.update_competition(request.json)

    return jsonify({"message": "Competition updated successfully"}), 200
