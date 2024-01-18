import os
import json
import flask
from flask_cors import CORS
from google.cloud import storage, vision

app = flask.Flask(__name__)
cors = CORS(app)

@app.route("/")
def analyze_image():
    ## Set CORS headers for the preflight request 
    if flask.request.method == 'OPTIONS':

        ## Allows GET requests from any origin with the Content-Type
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': ['POST','OPTIONS'],
            'Access-Control-Allow-Headers': 'Content-Type',
        }

        return ('', 204, headers)

    ## Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return ("Hello World!", 200, headers)


    # Get the image URL from the query parameter
    data= flask.request.get_json()
    image_name = data['image_name']

    print(image_name)

    # Validate if image name is provided
    if not image_name:
        return 'Error: Please provide an image name in the query parameter.', 400, headers

    # Download the image from Cloud Storage
    image_content = download_image_from_storage(image_name)

    # Analyze the image using Google Cloud Vision API
    detected_objects = detect_objects(image_content)

    # Log the detected objects
    print("Detected Objects:", detected_objects)

    # Return the detected objects in the response
    return json.dumps(detected_objects), 200, headers

def download_image_from_storage(image_name):
    # Replace 'your-bucket-name' with your actual Google Cloud Storage bucket name
    bucket_name = 'image-storage-gcp-final-project-410222'

    # Initialize the Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket and blob
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(image_name)

    # Download the image content
    image_content = blob.download_as_text()

    return image_content

def detect_objects(image_content):
    # Initialize the Cloud Vision API client
    client = vision.ImageAnnotatorClient()

    # Create an image instance from the image content
    image = vision.Image(content=image_content)

    # Perform object detection
    response = client.object_localization(image=image)

    # Extract detected objects
    detected_objects = [obj.name for obj in response.localized_object_annotations]

    return detected_objects
