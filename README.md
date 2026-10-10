# SE WevMac

Mini vMac for the Macintosh SE, running in a web browser.

It is a WebAssembly build of [Mini vMac](https://www.gryphel.com/c/minivmac/) with one change that matters: the ROM space is 1 MB instead of 256K. That lets it load an SE ROM-inator image and boot from the ROM disk at `$440000`, the same way the real board does. Hold `R` at startup, or tick the box on the page and it holds the key for you.

A ROM file you choose on the page is read by your browser and stays there. Nothing is uploaded.

## What's here

- `docs/` is the web page and the two emulator builds (early Mac SE and SE FDHD). GitHub Pages serves this folder.
- `patches/` is the small patch to Mini vMac and the commit it applies to.
- `build.sh` rebuilds the emulator with Emscripten.

## Building

You need Emscripten with its SDL2 port, plus gcc and git.

    ./build.sh

The script clones Mini vMac at the pinned commit, applies the patch, and writes the builds into `docs/`.

## Credits and license

Mini vMac was written by Paul C. Pratt, with later work by many contributors. It is licensed under the GNU GPL version 2, and so is this build. See `COPYING.txt`.

SE WevMac is a [Kero's Mac Mods](https://www.kerosmm.com) tool.
