from ..models import posts
from PIL import Image
import io

def create_post(image, description):        
    try:
        img = Image.open(image.stream)
        img_format = img.format if img.format else 'PNG'
        img.thumbnail((800, 800))
        memoire_tampon = io.BytesIO()
        img.save(memoire_tampon, format=img_format)
        blob = memoire_tampon.getvalue()

        posts.create_post(image, blob)

    except Exception as e:
        raise Exception
    posts.create_post(image, description)