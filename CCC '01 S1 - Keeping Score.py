cards = input()

club_index = cards.index("C")
diamond_index = cards.index("D")
heart_index = cards.index("H")
spades_index = cards.index("S")

clubs = cards[club_index+1: diamond_index]
diamonds = cards[diamond_index+1: heart_index]
hearts = cards[heart_index+1: spades_index]
spades = cards[spades_index+1:]

club_points = 0
diamond_points = 0
heart_points = 0
spade_points = 0

club_points += clubs.count("A")*4 + clubs.count("K")*3 + clubs.count("Q")*2 + clubs.count("J")*1
diamond_points += diamonds.count("A")*4 + diamonds.count("K")*3 + diamonds.count("Q")*2 + diamonds.count("J")*1
heart_points += hearts.count("A")*4 + hearts.count("K")*3 + hearts.count("Q")*2 + hearts.count("J")*1
spade_points += spades.count("A")*4 + spades.count("K")*3 + spades.count("Q")*2 + spades.count("J")*1

if len(clubs) == 0:
    club_points += 3
elif len(clubs) == 1:
    club_points += 2
elif len(clubs) == 2:
    club_points += 1

if len(diamonds) == 0:
    diamond_points += 3
elif len(diamonds) == 1:
    diamond_points += 2
elif len(diamonds) == 2:
    diamond_points += 1

if len(hearts) == 0:
    heart_points += 3
elif len(hearts) == 1:
    heart_points += 2
elif len(hearts) == 2:
    heart_points += 1

if len(spades) == 0:
    spade_points += 3
elif len(spades) == 1:
    spade_points += 2
elif len(spades) == 2:
    spade_points += 1

club = ""
diamond = ""
heart = ""
spade = ""


for i in range(len(clubs)):
    club += clubs[i] + " "

for i in range(len(diamonds)):
    diamond += diamonds[i] + " "

for i in range(len(hearts)):
    heart += hearts[i] + " "

for i in range(len(spades)):
    spade += spades[i] + " "

print("Cards Dealt Points")
print("Clubs " + club + str(club_points))
print("Diamonds " + diamond + str(diamond_points))
print("Hearts " + heart + str(heart_points))
print("Spades " + spade + str(spade_points))
print(" Total " + str(club_points+diamond_points+heart_points+spade_points))