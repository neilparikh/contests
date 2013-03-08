k = int(raw_input())
word = raw_input()
final = ""

i = 1
for c in word:
  s = 26 - (3 * i) - k
  c_new = (ord(c) - 64 + s) % 26
  if c_new == 0:
    c_new = 26
  final += chr(c_new + 64)
  i += 1
print final