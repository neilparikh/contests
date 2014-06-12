year = int(raw_input()) + 1
while True:
	year_s = str(year)
	g = True
	for c in year_s:
		if year_s.count(c) != 1:
			g = False
	if g:
		print year
		break
	year += 1