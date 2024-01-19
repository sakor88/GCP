import os
import json
import flask
from flask_cors import CORS
from google.cloud import storage, vision

app = flask.Flask(__name__)
cors = CORS(app)

# Imports the Cloud Logging client library
import google.cloud.logging
import logging

# Instantiates a client
client = google.cloud.logging.Client()

client.setup_logging()


@app.route("/", methods=["POST"])
def analyze_image(request):

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': ['POST','OPTIONS'],
    }

    image_name = request.form.get('fileName')
    image_content = request.form.get('image')


    if not image_name:
        return 'Error: Please provide an image name in the query parameter.', 400, headers


    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    if response.error.message:
        return ("Vision API error", 400, headers)
    
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )

    faces_json = []

    for face in faces:
        anger_value = f"anger: {likelihood_name[face.anger_likelihood]}"
        joy_value = f"joy: {likelihood_name[face.joy_likelihood]}"
        surprise_value = f"surprise: {likelihood_name[face.surprise_likelihood]}"

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
        ]

        face_bounds = "face bounds: {}".format(",".join(vertices))

        face_data = {
            "anger": anger_value,
            "joy": joy_value,
            "surprise": surprise_value,
            "face_bounds": face_bounds
        }

        faces_json.append(face_data)

    logging.info(faces_json)

    return faces_json, 200, headers
