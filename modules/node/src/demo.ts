import chalk from "chalk";
import { providers } from "./models";

//  Loop through each provider.
for (const providerId of Object.keys(providers)) {
  //  Show a summary of each provider.
  const provider = providers[providerId];
  console.log(chalk.blue.bold(provider.name));

  //  Loop through all of the models.
  for (const modelId of Object.keys(provider.models)) {
    const indent = "  ";
    const model = provider.models[modelId];
    console.log(
      chalk.green.bold(`${indent} ${model.name}`) +
        chalk.grey(": " + model.description_short),
    );
  }
}
