''' Date 4-9-2018 '''

import re
for _ in range(int(raw_input())):
    try:
        reg = re.compile(raw_input())
        print True
    except re.error:
        print False