#!/usr/bin/env python3

import os
import sys

path = sys.argv[1]
prefix = path.split(".")[0]
ext = path.split(".")[1]

command = "pandoc -f markdown " + path + " -t latex -o " + prefix + ".pdf"
move_buff = "mv " + prefix + ".pdf " + prefix + "-buff" + ".pdf"
if ext == "md":
    os.system(move_buff)
    os.system(command)
