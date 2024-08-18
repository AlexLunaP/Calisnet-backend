from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from ...application.user_dto import UserDTO
from ...domain.exception.incorrect_password import IncorrectPassword
from ...domain.exception.user_was_not_found import UserWasNotFound
from ...infrastructure.service.user_service import UserService

userFlaskBlueprint = Blueprint("User", __name__, url_prefix="/user")


@userFlaskBlueprint.route("/create/", methods=["POST"])
def create_user():
    userService: UserService = UserService()

    if request.json is None:
        raise BadRequest("No user was specified")

    userJson = request.json.get("user", False)
    if not userJson:
        raise BadRequest("No user was specified")

    userService.createUser(userJson)
    return jsonify({}), 200


@userFlaskBlueprint.route("/get/<string:userId>/", methods=["GET"])
def get_user(userId):
    userService: UserService = UserService()

    if not userId:
        raise NotFound("User ID is required")

    user = userService.getUser(userId)
    if not user:
        raise NotFound("User was not found")

    return jsonify(user), 200


@userFlaskBlueprint.route("/login/", methods=["POST"])
def login():
    if request.json is None:
        raise BadRequest("Email and password are required")

    email = request.json.get("userEmail", "").strip()
    password = request.json.get("userPassword", "").strip()

    if not email or not password:
        raise BadRequest("Email and password are required")

    try:
        user = UserService().loginUser(email, password)
    except (IncorrectPassword, UserWasNotFound):
        raise Unauthorized("Wrong email or password")

    jwt_token = create_access_token(identity=user)
    return jsonify({"access_token": jwt_token, "user": user}), 200


@userFlaskBlueprint.route("/update/<string:userId>/", methods=["PUT"])
def update_user_profile(userId):
    userService: UserService = UserService()

    if request.json is None:
        raise BadRequest("No data provided for update")

    bio = request.json.get("bio")
    birthdate = request.json.get("birthdate")
    profilePicUrl = request.json.get("profilePicUrl")
    socialLinks = request.json.get("socialLinks")

    if birthdate:
        try:
            birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
        except ValueError:
            raise BadRequest("Invalid birthdate format. Use DD/MM/YYYY.")

    userService.updateUserProfile(
        userId=userId,
        bio=bio,
        birthdate=birthdate,
        profilePicUrl=profilePicUrl,
        socialLinks=socialLinks,
    )
    return jsonify({"message": "Profile updated successfully"}), 200
