from fastapi import FastAPI
from app.api.routes import auth, roles

app = FastAPI(title="Meraki API")

app.include_router(auth.router)
app.include_router(roles.router)