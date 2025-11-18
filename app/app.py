from fastapi import FastAPI

# from .api import register_routes

app = FastAPI(title="My API", version="1.0.0")

app.get("/health")(lambda: {"status": "ok"})
# api/v1
