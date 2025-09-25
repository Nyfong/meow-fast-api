from fastapi import APIRouter, Depends
from my_fastapi_project.models.prompt_string import PromptString
from my_fastapi_project.services.prompt_string_service import PromptStringService


prompt_router = APIRouter(prefix="/prompt", tags=["Prompt data"])


#work with crud

@prompt_router.get("/promptdata")
def get_prompt():
    return [{
  "id": "chatGP-Kdet-ach-001",
  "author": "Pu Kdet",
  "timestamp": "2025-09-25T20:45:00Z",
  "type": "prompt",
  "content": "Write me a short story about a bamboo forest and a hidden village.",
  "metadata": {
    "tags": ["creative-writing", "story", "fantasy"],
    "language": "en",
    "source": "user",
    "confidence_estimate": 0.0,
    
  },
  "system": {
    "system_id": "fakeai-core-3",
    "name": "FakeAI Core",
    "version": "3.2.1",
    "model_family": "transformer-xl-sim",
    "model_size": "7B",
    "purpose": "synthetic content generation and testing",
    "training_data": {
      "sources": ["synthetic_corpora_v2", "public_domain_books", "web_crawl_2023_snapshot"],
      "approx_tokens": 12000000000,
      "curation_notes": "Filtered for profanity, PII, and extremist content; includes synthetic augmentations."
    },
    "generation_pipeline": {
      "preprocessing": "tokenize->normalize_unicode->dedupe",
      "fine_tuning": "supervised_fine_tune_on_prompts_v1",
      "postprocessing": "detoxify->format_normalize"
    },
    "safety": {
      "content_moderation": "automated + manual sampling",
      "policy_version": "2025-07-01",
      "rejection_reasons": ["PII", "Hate", "Illicit instructions"]
    },
    "provenance": {
      "created_by": "FakeAI Labs",
      "created_at": "2025-09-25T20:45:00Z",
      "dataset_version": "dataset_v3.0"
    },
    "license": "CC-BY-4.0 (synthetic dataset derivative)",
    "intended_use": ["research", "testing", "demo"],
    "privacy": {  "pii_mitigation": "redaction" }
  }
}
]

@prompt_router.post("/promptdata")
def post_prompt(promptSignleData: PromptString, service: PromptStringService = Depends()):          
    return {"promptdata": service.create_prompt(promptSignleData)}

