import base64
from ..models import posts_model
from PIL import Image
import io
import json
import urllib.request
from dotenv import load_dotenv
import os

def create_post(user_id, image, description):
    img = Image.open(image.stream)
    img_format = img.format if img.format else 'PNG'
    img.thumbnail((800, 800))
    memoire_tampon = io.BytesIO()
    img.save(memoire_tampon, format=img_format)
    blob = memoire_tampon.getvalue()
    posts_model.create_post(user_id, blob, description)
    send_notif()

def get_posts():
    rows = posts_model.get_all_posts()
    posts = []
    for row in rows:
        post = dict(row)
        
        blob_data = post["image"]
        
        if isinstance(blob_data, str):
            if blob_data.startswith("b'") or blob_data.startswith('b"'):
                import ast
                blob_data = ast.literal_eval(blob_data)
            else:
                blob_data = blob_data.encode('utf-8')
        
        base64_data = base64.b64encode(blob_data).decode('utf-8')
        
        mime_type = "image/png" if b"PNG" in blob_data[:10] else "image/jpeg"
        
        post["image"] = f"data:{mime_type};base64,{base64_data}"
            
        posts.append(post)
        
    return posts

def send_notif():
    try:
        load_dotenv()
        url = os.getenv("WEBHOOK_URL")
        data = json.dumps({"content": "Nouvelle photo sur [Holidays](https://holidays.super-sympa.fr) !"}).encode()
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "HolidaysBot/1.0"
        }
        urllib.request.urlopen(urllib.request.Request(url, data, headers))
    except:
        pass