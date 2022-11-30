import sys
import re
import time
import collections

# SYS
print(sys.path)
# RE
text = 'Mi numero de telefono es 8, el codigo del pais Co es +57'
result = re.findall('[0-9]+', text)
print(result)
# TIME
timestamp = time.time()  # Hora en formato maquina
local = time.asctime(time.localtime())  # Hora en formato convencional
print(f'time 1: {timestamp}\ntime 2: {local}')
# COLLECTIONS
numbers = [1, 1, 2, 1, 3, 4, 1]
counter = collections.Counter(numbers)
print(counter)
