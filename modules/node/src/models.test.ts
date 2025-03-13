import { providers } from "./index";

describe("models", () => {
  describe("providers", () => {
    test("exposes expected openai models", () => {
      const openai = providers["openai"];
      expect(openai).not.toBeUndefined();
      expect(openai.name).toBe("OpenAI");
      expect(Object.keys(openai.models).length).toBe(4);
    });
  });

  describe("model", () => {
    describe("gpt-4o-2024-08-06", () => {
      test("is configured", () => {
        const model = providers["openai"].models["gpt-4o-2024-08-06"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("gpt-4o-2024-08-06");
        expect(model.name).toBe("GPT-4o");
        expect(model.description_short).toBe(
          "Fast, intelligent, flexible GPT model",
        );
      });
    });

    describe("gpt-4.5-preview", () => {
      test("is configured", () => {
        const model = providers["openai"].models["gpt-4.5-preview"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("gpt-4.5-preview");
      });
    });

    describe("o1-2024-12-17", () => {
      test("is configured", () => {
        const model = providers["openai"].models["o1-2024-12-17"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("o1-2024-12-17");
      });
    });
  });
});
