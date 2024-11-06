from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_current_user, jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ...domain.exceptions.incorrect_password import IncorrectPassword
from ...domain.exceptions.user_was_not_found import UserWasNotFound
from ...infrastructure.service.user_service import UserService

user_flask_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_flask_blueprint.route("", methods=["POST"])
def create_user():
    user_service: UserService = UserService()

    if request.json is None:
        raise BadRequest("No user was specified")

    user_json = request.json.get("user", False)
    if not user_json:
        raise BadRequest("No user was specified")

    user_service.create_user(user_json)
    return jsonify({}), 200


@user_flask_blueprint.route("/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user_service: UserService = UserService()

    if not user_id:
        raise NotFound("User ID is required")

    user = user_service.get_user(user_id)
    if not user:
        raise NotFound("User was not found")

    return jsonify(user), 200


@user_flask_blueprint.route("/username/<string:username>", methods=["GET"])
def get_user_by_username(username):
    user_service: UserService = UserService()

    if not username:
        raise NotFound("Username is required")

    user = user_service.get_user_by_username(username)
    if not user:
        raise NotFound("User was not found")

    return jsonify(user), 200


@user_flask_blueprint.route("/<string:user_id>/", methods=["PUT"])
@jwt_required()
def update_user_profile(user_id):
    current_user_id: str = get_current_user()

    if not current_user_id:
        raise Unauthorized("Only logged users can update their profile")
    if current_user_id != user_id:
        raise Unauthorized("Not allowed to modify the profile of another user.")

    user_service: UserService = UserService()

    if request.json is None:
        raise BadRequest("No data provided for update")

    full_name = request.json.get("full_name")
    bio = request.json.get("bio")
    social_links = request.json.get("social_links")
    profile_image_url = request.json.get("profile_image_url")

    user_service.update_user_profile(
        user_id=user_id,
        full_name=full_name,
        bio=bio,
        social_links=social_links,
        profile_image_url=profile_image_url,
    )
    return jsonify({"message": "Profile updated successfully"}), 200


@user_flask_blueprint.route("/login", methods=["POST"])
def login():
    if request.json is None:
        raise BadRequest("Email and password are required")

    email = request.json.get("userEmail", "").strip()
    password = request.json.get("userPassword", "").strip()

    if not email or not password:
        raise BadRequest("Email and password are required")

    try:
        user = UserService().login_user(email, password)
    except (IncorrectPassword, UserWasNotFound):
        raise Unauthorized("Wrong email or password")

    jwt_token = create_access_token(identity=user)
    return jsonify({"access_token": jwt_token, "user": user}), 200
