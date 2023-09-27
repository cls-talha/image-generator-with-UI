import requests
import json
import base64
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import matplotlib.pyplot as plt

with open('api_credentials.json') as f:
    api_credentials = json.load(f)

def get_image(prompt: str):

    url = "https://api.getimg.ai/v1/stable-diffusion-xl/text-to-image"

    payload = {
        "model": "stable-diffusion-xl-v1-0",
        "prompt": str(prompt),
        "negative_prompt": "Disfigured, cartoon, blurry",
        "width": 1024,
        "height": 1024, 
        "steps": 30,
        "guidance": 7.5,
        "seed": 0,
        "scheduler": "euler",
        "output_format": "jpeg"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_credentials['api_key']}"
    }

    response = requests.post(url, json=payload, headers=headers)
    image = response.text
    data = json.loads(image)
    image_data = data["image"]
    image_bytes = base64.b64decode(image_data)
    image_stream = BytesIO(image_bytes)
    image = Image.open(image_stream)

    # # Convert PIL image to numpy array
    # image_np = np.array(image)

    # # Save the image using OpenCV
    # cv2.imwrite("purple_cat.jpg", cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

    return image
# get_image("realistic purple cat with long paws and curly tail")
