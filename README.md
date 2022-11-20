# Justintime-Compressed-C

Just In Time, Compressed C
by Enderbyte09, inspiration by awesomegamer

This program is a way to make the *smallest* executables possible by compiling to bytecode first then comiling them just in time. 
How to install:
Download either using the button or git clone. cd in to the directory. A total of 15 MB is required for installation Like most programs, JCC can be built and installed with three commands:
./configure (makes sure you have all the packages required for building)
make (builds program and places executable in directory)
make install (Installs JCC to /usr/bin)
make clean (optional, cleans up temporary files left from build)


    usage: jcc <file> [options]

    List of options:
    Misc Options:
        --help: Help menu
        --version: Print version       
    Build Options:
        --build: Build file into jcc file
        --nodep: Do not include dependencies in output jcc file
    Run Options:
        -f: Allow overwrite of files
        --tcc: Use the TCC (Tiny C Compiler) instead of default gcc
        --keeplog: Keep the compile log file even if the build was successfull
        -v (--verbose): Print verbose output during extraction
