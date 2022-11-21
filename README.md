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

=ON WINDOWS=
Either download the provided jcc.exe or download entire repository and run build.ps1 (requires execution policy change)

NOTE: jcc files from before version 3 will not work in version 3 and above. Please recompile to fit this new format


    usage: jcc <file> [options]

    List of options:
    Misc Options:
        --help: Help menu
        --version: Print version     
    Build Options:
        --build: Build file into jcc file
        --nodep: Do not include dependencies in output jcc file
        -v (--verbose): Print verbose output
        --allowbadext: Do operation even if the input file has a disallowed extension
    Run Options:
        -f: Allow overwrite of files
        --tcc: Use the TCC (Tiny C Compiler) instead of default gcc
        --keeplog: Keep the compile log file even if the build was successfull
        --decompile: Extract files but do not run executable
        -v (--verbose): Print verbose output
        --allowbadext: Do operation even if the input file has a disallowed extension


Credits:
Python program by Enderbyte09
prime.c, prime.jcc, mathtrek.jcc by Enderbyte09
sort.c and sort.jcc by awesomegamer
snake.jcc by trogobit
