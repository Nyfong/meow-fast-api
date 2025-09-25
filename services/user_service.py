from fastapi import Depends
from my_fastapi_project.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    def list_users(self):
        return self.repo.get_all_users()

    def find_user(self, name: str):
        return self.repo.get_user(name)
    
    def get_alice_test(self, name: str):
        return self.repo.get_user(name)
