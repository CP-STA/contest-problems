## Authored by Kay Akashi ##

def main():

	s = str(input())
	t = str(input())

	dic = {}
	for i in range(len(s)):
	    dic[s[i]] = 0
	for i in range(len(s)):
	    dic[s[i]] += 1
	for i in range(len(t)):
	    dic[t[i]] -= 1

	li = []
	for k, v in dic.items():
	    if v != 0:
	        li.append([k, v])
	li.sort()

	for el in li:
	    print(el[0], el[1])

if __name__ == '__main__':
	main()