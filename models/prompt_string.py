from pydantic import BaseModel

class PromptString(BaseModel):
    prompt: str