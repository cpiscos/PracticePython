name1 = input('Player 1\'s name?:\n')
name2 = input('Player 2\'s name?:\n')
player1 = input(name1 + ' - Rock, Paper, or Scissors?\n').lower()
player2 = input(name2 + ' - Rock, Paper, or Scissors?\n').lower()
if player1 not in ['rock', 'paper', 'scissors']:
    print('input not valid')
    exit()
if player1 == player2:
    print('Tie!')
elif player1 == 'rock':
    if player2 == 'scissors':
        print(name1 + ' wins!')
    else:
        print(name2 + ' wins!')
elif player1 == 'paper':
    if player2 == 'rock':
        print(name1 + ' wins!')
    else:
        print(name2 + ' wins!')
elif player1 == 'scissors':
    if player2 == 'rock':
        print(name1 + ' wins!')
    else:
        print(name2 + ' wins!')