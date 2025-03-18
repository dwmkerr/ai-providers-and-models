import fs from "fs";
import path from "path";
import { Provider } from "./types";
import { loadProvidersFile } from "./providers-file";

//  Load and export the providers.
const yaml = fs.readFileSync(
  path.join(__dirname, "../data/models.yaml"),
  "utf8",
);
export const providersFile = loadProvidersFile(yaml);
export const providers: Record<string, Provider> = providersFile.providers;
export const models = Object.values(providers)
  .map((provider) => Object.values(provider.models))
  .flat();
