import os
for f in os.listdir("."):
    r = f.replace(" ","_")
    r = r.replace("·","-")
    if( r != f):
        os.rename(f,r)