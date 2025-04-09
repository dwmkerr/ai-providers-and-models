export interface ProvidersFile {
  version: string;
  updated: string;
  source: string;
  author: string;
  providers: Record<string, Provider>;
}

export interface Provider {
  id: string;
  name: string;
  docs: string;
  api_specification: ApiSpecification;
  base_url: string;
  additional_endpoints: ApiSpecification[];
  models: Record<string, Model>;
}

export type Endpoint = {
  api_specification: ApiSpecification;
  base_url: string;
};

export type ApiSpecification =
  | "api.openai.com/v1"
  | "generativelanguage.googleapis.com/v1beta";

export interface Model {
  id: string;
  name: string;
  description: string;
  description_short: string;
  status: string;
  knowledgeCutoff?: string;
  context_window: number;
  max_output_tokens: number;
  pricing: {
    input_per_million: number;
    output_per_million: number;
  };
  validated: boolean;
  modalities: {
    text: boolean;
    image: boolean;
    audio: boolean;
    video: boolean;
  };
  endpoints: {
    assistants: boolean;
    batch: boolean;
    chat_completions: boolean;
    completions_legacy: boolean;
    embeddings: boolean;
    fine_tuning: boolean;
    image_generation: boolean;
    moderation: boolean;
    realtime: boolean;
    responses: boolean;
    speech_generation: boolean;
    transcription: boolean;
    translation: boolean;
  };
  documentation_url: string;
  versions: Array<{
    id: string;
    release_date: string;
    isDefault: boolean;
    isDeprecated: boolean;
    description: string;
  }>;
}

export interface Modalities {
  text: boolean;
  image: boolean;
  audio: boolean;
}

export interface Endpoints {
  chat: boolean;
  completions: boolean;
  fine_tuning: boolean;
  embeddings: boolean;
  audio_transcriptions: boolean;
  audio_translations: boolean;
  text_to_speech: boolean;
  images: boolean;
  edits: boolean;
  moderation: boolean;
}

export interface Pricing {
  per_million_input_tokens?: number;
  per_million_output_tokens?: number;
}
