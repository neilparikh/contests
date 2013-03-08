final = ""
k = int(raw_input())
for i in range(k):
  for j in range(k):
    final += "*"
  for j in range(k):
    final += "x"
  for j in range(k):
    final += "*"
  final += "\n"

for i in range(k):
  for j in range(k):
    final += " "
  for j in range(k):
    final += "x"
  for j in range(k):
    final += "x"
  final += "\n"

for i in range(k):
  for j in range(k):
    final += "*"
  for j in range(k):
    final += " "
  for j in range(k):
    final += "*"
  final += "\n"
print final,