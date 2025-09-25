from fastapi import Depends
from my_fastapi_project.core.db import get_cyber_model

class PromptStringRepository:
    def __init__(self, db=Depends(get_cyber_model)):
        self.db = db

    def get_all_prompt_strings(self):
        return self.db
    
    def create_prompt(self,prompt: str ):
        self.db.append(prompt)
        return prompt