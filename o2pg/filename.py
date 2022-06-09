import os

# dirname=r'C:\Users\hp\Desktop\o2pg'
# lst = os.listdir(dirname)
#
# for i in lst:
#     if i.endswith('sql'):
#         print(i)

import re

s = 'NUMBER(33)'

res = re.sub(r"NUMBER\([1-9]\)", 'int4', s)
print(res)
