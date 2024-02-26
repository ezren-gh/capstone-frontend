import settings
import requests
import io

from PIL import Image

def glipv2_inference(image, text):
    filename = "uploaded_image.jpg"

    buffer = io.BytesIO()
    image.save(buffer, format=image.format, quality=100)
    image = buffer.getbuffer()

    body = {"text": text}
    files = {"image": (filename, image)}
    res = requests.post(settings.GLIPV2_URL, params=body, files=files)
    img = Image.open(io.BytesIO(res.content))

    return img


def desco_glip_inference(image, text, ground_tokens):
    filename = "uploaded_image.jpg"

    buffer = io.BytesIO()
    image.save(buffer, format=image.format, quality=100)
    image = buffer.getbuffer()

    body = {"text": text, "ground_tokens": ground_tokens}
    files = {"image": (filename, image)}
    res = requests.post(settings.DESCO_GLIP_URL, params=body, files=files)
    img = Image.open(io.BytesIO(res.content))

    return img


def desco_fiber_inference(image, text, ground_tokens):
    filename = "uploaded_image.jpg"

    buffer = io.BytesIO()
    image.save(buffer, format=image.format, quality=100)
    image = buffer.getbuffer()

    body = {"text": text, "ground_tokens": ground_tokens}
    files = {"image": (filename, image)}
    res = requests.post(settings.DESCO_FIBER_URL, params=body, files=files)
    img = Image.open(io.BytesIO(res.content))

    return img
