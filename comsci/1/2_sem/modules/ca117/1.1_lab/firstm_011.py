#!/usr/bin/env python3

import sys

list = [print(line.replace("m", "M", 1).rstrip()) for line in sys.stdin]
