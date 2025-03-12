import fs from 'fs';
import path from 'path';
import YAML from 'yaml';

// Exported TypeScript type definition (simplified, extend as needed)
export interface Model {
  id: string;
  verified: boolean;
  name: string;
  docs: string;
  description: string;
  short_description: string;
  modalities: Record<string, boolean>;
  endpoints: Record<string, boolean>;
  price?: {
    per_million_input_tokens?: number;
    per_million_output_tokens?: number;
  };
  context_window_tokens: number;
  max_output_tokens: number;
}

// Models.yaml as JS object
export const modelsData = YAML.parse(
  fs.readFileSync(path.join(__dirname, '../../models.yaml'), 'utf8')
);

// Array of models exported for convenience
export const models: Model[] = modelsData.providers.flatMap((provider: any) => provider.models);

