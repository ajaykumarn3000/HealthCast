from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.diabetics import router as diabetics_router
from backend.routes.login import router as login_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return "Connected to the server!"


app.include_router(router=login_router)
app.include_router(router=diabetics_router)
