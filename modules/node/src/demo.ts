import { providers } from "./models";

for (const provider of providers) {
  console.log(`${provider.name}`);
  for (const model of provider.models) {
    console.log(`  ${model.verified ? "✅" : "⚠️"} ${model.name}`);
  }
}
