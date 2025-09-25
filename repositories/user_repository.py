from fastapi import Depends
from my_fastapi_project.core.db import get_db

class UserRepository:
    def __init__(self, db=Depends(get_db)):
        self.db = db

    def get_all_users(self):
        return self.db["users"]

    def get_user(self, name: str):
        return name if name in self.db["users"] else None
