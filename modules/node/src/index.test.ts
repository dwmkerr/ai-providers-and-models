import { providersFile, providers, models } from "./index";

describe("index", () => {
  it("exports expected API", () => {
    expect(providersFile).not.toBeUndefined();
    expect(providers).not.toBeUndefined();
    expect(models).not.toBeUndefined();
  });
});
