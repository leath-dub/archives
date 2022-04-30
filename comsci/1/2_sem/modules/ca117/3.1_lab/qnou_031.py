#!/usr/bin/env python3

import sys

print("Words with q but no u:", [word.strip() for word in sys.stdin if "q" in word.lower().replace("qu", "")])
