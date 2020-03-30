import re

S = input()

match = re.search(pattern=r'^(dream|dreamer|erase|eraser)+$',
                  string=S)

print('YES' if match else 'NO')
