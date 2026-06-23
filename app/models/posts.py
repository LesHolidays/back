from ..database import get_db
from datetime import datetime

def create_post(image, description):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO Post (image, description, date_post) VALUES (?, ?, ?)', (image, description, datetime.now()))
    conn.commit()
    conn.close()