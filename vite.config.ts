import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import path from "path";

// https://vite.dev/config/
export default defineConfig({
  base: "/static/",
  build: {
    manifest: true,
    outDir: "staticfiles",
    rollupOptions: {
      input: {
        "main.jsx": path.resolve(__dirname, "src/frontend/main.jsx"),
      },
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src/frontend/"),
    },
  },
  plugins: [react(), tailwindcss()],
});
