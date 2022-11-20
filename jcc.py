import zlib
import sys
import os
import random
if len(sys.argv) < 2:
    print("Please provide a file name.")
    sys.exit()
infile = sys.argv[1]
if "--build" in sys.argv:
    #Build to .jcc
    print("opening file")
    if os.path.isfile(infile):
        with open(infile,'r') as f:
            ldata = f.read()
        print(f"Infile data length: {len(ldata)}")
        if len(ldata) > 70:

            print("Compressing...")
            cdata = zlib.compress(ldata.encode(),9)
            print(f"Compressed data length: {len(cdata)}")
        else:
            cdata = ldata.encode()#Shorter than 70 bytes, no point in compressing
        print("Writing data...")
        with open(infile.split(".")[-2]+".jcc","wb+") as g:
            g.write(cdata)
        print("Done!")
    else:
        print("ERROR File not found.")
elif "--test" in sys.argv:
    for i in range(10,1000000,10):
        tdat = "".join([random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]) for j in range(i)])
        cdata = zlib.compress(tdat.encode(),9)
        print(f"Length: {i}, csize: {len(cdata)}, Ratio : {i/len(cdata)}")
else:
    ridcode = random.randint(1,9999)#Prevent conflict
    #print("opening file")
    if os.path.isfile(infile):
        with open(infile,'rb') as f:
            ldata = f.read()
        if len(ldata) > 70:
            ffldata = zlib.decompress(ldata,zlib.MAX_WBITS|32)
        else:
            ffldata = ldata
        try:
            with open(".temp__.c","x") as k:
                k.write(ffldata.decode())
        except FileExistsError:
            print("Error. Temp file already exists. Run rm .temp__.c to fix this")
            sys.exit()
        if "--gcc" in sys.argv:
            p = os.system(f"tcc .temp__.c -lm -O -o .temp{ridcode}.lexe")
        else:
            p = os.system(f"tcc .temp__.c -lm -o .temp{ridcode}.lexe")
        if p != 0:
            print("Compile error! (see log)")
            sys.exit()
        os.remove(".temp__.c")
        i = os.system(f"./.temp{ridcode}.lexe")
        if i != 0:
            print(f"Program exited with code {i}. This is usually an error")
        os.remove(f"./.temp{ridcode}.lexe")
    else:
        print("ERROR File not found.")