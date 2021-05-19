from fastapi import FastAPI
from api.routes import router_v1

from database.database import engine
from database import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='FastAPI_test'
)

app.include_router(router_v1, prefix='/api/v1')

