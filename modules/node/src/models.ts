import fs from "fs";
import path from "path";
import YAML from "yaml";

export interface Pricing {
  per_million_input_tokens?: number;
  per_million_output_tokens?: number;
}

export interface ProvidersFile {
  version: string;
  updated: string;
  source: string;
  author: string;
  providers: Provider[];
}

export interface Provider {
  id: string;
  name: string;
  docs: string;
  api_specification: string;
  models: Model[];
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

export interface Model {
  id: string;
  name: string;
  docs: string;
  description: string;
  short_description: string;
  validated: boolean;
  modalities: Modalities;
  endpoints: Endpoints;
  price?: Pricing;
  context_window_tokens: number;
  max_output_tokens: number;
}

export const providersFile: ProvidersFile = YAML.parse(
  fs.readFileSync(path.join(__dirname, "../models.yaml"), "utf8"),
);

export const providers: Provider[] = providersFile.providers;
