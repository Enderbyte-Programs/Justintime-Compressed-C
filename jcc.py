import zlib
import sys
import os
import random
import re
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
if "--help" not in sys.argv:
    if len(sys.argv) < 2:
        print("Please provide a file name. For help, please run with --help")
        sys.exit()
infile = sys.argv[1]
if "--build" in sys.argv:
    #Build to .jcc
    print("opening file")
    if os.path.isfile(infile):
        with open(infile,'r') as f:
            ldata = f.read()
        print(f"Infile data length: {len(ldata)}")
        ldata = comment_remover(ldata)
        print(f"Parsed infile length: {len(ldata)}")
        cdata = zlib.compress(ldata.encode(),9)
        print(f"Compressed data length: {len(cdata)}")
        print("Writing data...")
        with open(infile.split(".")[-2]+".jcc","wb+") as g:
            g.write(cdata)
        print("Done!")
    else:
        print("ERROR File not found.")
elif "--help" in sys.argv:
    print("""Just In Time Compressed C
    By Enderbyte Programs
    
    usage: jcc <file> [options]

    List of options:

    Build Options / Misc Options:
        --build: Build file into jcc file
        --help: Help menu
    Run Options:
        -f: Allow overwrite of files
        --tcc: Use the TCC (Tiny C Compiler) instead of default gcc
        --keeplog: Keep the compile log file even if the build was successfull""")
else:
    ridcode = random.randint(1,9999)#Prevent conflict
    #print("opening file")
    if os.path.isfile(infile):
        with open(infile,'rb') as f:
            ldata = f.read()
        ffldata = zlib.decompress(ldata,zlib.MAX_WBITS|32)
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
        if "--tcc" not in sys.argv:
            p = os.system(f"gcc .temp__.c -lm -O -o .temp{ridcode}.lexe 2> compile.log")
        else:
            p = os.system(f"tcc .temp__.c -lm -o .temp{ridcode}.lexe 2> compile.log")
        if p != 0:
            print("Compile error! (see log)")
            sys.exit(-1)
        else:
            if "--keeplog" not in sys.argv:
                os.remove("compile.log")#Keeping log in case people want to read it 
        os.remove(".temp__.c")
        i = os.system(f"./.temp{ridcode}.lexe")
        if i != 0:
            print(f"Program exited with code {i}. This is usually an error")
        os.remove(f"./.temp{ridcode}.lexe")
        
    else:
        print("ERROR File not found.")