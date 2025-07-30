from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

#PostgreSQL Connection Config 
DB_CONFIG = {
    'dbname': 'FastAPI_db',
    'user': 'aditya1',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

# Pydantic Schemas 
class User(BaseModel):
    name: str
    email: EmailStr

class UserOut(User):
    id: int

# DB Initialization
def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()

# API Routes

# GET all users
@app.get("/users", response_model=List[UserOut])
def get_users():
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# GET single user by ID
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST new user
@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: User):
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING *",
        (user.name, user.email)
    )
    new_user = cursor.fetchone()
    conn.commit()
    conn.close()
    return new_user

# PUT update user
@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: User):
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING *",
        (user.name, user.email, user_id)
    )
    updated_user = cursor.fetchone()
    conn.commit()
    conn.close()
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)