import base64
import uuid
from mimetypes import add_type, guess_extension
from pathlib import Path

IMAGE_SERVER_PATH = Path("/home/alexluna/Desktop/TFG/Calisnet/static/images")

add_type("image/svg+xml", ".svg")


def save_media(media: str) -> str:
    if not media.startswith("data:"):
        raise ValueError("Invalid media format")

    # Extract the MIME type and base64 data
    header, base64_data = media.split(",", 1)
    mime_type = header.split(";")[0].split(":")[1]

    # Decode the base64 data
    binary_data = base64.b64decode(base64_data)

    # Determine the file extension
    file_extension = guess_extension(mime_type)
    if not file_extension:
        raise ValueError("Could not determine the file extension")

    # Save the binary data to a file
    file_name = f"{uuid.uuid4()}{file_extension}"
    file_path = IMAGE_SERVER_PATH.joinpath(file_name)
    with open(file_path, "wb") as file:
        file.write(binary_data)

    print("\n")
    print("file_path: ", file_path)
    # Return the file path where the image is stored
    return str(file_path)


def get_base64_image(image_path: str) -> str:
    mime_type = "image/png"  # Default MIME type
    if image_path.endswith(".svg"):
        mime_type = "image/svg+xml"
    elif image_path.endswith(".jpg") or image_path.endswith(".jpeg"):
        mime_type = "image/jpeg"
    elif image_path.endswith(".gif"):
        mime_type = "image/gif"

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded_string}"
