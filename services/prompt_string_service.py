from my_fastapi_project.repositories.prompt_string_repository import PromptStringRepository
from fastapi import Depends
class PromptStringService:
    def __init__(self, parameters_string: str, repository: PromptStringRepository = Depends()):
        self.parameters_string = parameters_string
        self.repository = repository

    def get_all_prompt_strings(self):
        return self.repository.get_all_prompt_strings()
    
    def create_prompt(self, prompt:str):
        return self.repository.create_prompt(prompt)
    