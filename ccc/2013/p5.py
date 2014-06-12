def get_scores(games):
	scores = [0, 0, 0, 0, 0]
	for game in games:
		if game[2] == 0:
			scores[game[0]] += 1
			scores[game[1]] += 1
		else:
			scores[game[2]] += 3
	return scores

def chances(games_played, games_left):
	global chances_win
	if len(games_played) == 6:
		scores = get_scores(games_played)
		# print scores
		if max(scores) == scores[t] and scores.count(max(scores)) == 1:
			chances_win += 1
	else:
		games_left[0].append(0)
		games_played.append(games_left[0])
		
		# team one wins
		games_played[-1][2] = games_played[-1][0]
		chances(games_played[:], games_left[1:])
		
		# team two wins
		games_played[-1][2] = games_played[-1][1]
		chances(games_played[:], games_left[1:])
		
		# tie
		games_played[-1][2] = 0
		chances(games_played[:], games_left[1:])

t = int(raw_input())
g = int(raw_input())
chances_win = 0
games = [[1, 2], [1, 3], [1, 4],
		 [2, 3], [2, 4], [3, 4]]
games_played = []
for i in range(g):
	in_str = raw_input()
	split_info = in_str.split(" ")
	game = [int(split_info[0]), int(split_info[1]), 0]
	if split_info[2] > split_info[3]:
		game[2] = game[0]
	elif split_info[2] < split_info[3]:
		game[2] = game[1]
	games_played.append(game)
	
	if [game[0], game[1]] in games:
		games.pop(games.index([game[0], game[1]]))

chances(games_played[:], games)
print chances_win