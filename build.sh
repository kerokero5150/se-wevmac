#!/bin/bash
# Build SE WevMac: Mini vMac for the Mac SE and SE FDHD, compiled to WebAssembly,
# with a 1 MB ROM space.
#
# Needs: emcc (Emscripten) with the SDL2 port, gcc, git.
set -e
cd "$(dirname "$0")"
COMMIT=$(cat patches/MINIVMAC_COMMIT)
if [ ! -d minivmac ]; then
  git clone https://github.com/minivmac/minivmac.git
  (cd minivmac && git checkout "$COMMIT" && git apply ../patches/minivmac-wevmac.patch)
fi
cd minivmac
gcc setup/tool.c -o setuptool
SRCS="MINEM68K OSGLUSDL GLOBGLUE M68KITAB VIAEMDEV IWMEMDEV SCCEMDEV RTCEMDEV ROMEMDEV SCSIEMDV SONYEMDV SCRNEMDV MOUSEMDV ADBEMDEV SNDEMDEV PROGMAIN"
for V in SE SEFDHD; do
  rm -rf cfg bld
  ./setuptool -t lx64 -m $V -api sd2 -n "sewevmac" -sound 1 -mem 4M -speed z > setup.sh
  bash setup.sh
  # A 256K ROM is repeated by the page to fill the 1 MB ROM space.
  sed -i 's/#define kROM_Size .*/#define kROM_Size 0x00100000/' cfg/CNFUDALL.h
  mkdir -p wbld_$V; OBJS=""
  for s in $SRCS; do
    # main is renamed so the page decides when the emulator starts.
    emcc src/$s.c -c -O2 -Dmain=vmac_main -DCheckRomCheckSum=0 -Icfg -Isrc -sUSE_SDL=2 -o wbld_$V/$s.o
    OBJS="$OBJS wbld_$V/$s.o"
  done
  emcc $OBJS -O2 -sUSE_SDL=2 -sASYNCIFY -sALLOW_MEMORY_GROWTH=1 -sINVOKE_RUN=0 -sMODULARIZE=1 -sEXPORT_NAME=WevMac_$V \
    -sEXPORTED_FUNCTIONS='["_vmac_main","_wevmac_insert_disk"]' -sEXPORTED_RUNTIME_METHODS='["FS","ccall"]' \
    -o ../docs/wevmac_$V.js
done
