import json

slug = 'within-half-an-hour'
path = '/Users/akashiaya/Desktop/problems-private/' + slug
with open(path + '/test-cases.json') as f:
	jsn = json.load(f)

IN = []
for el in jsn:
	IN.append(el['input'])
IN = str(len(jsn)) + '\n' + ''.join(IN)

with open(path + '/input.txt', 'w') as f:
	f.write(IN)


import time
from solution2 import main

t = int(input())

ex_times = []
for _ in range(t):
	start = time.time()
	main()
	end = time.time()
	ex_time = str(end * 1000 - start * 1000) + ' ' + '(ms)'
	ex_times.append(ex_time)
	print()

for i in range(len(ex_times)):
	print(i, ex_times[i])