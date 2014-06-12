t = int(raw_input())
c = int(raw_input())
num_done = 0
chores = []
for i in range(c):
	chores.append(int(raw_input()))
chores.sort()

while t > 0 and len(chores) > 0:
	t -= chores.pop(0)
	num_done += 1

if t == 0 or c == 0:
	num_done += 1

print num_done - 1