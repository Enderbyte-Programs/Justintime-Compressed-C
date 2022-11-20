# Justintime-Compressed-C

Just In Time, Compressed C
by Enderbyte09, inspiration by awesomegamer

This program is a way to make the *smallest* executables possible by compiling to bytecode first then comiling them just in time. 

    usage: jcc <file> [options]

    List of options:

    Build Options / Misc Options:
        --build: Build file into jcc file
        --help: Help menu
    Run Options:
        -f: Allow overwrite of files
        --tcc: Use the TCC (Tiny C Compiler) instead of default gcc
        --keeplog: Keep the compile log file even if the build was successfull