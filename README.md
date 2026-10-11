# Kero's SE WevMac

Mini vMac for the Macintosh SE, running in a web browser.

It is a WebAssembly build of [Mini vMac](https://www.gryphel.com/c/minivmac/). Start it with the stock ROM or your own 256K Mac SE ROM, insert a disk image, and download the image again with your changes.

A ROM file you choose on the page is read by your browser and stays there. Nothing is uploaded.

## Mac app

`app/` wraps the same emulator in a Mac app, built with [Tauri](https://tauri.app). It runs offline and saves disk images through a normal save dialog. The app also takes a 1 MB SE ROM-inator image, as one file or as its HI and LO halves, and boots from the ROM disk when you hold `R` at startup.

Files go in and out with ImportFl and ExportFl, Paul C. Pratt's Mini vMac utilities. The app carries them on a tools disk (`app/web/tools/WevMacTools.dsk`, GPL v2, source included on the disk). Open ImportFl on the Mac and pick a file in the app to send it in. Open a file with ExportFl and the app asks where to save it.

To build it on a Mac you need Node.js, Rust, and the Xcode command line tools:

    cd app
    npm install
    npx tauri build

The app lands in `app/src-tauri/target/release/bundle/`. Pushing to `main` also builds a universal app with GitHub Actions.

It is not notarized. The first time, open it with a right-click and Open, or allow it under Privacy & Security in System Settings.

## What's here

- `docs/` is the web page and the two emulator builds (early Mac SE and SE FDHD). GitHub Pages serves this folder.
- `patches/` is the small patch to Mini vMac and the commit it applies to.
- `build.sh` rebuilds the emulator with Emscripten.
- `app/` is the Mac app. It reuses the builds in `docs/` and has its own page in `app/web/`.

## Building

You need Emscripten with its SDL2 port, plus gcc and git.

    ./build.sh

The script clones Mini vMac at the pinned commit, applies the patch, and writes the builds into `docs/`. The patch adds what the page needs from the emulator: inserting a disk from the page, the file name and new-file calls that ImportFl and ExportFl use, and a notice when the Mac ejects something.

## Credits and license

Mini vMac was written by Paul C. Pratt, with later work by many contributors. It is licensed under the GNU GPL version 2, and so is this build. See `COPYING.txt`.

SE WevMac is a [Kero's Mac Mods](https://www.kerosmm.com) tool.
