from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ..service.participant_service import ParticipantService

participant_flask_blueprint = Blueprint(
    "participant", __name__, url_prefix="/participant"
)


@participant_flask_blueprint.route("/create/", methods=["POST"])
@jwt_required()
def create_participant():
    participant_service: ParticipantService = ParticipantService()

    print(request.json)

    if request.json is None:
        raise BadRequest("No participant was specified")

    participant_json = request.json.get("participant", False)
    if not participant_json:
        raise BadRequest("No participant was specified")

    participant_service.create_participant(participant_json)
    return jsonify({}), 200


@participant_flask_blueprint.route(
    "/competition/<string:competition_id>/", methods=["GET"]
)
def get_all_by_competition_id(competition_id):
    participant_service: ParticipantService = ParticipantService()

    if not competition_id:
        raise BadRequest("Competition ID is required")

    participants = participant_service.get_participants_by_competition(competition_id)
    if not participants:
        raise NotFound("No participants were found for this competition")

    return jsonify(participants), 200


@participant_flask_blueprint.route(
    "/participant/<string:participant_id>/", methods=["GET"]
)
def get_all_by_participant_id(participant_id):
    participant_service: ParticipantService = ParticipantService()

    if not participant_id:
        raise BadRequest("Participant ID is required")

    participants = participant_service.get_participants_by_participant(participant_id)
    if not participants:
        raise NotFound("No participations were found for this participant_id")

    return jsonify(participants), 200


@participant_flask_blueprint.route("/delete/", methods=["DELETE"])
@jwt_required()
def delete_participant():
    print("*********************************")

    current_user_id: str = get_current_user()
    print(current_user_id)

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

    if current_user_id != participant_id:
        raise Unauthorized("Not allowed to modify the participation of another user.")

    participant_service: ParticipantService = ParticipantService()

    participants = participant_service.get_participants_by_participant(participant_id)
    if not participants:
        raise NotFound("No participations were found for this participant_id")

    participant_service.delete_participant(participant_id, competition_id)
    return jsonify({}), 200
