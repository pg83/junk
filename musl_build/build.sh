set -e
set -x

rm -rf ./lib && mkdir lib
PATH=~/tcc/bin:$PATH CC=tcc make Makefile clean
PATH=~/tcc/bin:$PATH CC=tcc make Makefile all
PATH=~/tcc/bin:$PATH CC=tcc tcc -nostdinc -static -nostdlib -I./include ~/tcc/lib/libtcc.a ~/tcc/lib/tcc/libtcc1.a ./lib/libc.a ./qw.c ./lib/libc.a ~/tcc/lib/tcc/libtcc1.a ./lib/crt* ./lib/libc.a
