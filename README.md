# Kero's SE WevMac

Mini vMac for the Macintosh SE, running in a web browser.

It is a WebAssembly build of [Mini vMac](https://www.gryphel.com/c/minivmac/). Start it with the stock ROM or your own 256K Mac SE ROM, insert a disk image, and download the image again with your changes.

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
