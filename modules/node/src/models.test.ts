import { providers } from "./index";

describe("models", () => {
  describe("providers", () => {
    test("exposes expected openai models", () => {
      expect(providers[0].name === "openai");
      expect(providers[0].models.length).toBe(2);
    });
  });
});
