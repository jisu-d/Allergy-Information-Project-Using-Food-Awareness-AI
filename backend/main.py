from fastapi import FastAPI
from router.api.v1 import img_processing

app = FastAPI()

app.include_router(img_processing.router)