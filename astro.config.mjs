// Astro settings for the Space Array website.
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://spacearray.org",
  // Build news.astro as news.html, so every page keeps its old address.
  build: { format: "file" },
  // Keep the HTML as written. Do not squeeze the spaces out of it.
  compressHTML: false,
});
