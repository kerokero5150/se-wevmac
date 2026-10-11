// Collect what the app's web view loads into dist/: the app page, the emulator
// builds and stock ROM from docs/, and the fonts.
import { cpSync, mkdirSync, rmSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const docs = join(here, "..", "docs");
const dist = join(here, "dist");

rmSync(dist, { recursive: true, force: true });
mkdirSync(join(dist, "fonts"), { recursive: true });

cpSync(join(here, "web", "index.html"), join(dist, "index.html"));
cpSync(join(here, "web", "logo.png"), join(dist, "logo.png"));
for (const f of readdirSync(docs)) {
  if (/^wevmac_.*\.(js|wasm)$/.test(f)) cpSync(join(docs, f), join(dist, f));
}
cpSync(join(docs, "roms"), join(dist, "roms"), { recursive: true });

const fonts = {
  "silkscreen": [400],
  "ibm-plex-sans": [400, 500, 600],
  "ibm-plex-mono": [400, 500],
};
for (const [family, weights] of Object.entries(fonts)) {
  for (const w of weights) {
    const f = `${family}-latin-${w}-normal.woff2`;
    cpSync(join(here, "node_modules", "@fontsource", family, "files", f), join(dist, "fonts", f));
  }
}
console.log("dist/ is ready");
