#Bash shell script is easier to write than Python to combine all of files into one file.

#!/bin/bash
cat *.seq >> AllSeq.seq


#!/usr/bin/python
from glob import glob
for file in glob("416-ADH-*.seq"): # Any combination for the file names
    f= open(file,"r")  
    for lines in f.readlines():
        AllSeq= open("AllSeq.seq", "a")
        AllSeq.write(lines)
    f.close()
AllSeq.close()  
