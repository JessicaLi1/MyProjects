import random
import requests

#a funtion to find a pokemon using its id number
def find_a_pokemon(n):
   
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(n)
    response = requests.get(url)
    pokemon = response.json()
    card={'name':pokemon['name'],'id':pokemon['id'],'height':pokemon['height'],'weight':pokemon['weight']}
    return card




#play a number of rounds of the choice of player, count total wins/lose/draws, output final result
player_wins=0
opponent_wins=0
draws=0

num_rounds = int(input('How many rounds do you want to play? '))
for game_rounds in range(num_rounds):

#replace print with input in some of these places so that user need to press a key/botton to continue, increases interactiveness, and prevents conponents of the game from outputting at the same time, improves user experience
    #find 3 random pokemons for the user to choose from (can let user choose the number of random pokemons in later updates)
    player_numbers=random.sample(range(151), 3)
    for num in player_numbers:
      print (find_a_pokemon(num))
      
    #player finds their pokemon
    player_num=int(float(input('Please choose a Pokemon from above (enter the id): ')))
    player_pokemon=find_a_pokemon(player_num)
    print (f'Your Pokemon: {player_pokemon}')

    #outputs a pokemon for the opponent, need player's reaction to coninue
    n2 = random.randint(0, 151)
    opponent_pokemon=find_a_pokemon(n2)
    print (f"Opponent's Pokemon: {opponent_pokemon['name']}")




    #find both players' stat choice
    player_choice=(input('Your choice of stat: '))
    opponent_choice=(random.choice(['id','height','weight']))
    print (f'Opponent\'s choice of stat: {opponent_choice}')
    input ("press enter to continue")

    #randomly decide and output player's choice or opponent's choice
    stat_choice=random.choice([player_choice,opponent_choice])

    if stat_choice==player_choice:
      print (f"It's going to be your choice {player_choice}")
    else:
      print (f"It's going to be the opponent's choice {opponent_choice}")

    input ('press enter to continue')

    print (f"Opponent's Pokemon stats: {opponent_pokemon}")

    input ('press enter to continue')





    #compare stats and output game result
    stat1=float(player_pokemon[stat_choice])
    stat2=float(opponent_pokemon[stat_choice])


    if stat1>stat2:
       print('You win!')
       player_wins=player_wins+1
    if stat1<stat2:
       print('You lose!')
       opponent_wins=opponent_wins+1

    if stat1==stat2:
       print('Draw')
       draws=draws+1

    input("press enter to continue")




    #at the end of the round, output 'next round', or at the end of the final round, output the final result
    if game_rounds<num_rounds-1:
      print('Next round')
    else:
      print('Final result:')
      print(f'You won {player_wins} games')
      print(f'Opponent won {opponent_wins} games')
      print(f'{draws} draws')
      input("press enter to continue")
      if player_wins>opponent_wins:
         print('You win the game!')
      if player_wins<opponent_wins:
         print('You lose the game!')
      elif player_wins<opponent_wins:
         print('The game is a draw')
