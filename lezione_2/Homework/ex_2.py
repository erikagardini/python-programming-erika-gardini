s = "fire and ice"

print(s[2])

print(s[4])

print(s[9])

print(s[-1])

print(s[-2])

print(s[0::2])
print(s[1::2])

to = len(s) / 2
to = int(to)
print(to)
print(s[0:to])

s_reversed = s[::-1]
print(s_reversed)

count = s.count("i") + s.count("e")
print(count)

s = s.replace("and", "&")
print(s)

print(s.find("fire"))

print(s.find("re and"))

print(s.find("re &"))

pos = s.find("e")
print(pos)

pos = s_reversed.find("e")
print(len(s_reversed) - pos)

s = "234 4329 7654 8923"
for el in s:
	if el.isdigit():
		num = int(el)
		print(num + 3)





