from ..database import get_db

def get_utilisateurs():
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM Utilisateur")
        utilisateurs = cur.fetchall()
        return utilisateurs
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def get_utilisateur_by_id(utilisateur_id):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Utilisateur WHERE id = ?", (utilisateur_id,))
        utilisateur = cur.fetchone()
        return utilisateur
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()
