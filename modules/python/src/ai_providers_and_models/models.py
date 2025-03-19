from datetime import date
from pydantic import BaseModel
from typing import Dict, Optional


class Pricing(BaseModel):
    input_per_million: float
    output_per_million: float


class Endpoints(BaseModel):
    assistants: bool
    batch: bool
    chat_completions: bool
    completions_legacy: bool
    embeddings: bool
    fine_tuning: bool
    image_generation: bool
    moderation: bool
    realtime: bool
    responses: bool
    speech_generation: bool
    transcription: bool
    translation: bool


class Model(BaseModel):
    id: str
    name: str
    documentation_url: str
    description_short: str
    description: str
    status: str
    knowledge_cutoff: Optional[str] = None
    context_window: Optional[int] = None
    max_output_tokens: Optional[int] = None
    validated: bool
    pricing: Pricing
    modalities: Dict[str, bool]
    endpoints: Endpoints


class Provider(BaseModel):
    id: str
    name: str
    docs: str
    api_specification: str
    base_url: str
    models: Dict[str, Model]


class ProvidersFile(BaseModel):
    version: str
    updated: date
    source: str
    author: str
    providers: Dict[str, Provider]
