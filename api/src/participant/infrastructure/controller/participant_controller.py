from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ...application.service.participant_service import ParticipantService

participant_flask_blueprint = Blueprint(
    "participants", __name__, url_prefix="/participants"
)


@participant_flask_blueprint.route("", methods=["POST"])
@jwt_required()
def create_participant():
    if request.json is None:
        raise BadRequest("No participant was specified")

    participant_json = request.json.get("participant", False)
    if not participant_json:
        raise BadRequest("No participant was specified")

    participant_service: ParticipantService = ParticipantService()
    participant_service.create_participant(participant_json)
    return jsonify({}), 200


@participant_flask_blueprint.route("", methods=["GET"])
def get_participants():
    competition_id = request.args.get("competition_id")
    participant_id = request.args.get("participant_id")

    participant_service: ParticipantService = ParticipantService()
    participants = participant_service.get_participants(
        competition_id=competition_id, participant_id=participant_id
    )
    if not participants:
        raise NotFound("No participants were found")

    return jsonify(participants), 200


@participant_flask_blueprint.route("", methods=["DELETE"])
@jwt_required()
def delete_participant():
    current_user_id: str = get_current_user()
    if not current_user_id:
        raise Unauthorized("Only logged users can leave competitions")

    if request.json is None:
        raise BadRequest("No participant was specified")

    participant_json = request.json.get("participant", False)
    participant_id = participant_json.get("participant_id")
    competition_id = participant_json.get("competition_id")

    if not participant_id:
        raise BadRequest("Participant ID is required")
    if not competition_id:
        raise BadRequest("Competition ID is required")

    participant_service: ParticipantService = ParticipantService()
    participant_service.delete_participant(participant_id, competition_id)
    return jsonify({}), 200
