import gradio as gr
import requests
import io

from PIL import Image

#authorization
API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def generate_image(prompt):
    image_bytes = query({"inputs": prompt})
    image = Image.open(io.BytesIO(image_bytes))
    return image

demo = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image"
)

demo.launch(share=True)