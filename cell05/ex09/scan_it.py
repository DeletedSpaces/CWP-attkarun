#!/usr/bin/env python3
import re
import sys
if len(sys.argv) != 3:
    print("none")
else:
    matches = re.findall(sys.argv[1], sys.argv[2])
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))
