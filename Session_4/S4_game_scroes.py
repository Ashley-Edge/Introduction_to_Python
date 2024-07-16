# Exercise 4.2:
#   Make a list of game scores.
#   Using list functions write code to output information of the scores in the following format:
#   Number of scores: 10
#   Highest score: 200
#   Lowest score: 3
#   Extension: Output all of the scores in descending order

game_scores = [3, 86, 200, 167, 34, 132, 199, 64, 183, 13]

print(f"Number of scores: {len(game_scores)}")
print(f"Highest score: {max(game_scores)}")
print(f"Lowest score: {min(game_scores)}")
print(f"Scores in descending order: {sorted(reversed(game_scores))}")
