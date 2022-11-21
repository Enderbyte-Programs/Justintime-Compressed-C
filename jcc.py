import zlib
import sys
import os
import random
import re
from platform import system as getos
if getos() == "Windows":
    NT = True
else:
    NT = False
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)
def compressfile(filename: str,verbose=False) -> bytes:
    with open(filename) as f:
        data = f.read()
    if verbose:
        print(f"{filename} insize {len(data)} bytes")
    result = zlib.compress(comment_remover(data).encode(),9)
    if verbose:
        print(f"{filename} csize {len(result)} bytes")
    return result
if "--help" not in sys.argv and "--version" not in sys.argv:
    if len(sys.argv) < 2:
        print("Please provide a file name. For help, please run with --help")
        sys.exit()
def vbprint(data: str) -> None:
    if VERBOSE:
        print(data)
infile = sys.argv[1]
ext = infile.split(".")[-1]
if "-v" in sys.argv or "--verbose" in sys.argv:
    VERBOSE = True
else:
    VERBOSE = False
if "--build" in sys.argv:
    #Build to .jcc
    if ext != "c" and "--allowbadext" not in sys.argv:
        print("Invalid input file. Please use .c files only for building or run with argument --allowbadext")
        if ext == "jcc":
            print("This file is already built. To run, execute jcc <file>")
        sys.exit()
    vbprint("opening file")
    if os.path.isfile(infile):
        with open(infile,'r') as f:
            ldata = f.read()
        vbprint(f"Infile data length: {len(ldata)}")
        ldata = comment_remover(ldata)
        vbprint(f"Parsed infile length: {len(ldata)}")
        vbprint("Finding dependencies...")
        linc = 0
        writedata = b""
        if "--nodep" not in sys.argv:
            for line in ldata.splitlines():
                if line[0:3] == "#in":
                    effline = ldata.splitlines()[linc]
                    lcdep = effline.split(" ")[1].strip()
                    if lcdep[0] == "\"":
                        lcdep = lcdep.replace("\"","")
                        vbprint(f"Found dependency {lcdep}")
                        writedata += lcdep.encode() + b"$SDEP$"
                        if not os.path.isfile(lcdep):
                            print(f"ERROR! Dependency file {lcdep} could not be found. Make sure it is in the same directory as cwd!")
                        writedata += compressfile(lcdep,True) + b"$EDEP$"
                linc += 1

        cdata = zlib.compress(ldata.encode(),9)
        vbprint(f"Compressed data length: {len(cdata)}")
        writedata += b"$DATA$"
        writedata += cdata
        vbprint(f"Total length: {len(writedata)} bytes")
        vbprint("Writing data...")
        
        with open(infile.split(".")[-2]+".jcc","wb+") as g:
            g.write(writedata)
        vbprint("Done!")
    else:
        print("ERROR File not found.")
elif "--version" in sys.argv:
    print("JCC 5 [BETA]")
elif "--help" in sys.argv:
    print("""Just In Time Compressed C
    By Enderbyte Programs
    
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
        """)
else:
    ridcode = random.randint(1,9999)#Prevent conflict
    if ext != ".jcc" and "--allowbadext" not in sys.argv:
        print("I can only run files with a jcc extension. If you are sure that this is a jcc file, run jcc with --allowbadext")
        if ext == "c":
            print("To build a C program in to a jcc file, run jcc <file> --build")
        sys.exit()
    vbprint("Opening file")
    if os.path.isfile(infile):
        with open(infile,'rb') as f:
            ldata = f.read()
        HEAD = ldata.split(b"$DATA$")[0]
        ldata = ldata.split(b"$DATA$")[1]
        vbprint(f"Data length: {len(ldata)} bytes | Header length: {len(HEAD)} bytes")

        vbprint("Decompressing data")
        ffldata = zlib.decompress(ldata,zlib.MAX_WBITS|32)
        vbprint("Writing temp file")
        try:
            with open(".temp__.c","x") as k:
                k.write(ffldata.decode())
        except FileExistsError:
            if "-f" in sys.argv:#Force it
                with open(".temp__.c","w+") as k:
                    k.write(ffldata.decode())
            else:
                print("Error. Temp file already exists. Run rm .temp__.c to fix this")
                sys.exit()

        #Header stuff here
        vbprint("Writing dependancies")
        lfixes = {}
        deps = []
        if len(HEAD) > 10:
            depdat = HEAD.split(b"$EDEP$")
            depdat = [d for d in depdat if d != b'']#Removing empty strings
            for dependancy in depdat:
                depname = dependancy.split(b"$SDEP$")[0]
                depstuff = dependancy.split(b"$SDEP$")[1]
                vbprint(f"Writing dependancy {depname}")
                deps.append(depname)
                if os.path.isfile(depname):
                    vbprint("Dependancy path already exists. Renaming")
                    lfixes[depname] = depname + b" (copy)"
                    os.rename(depname,depname+b" (copy)")
                with open(depname,"w+") as f:
                    vbprint(f"Decompressing {depname}")
                    f.write(zlib.decompress(depstuff).decode())
            vbprint("Finished unpacking!")
        #input()
        if "--decompile" not in sys.argv:
            vbprint("Building...")
            if "--tcc" not in sys.argv:
                p = os.system(f"gcc .temp__.c -lm -O -o .temp{ridcode}.exe 2> compile.log")
            else:
                p = os.system(f"tcc .temp__.c -lm -o .temp{ridcode}.exe 2> compile.log")
            if p != 0:
                print("Compile error! (see log)")
                sys.exit(-1)
            for ldep in deps:
                os.remove(ldep)
            for lk in lfixes.keys():
                os.rename(lfixes[lk],lk)#Reverting file system
            else:
                if "--keeplog" not in sys.argv:
                    os.remove("compile.log")#Keeping log in case people want to read it 
            os.remove(".temp__.c")
            if not NT:
                i = os.system(f"./.temp{ridcode}.exe")
            else:
                i = os.system(f".temp{ridcode}.exe")
            if i != 0:
                print(f"Program exited with code {i}. This is usually an error")
            os.remove(f".temp{ridcode}.exe")
        else:
            print("Find decompiled main file at .temp__.c")
    else:
        print("ERROR File not found.")