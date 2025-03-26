import YAML from "yaml";
import { Provider, ProvidersFile } from "./types";

export function loadProvidersFile(yaml: string): ProvidersFile {
  //  Before we return the deserialized object we'll mutate it to clean up some
  //  fields, this is OK as it is within the function (i.e. not mutating
  //  external state).
  const providersFile: ProvidersFile = YAML.parse(yaml) as ProvidersFile;
  Object.keys(providersFile.providers).forEach((id) => {
    const provider = providersFile.providers[id];
    //  If the 'additional_endpoints' array is missing, set it to an empty
    //  array.
    provider.additional_endpoints = provider.additional_endpoints || [];

    //  If the provider uses a merge key, set that up now.
    // eslint-disable-next-line  @typescript-eslint/no-explicit-any
    const mergeKey = (provider as Record<string, any>)["<<"] as Provider;
    if (mergeKey) {
      const merged = {
        ...mergeKey,
        ...provider,
      };
      // eslint-disable-next-line  @typescript-eslint/no-explicit-any
      delete (merged as Record<string, any>)["<<"];
      providersFile.providers[id] = merged;
    }
  });

  return providersFile;
}
