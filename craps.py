import random

def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll = int(roll1 + roll2)
    return roll

def craps():
    name = input("Please enter your name: ")
    players = {'Matt': 1000, 'Johnny': 1000, 'Jack': 1000}
    if name in players:
        new_name = random.choice(['Tommy', 'Lisa', 'Patty'])
        players[new_name] = players.pop(name)
        print(f"Sorry the name {name} is already taken. Your new name will be {new_name}.")
        name = new_name
    players[name] = 1000
    print(f"Welcome {name}. Your balance is 1000 dollars.")

    while True:
        # Bet round
        bets = {}
        for player, balance in players.items():
            if balance <= 0:
                continue
            bet = 0
            if player == name:
                while bet <= 0 or bet > balance:
                    bet = int(input(f"{player}, how much do you want to bet? (your balance is {balance}) "))
            else:
                bet = random.randint(1, balance)
                print(f"{player} placed a bet of {bet}.")
            bets[player] = bet
        print("Bets placed:", bets)

        roll = roll_dice()
        if roll in [7, 11]:
            print(f"You win! You rolled {roll}.")
            for player, bet in bets.items():
                players[player] += bet
        elif roll in [2, 3, 12]:
            print(f"You lose! You rolled {roll}.")
            for player, bet in bets.items():
                players[player] -= bet
        else:
            print(f"You rolled a {roll}. Point is {roll}.")
            while True:
                user_input = input("Press 'Enter' to roll the dice again or type 'Exit' to close the game")
                if user_input.lower() == 'exit':
                    break
                shoot = roll_dice()
                if shoot == 7:
                    print(f"You rolled a {shoot}. You lose!")
                    for player, bet in bets.items():
                        players[player] -= bet
                    break
                elif shoot == 11:
                    print(f"You rolled {shoot}. You lose!")
                    for player, bet in bets.items():
                        players[player] -= bet
                    break
                elif shoot == roll:
                    print(f"You rolled {shoot}, And the point was {roll}. You win!")
                    for player, bet in bets.items():
                        players[player] += bet
                    break
                else:
                    print(f"Try again. You rolled {shoot}")

        # Check if any player is out of money
        for player, balance in players.items():
            if balance <= 0:
                print(f"{player} is out of money and is eliminated!")
                del players[player]

        # Check if only one player is left
        if len(players) == 1:
            winner = list(players.keys())[0]
            print(f"Congratulations {winner}, you are the winner with a balance of {players[winner]}!")
            break

        # Check if all players are out of money
        if not players:
            print("No players left! Game over.")
            break

craps()
