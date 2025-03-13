import { providers } from "./models";

for (const providerId of Object.keys(providers)) {
  const provider = providers[providerId];
  console.log(`${provider.name}`);
  for (const modelId of Object.keys(provider.models)) {
    const model = provider.models[modelId];
    console.log(
      `  ${model.validated ? "✅" : "⚠️"} ${model.name} - ${JSON.stringify(model.modalities)}`,
    );
    console.log("    " + model.description_short);
  }
}
