from ..models import posts
from werkzeug.utils import secure_filename
from PIL import Image
import io

def create_post(image, description):
    filename = secure_filename(image.filename)
        
    try:
        img = Image.open(image.stream)
        img_format = img.format if img.format else 'PNG'
        img.thumbnail((800, 800))
        memoire_tampon = io.BytesIO()
        img.save(memoire_tampon, format=img_format)
        blob_concrêt = memoire_tampon.getvalue()

        conn = sqlite3.connect('ma_base.db') # Mets le bon chemin vers ton fichier .db
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (filename, image_data) VALUES (?, ?)",
            (filename, blob_concrêt)
        )
        conn.commit()
        conn.close()

    except Exception as e:
        raise Exception
    posts.create_post(image, description)