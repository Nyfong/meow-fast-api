from fastapi import FastAPI
from my_fastapi_project.controllers import user_controller
from my_fastapi_project.core.docs import setup_scalar

app = FastAPI()

setup_scalar(app)  # mount scalar docs

app.include_router(user_controller.router)
