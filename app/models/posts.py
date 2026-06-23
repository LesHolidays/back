from ..database import get_db
from datetime import datetime
from sqlite3 import Binary

def create_post(blob, description):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO Post (image, description, date_post) VALUES (?, ?, ?)', (Binary(blob), description, datetime.now()))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()