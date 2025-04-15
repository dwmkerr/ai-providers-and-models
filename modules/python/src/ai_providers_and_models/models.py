from datetime import date
from pydantic import BaseModel
from typing import Dict, Optional, List


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


class ModalityOptions(BaseModel):
    text: bool
    image: bool
    audio: bool
    video: bool


class Modalities(BaseModel):
    input: ModalityOptions
    output: ModalityOptions


class Version(BaseModel):
    id: str
    release_date: str
    isDefault: bool
    isDeprecated: bool
    description: Optional[str] = None


class Model(BaseModel):
    id: str
    name: str
    documentation_url: str
    description_short: str
    description: str
    status: str
    knowledgeCutoff: Optional[str] = None
    context_window: Optional[int] = None
    max_output_tokens: Optional[int] = None
    validated: bool
    pricing: Pricing
    modalities: Modalities
    endpoints: Endpoints
    versions: Optional[List[Version]] = None


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
