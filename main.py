
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        def sort_number (pokemons):
            return int(pokemons["number"])
        index=int(input("Ievadiet Pokemona Nummuru"))
        pokemons.sort(key = sort_number)
        print(pokemons[index])


        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sort_total (pokemons):
            return int(pokemons["total"])
        pokemons.sort(key = sort_total, reverse = True)
        print(pokemons[:11])
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sort_total (pokemons):
            return int(pokemons["total"])
        pokemons.sort(key = sort_total, reverse = False)
        print(pokemons[:11])
        pass
    elif choice == '4':
        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
         
        START=input("Press Enter to Start")
        player = str(input("Enter YOure Name"))
        computer_name = str("DUNGEON MASTER")
        print("CHOOSE YOURE CAHMPION")


        print("Enemie has chosen") 
        comp_choice = random.randint(0, 42)
        print(pokemons[comp_choice])
        pokemon_1 = pokemons[comp_choice]

        player_choice = int(input("Ievadiet jūsu pokemona indeksu"))
        print(pokemons[player_choice])
        pokemon_2 = pokemons[player_choice]

        
        








    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


