from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()


DB_NAME = os.getenv("POSTGRES_DB", "devops_db")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "db")

@app.get("/")
def read_root():
    return {"message": "Witaj w projekcie DevOps!", "status": "Działa"}

@app.get("/db-test")
def test_db():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        return {"status": "Połączono z bazą danych PostgreSQL!"}
    except Exception as e:
        return {"status": "Błąd połączenia", "error": str(e)}