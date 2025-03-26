import { providers } from "./index";

describe("models", () => {
  describe("providers", () => {
    test("exposes expected openai models", () => {
      const openai = providers["openai"];
      expect(openai).not.toBeUndefined();
      expect(openai.name).toBe("OpenAI");
      expect(Object.keys(openai.models).length).toBe(6);
    });

    test("claude", () => {
      const claude = providers["claude"];
      expect(claude).not.toBeUndefined();
      expect(claude.name).toBe("Claude");
      expect(Object.keys(claude.models).length).toBe(0);
    });

    test("exposes gemini provider's models", () => {
      const provider = providers["gemini"];
      expect(provider).not.toBeUndefined();
      expect(provider.name).toBe("Gemini");
      expect(Object.keys(provider.models).length).toBe(3);
    });

    test("exposes additional_endpoints when provided", () => {
      //  Note that openai has no additional endpoints, but gemini does.
      const openai = providers["openai"];
      const gemini = providers["gemini"];
      expect(openai.additional_endpoints).toEqual([]);
      expect(gemini.additional_endpoints).toEqual([
        {
          api_specification: "api.openai.com/v1",
          base_url: "https://generativelanguage.googleapis.com/v1beta/openai/",
        },
      ]);
    });

    test("allows for provider mappings such as 'gemini_openai'", () => {
      //  Expect that 'gemini_openai' is mapped properly
      const geminiOpenAI = providers["gemini_openai"];
      expect(geminiOpenAI).not.toBeUndefined();
      expect(geminiOpenAI.name).toBe("Gemini (OpenAI Compatible)");
      expect(Object.keys(geminiOpenAI.models).length).toBe(3);
    });
  });

  describe("openai-models", () => {
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

    describe("o3-mini-2025-01-31", () => {
      test("is configured", () => {
        const model = providers["openai"].models["o3-mini-2025-01-31"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("o3-mini-2025-01-31");
      });
    });

    describe("o1-2024-12-17", () => {
      test("is configured", () => {
        const model = providers["openai"].models["o1-2024-12-17"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("o1-2024-12-17");
      });
    });

    describe("gpt-4o-mini-2024-07-18", () => {
      test("is configured", () => {
        const model = providers["openai"].models["gpt-4o-mini-2024-07-18"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("gpt-4o-mini-2024-07-18");
      });
    });

    describe("gpt-4-0613", () => {
      test("is configured", () => {
        const model = providers["openai"].models["gpt-4-0613"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("gpt-4-0613");
      });
    });
  });

  describe("gemini-models", () => {
    describe("models/gemini-2.0-flash", () => {
      test("is configured", () => {
        const model = providers["gemini"].models["models/gemini-2.0-flash"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("models/gemini-2.0-flash");
        expect(model.name).toBe("Gemini 2.0 Flash");
        expect(model.description_short).toBe(
          "Our newest multimodal model, with next generation features and improved capabilities",
        );
      });
    });
    describe("models/gemini-2.0-flash-lite", () => {
      test("is configured", () => {
        const model =
          providers["gemini"].models["models/gemini-2.0-flash-lite"];
        expect(model).not.toBeUndefined();
        expect(model.id).toBe("models/gemini-2.0-flash-lite");
        expect(model.name).toBe("Gemini 2.0 Flash-Lite");
        expect(model.description_short).toBe(
          "A Gemini 2.0 Flash model optimized for cost efficiency and low latency",
        );
      });
    });
    describe("models/gemini-1.5-flash", () => {
      test("is configured", () => {
        const model = providers["gemini"].models["models/gemini-1.5-flash"];
        expect(model.id).toBe("models/gemini-1.5-flash");
        expect(model.name).toBe("Gemini 1.5 Flash");
        expect(model.description_short).toBe(
          "Our most balanced multimodal model with great performance for most tasks",
        );
      });
    });
  });
});
