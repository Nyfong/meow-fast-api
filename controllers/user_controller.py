from fastapi import APIRouter, Depends
from my_fastapi_project.services.user_service import UserService
from my_fastapi_project.services.prompt_string_service import PromptStringService


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(service: UserService = Depends()):
    return {"users": service.list_users()}

@router.get("/{name}")
def get_user(name: str, service: UserService = Depends()):
    user = service.find_user(name)
    if user:
        return {"user": user}
    return {"error": "User not found"}

@router.get("/fongtest/{name}")
def get_alice_test(name: str, service:UserService = Depends()):
    user = service.get_alice_test(name)
    if user:
        return {"user": user}
    return {"error": "User not found"}
