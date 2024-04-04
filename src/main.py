from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from database.fu_db import get_db
from routers import contact
from routers import auth

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(contact.router)

# @app.get("/")
# def index():
#     return {"message": "Contact Application"}


# @app.get("/api/healthchecker")
# async def healthchecker(db: AsyncSession = Depends(get_db)):
#     try:
#         result = await db.execute(text("SELECT 1"))
#         result = result.fetchone()
#         if result is None:
#             raise HTTPException(status_code=500, detail="Database is not configured correctly")
#         return {"message": "Welcome to FastAPI!"}
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500, detail="Error connecting to the database")