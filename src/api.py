from fastapi import FastAPI
from db import get_conn

app = FastAPI(title="ArXiv Paper Curator")

@app.get("/health")
def health_check():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return {
            "status": "ok",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "disconnected",
            "error": str(e)
        }
