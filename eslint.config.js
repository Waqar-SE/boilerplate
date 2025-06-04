import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import deMorgan from "eslint-plugin-de-morgan";
import noSecrets from "eslint-plugin-no-secrets";
import { defineConfig } from "eslint/config";

export default defineConfig([
  { ignores: ["*", "!src/frontend/**/*"] },
  {
    plugins: { js },
    extends: ["js/recommended"],
  },
  {
    languageOptions: { globals: globals.browser },
  },
  {
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "warn",
    },
  },
  {
    plugins: {
      "no-secrets": noSecrets,
    },
    rules: {
      "no-secrets/no-secrets": "error",
    },
  },
  deMorgan.configs.recommended,
  tseslint.configs.recommended,
  pluginReact.configs.flat.recommended,
]);
