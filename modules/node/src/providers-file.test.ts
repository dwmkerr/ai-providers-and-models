import { loadProvidersFile } from "./providers-file";

describe("providers-file", () => {
  test("converts undefined 'additional_endpoints' to empty arrays", () => {
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
});
