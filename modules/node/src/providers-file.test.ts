import { loadProvidersFile } from "./providers-file";

describe("providers-file", () => {
  it("converts undefined 'additional_endpoints' to empty arrays", () => {
    //  Note: no 'additional_endpoints'.
    const yaml = `
version: 0.1.7
providers:
  openai:
    id: openai
`;
    const providersFile = loadProvidersFile(yaml);
    expect(providersFile.providers["openai"].additional_endpoints).toEqual([]);
  });

  it("can handle merge anchors for providers", () => {
    const yaml = `
version: 0.1.7
providers:
  openai: &openai
    id: openai
    name: openai
  openai_merged:
    <<: *openai
    id: openai_merged
`;
    const providersFile = loadProvidersFile(yaml);
    const mergedProvider = providersFile.providers["openai_merged"];
    expect(mergedProvider.id).toEqual("openai_merged"); // merged + overridden
    expect(mergedProvider.name).toEqual("openai");
  });
});
