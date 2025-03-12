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
  name: string;
  docs: string;
  api_specification: string;
  models: Model[];
}

export interface Model {
  id: string;
  verified: boolean;
  name: string;
  docs: string;
  description: string;
  short_description: string;
  modalities: Record<string, boolean>;
  endpoints: Record<string, boolean>;
  price?: Pricing;
  context_window_tokens: number;
  max_output_tokens: number;
}

export const providersFile: ProvidersFile = YAML.parse(
  fs.readFileSync(path.join(__dirname, "../models.yaml"), "utf8"),
);

export const providers: Provider[] = providersFile.providers;
