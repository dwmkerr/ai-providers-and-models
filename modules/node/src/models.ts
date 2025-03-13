import fs from "fs";
import path from "path";
import YAML from "yaml";
import { Provider, ProvidersFile } from "./types";

export const providersFile: ProvidersFile = YAML.parse(
  fs.readFileSync(path.join(__dirname, "../models.yaml"), "utf8"),
);

export const providers: Record<string, Provider> = providersFile.providers;
