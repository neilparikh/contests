word = raw_input()
good = True
for c in word:
	if c not in ['I', 'O', 'S', 'H', 'Z', 'X', 'N']:
		good = False
		break

if good:
	print "YES"
else:
	print "NO"