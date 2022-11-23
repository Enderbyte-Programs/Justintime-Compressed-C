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

##ON WINDOWS##

Either download the provided jcc.exe or download entire repository and run build.ps1 (requires execution policy change)

NOTE: jcc files from before version 3 will not work in version 3 and above. Please recompile to fit this new format


    usage: jcc <file> [options]

    List of options:
    Misc Options:
        --help: Help menu
        --version: Print version  
        --validatecache: Validates cache
        --clearcache: Clears cache
        --cstat: Get statistics about the cache   
    Build Options:
        --build: Build file into jcc file
        --nodep: Do not include dependencies in output jcc file
        -v (--verbose): Print verbose output
        --allowbadext: Do operation even if the input file has a disallowed extension
        --notest: Do not run compile test when building JCC
        --nocompileout: Do not display compiler output during test
    Run Options:
        -f: Allow overwrite of files
        --tcc: Use the TCC (Tiny C Compiler) instead of default gcc
        --keeplog: Keep the compile log file even if the build was successfull
        --decompile: Extract files but do not run executable
        -v (--verbose): Print verbose output
        --allowbadext: Do operation even if the input file has a disallowed extension
        --showout: Show compiler output during build
        --nocache: Do not add this file to cache
        --rebuild: Do not check cache and force rebuild
        --checkcache: Check if program is in cache but do not run



Credits:
Python program by Enderbyte09
prime.c, prime.jcc, mathtrek.jcc by Enderbyte09
sort.c and sort.jcc by awesomegamer
snake.jcc by trogobit

## Changelog
    JCC 7 [2022-11-22]
    Type: Feature add
    Contributors: Enderbyte09
        -Added Cache
            -Works on Windows and Linux
            -Set to [USER FOLDER]/.jcccache
            -Contains executables that is copied
    
    JCC 6 [2022-11-21]
    Type: Feature add
    Contributors: Enderbyte09
        -Added preliminary testing
            -Tests code when --build ing
            -Defaults gcc output to stdout
            -Unless --nocompileout is specified, in which case it will not generate any
            -Disable this testing with the --notest arg
        -Improved compression algorith
            -Now removes empty spaces from lines, *improving efficiency*
            -Applies to both normal files and header files
    
    JCC 5.1 [2022-11-21]
    Type: Bugfix
    Contributors: Enderbyte09
        -Fixed bug where you coulc not run any jcc files
        
    JCC 5 [2022-11-21]
    Type: Feature add
    Contributors: Enderbyte09
        -Added hi.c testing file
        -Added windows support
            -Changed end extension to .exe as it makes no difference on Linux
            -Added build.sh1, equivilant of Makefile
            -REQUIRES MINGW INSTALLATION AND ADD2PATH, WHICH IS NOT PROVIDED WITH THIS SOFTWARE
        -Warning will now be displayed on files that don't have the right extension
            -Bypass this with --allowbadext
        -Added --decompile
            Decompiles JCC placing headers in the same directory and target C file as .temp__.c
    
    JCC 4 [2022-11-20]
    Type: Bugfix
    Contributors: Enderbyte09
        -Improved compression algorithm by removing comments on header files
        
    JCC 3 [2022-11-20]
    Type: Feature add
    Contributors: Enderbyte09, troglobit, awesomegamer
        -Added support for bundling dependency headers
            -MUST BE IN CURRENT WORKING DIRECTORY
        -Added --nodep arg
            -Does NOT bundle dependency
        -Changed executable format, old programs will NOT WORK
    
    JCC 2 [2022-11-20]
    Type: Feature add
    Contributors: Enderbyte09
        -Improved compression by removing comments from files
        
    JCC 1 [2022-11-19]
    NO INFO
