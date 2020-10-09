sport = input("Enter sport name: ")

p1_score = input("Enter P1 score: ")

p2_score = input("Enter P2 score: ")

if p1_score == p2_score:
    print("The game is a draw.")

elif sport.lower() == "basketball" or sport.lower() == "golf":
    p1_wins_basketball = sport == "basketball" and p1_score > p2_score
    p1_wins_golf = sport == "golf" and p1_score < p2_score

    p1_wins = p1_wins_golf or p1_wins_basketball

    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport.")
