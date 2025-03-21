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
  docs: string;
  description: string;
  description_short: string;
  validated: boolean;
  modalities: Modalities;
  endpoints: Endpoints;
  price?: Pricing;
  context_window_tokens: number;
  max_output_tokens: number;
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
