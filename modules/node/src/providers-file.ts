import YAML from "yaml";
import { ProvidersFile } from "./types";

export function loadProvidersFile(yaml: string): ProvidersFile {
  //  Before we return the deserialized object we'll mutate it to clean up some
  //  fields, this is OK as it is within the function (i.e. not mutating
  //  external state).
  const providersFile: ProvidersFile = YAML.parse(yaml) as ProvidersFile;
  Object.keys(providersFile.providers).map((id) => {
    const provider = providersFile.providers[id];
    //  If the 'additional_endpoints' array is missing, set it to an empty
    //  array.
    provider.additional_endpoints = provider.additional_endpoints || [];
    return provider;
  });

  return providersFile;
}
