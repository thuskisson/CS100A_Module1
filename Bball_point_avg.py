# Game Point Totals
game1 = input("Enter total points scored in game 1  ")
game2 = input("Enter total points scored in game 2  ")
game3 = input("Enter total points scored in game 3  ")
game4 = input("Enter total points scored in game 4  ")
game5 = input("Enter total points scored in game 5  ")

#Make sure point totals are of type int
game1 = int(game1)
game2 = int(game2)
game3 = int(game3)
game4 = int(game4)
game5 = int(game5)

# Total points for all the games played
Total_Points = (game1 + game2 + game3 + game4 + game5)

# Average points for all the games played
Avg_ppg = (Total_Points / 5)

print(f"Average Points Per Game: {Avg_ppg}")