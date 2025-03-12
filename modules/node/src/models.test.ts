import { providers } from "./index";

describe("models", () => {
  describe("providers", () => {
    test("exposes expected openai models", () => {
      expect(providers[0].name === "openai");
      expect(providers[0].models.length).toBe(2);
    });
  });

  describe("model", () => {
    test("is correctly loaded", () => {
      const model = providers[0].models[0];
      expect(model.id).toBe("gpt-4o-2024-08-06");
      expect(model.name).toBe("GPT-4o");
      expect(model.description_short).toBe(
        "Fast, intelligent, flexible GPT model",
      );
    });
  });
});
