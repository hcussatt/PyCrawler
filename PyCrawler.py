"""
Henry Cussatt
henry.cussatt@uvm.edu
CS 021 Final Project
"""
import random
import time
import tile_generator
import os

def gen_map(floor):
    stairs_bounds = 3,6
    stairs_bounds_2 = 2,4
    floor_inventory = [2,2,2]
    if floor == 2:
        stairs_bounds = 0,3
        stairs_bounds_2 = 0,2
    if floor != 3:
        map = [[1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1]]
        shop = 0,0
        chest = 0,0
        stairs = random.randint(stairs_bounds[0],stairs_bounds[1]),random.randint(stairs_bounds_2[0],stairs_bounds_2[1])
        while shop[0] == chest[0] and shop[1] == chest[1]:
            shop = random.randint(0,6), random.randint(0,4)
            chest = random.randint(0,6), random.randint(0,4)
        while (stairs[0] == shop[0] and stairs[1] == shop[1]) or (stairs[0] == chest[0] and stairs[1] == chest[1]):
            stairs = random.randint(stairs_bounds[0],stairs_bounds[1]), random.randint(stairs_bounds_2[0],stairs_bounds_2[1])
        while (shop == [0,0]):
            shop = random.randint(0,6), random.randint(0,4)
        while (chest == [0,0]):
            chest = random.randint(0,6), random.randint(0,4)
            
        map[shop[1]][shop[0]] = map[shop[1]][shop[0]] * 2
        map[chest[1]][chest[0]] = map[chest[1]][chest[0]] * 3
        map[stairs[1]][stairs[0]] = map[stairs[1]][stairs[0]] * 4
    else:
        map = [[1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1]]
        shop = 0,0
        chest = 0,0
        stairs = random.randint(stairs_bounds[0],stairs_bounds[1]),random.randint(stairs_bounds_2[0],stairs_bounds_2[1])
        while shop[0] == chest[0] and shop[1] == chest[1]:
            shop = random.randint(0,6), random.randint(0,4)
            chest = random.randint(0,6), random.randint(0,4)
        while (stairs[0] == shop[0] and stairs[1] == shop[1]) or (stairs[0] == chest[0] and stairs[1] == chest[1]):
            stairs = random.randint(stairs_bounds[0],stairs_bounds[1]), random.randint(stairs_bounds_2[0],stairs_bounds_2[1])
        map[shop[1]][shop[0]] = map[shop[1]][shop[0]] * 2
        map[chest[1]][chest[0]] = map[chest[1]][chest[0]] * 3
        map[stairs[1]][stairs[0]] = map[stairs[1]][stairs[0]] * 5
    return map

def draw_map(map, floor, coins):
    os.system("clear")
    print(f"Floor {floor} \t\t\t {coins} coins")
    for i in range(len(map)):
        for k in range(11):
            print("")
            for h in map[i]:
                if h % 10 == 0:
                    print(tile_generator.player(k), end=" ")
                elif h == 2:
                    print(tile_generator.shop(k), end=" ")
                elif h == 3:
                    print(tile_generator.chest(k), end=" ")
                elif h == 4:
                    print(tile_generator.stairs(k), end=" ")
                elif h == 5:
                    print(tile_generator.boss(k), end = " ")
                else:
                    print(tile_generator.empty(k), end=" ")


def start():
    os.system("clear")
    start = ""
    while start.lower() != "start":
        with open("start_screen.txt") as f:
            for line in f:
                print(line.strip())
        start = input("")
        if start.lower() == "quit":
            quit()
    return "move"
        

def movement(x, y, map, inventory_list, floor):
    encounter = 1

    while True:
        map[y][x] = map[y][x] * 10
        draw_map(map, floor, inventory_list["coins"][0])
        map[y][x] = map[y][x] / 10
        move = input("\nWhich direction would you like to move? (N)orth, (S)outh, (E)ast, or (W)est? ")
        print("\n\n\n")
            
        if move.lower() == 's' and y != 4:
            y += 1
        elif move.lower() == 's' and y == 4:
            print("This movement would take you out of bounds.")
        elif move.lower() == 'n' and y != 0:
            y -= 1
        elif move.lower() == 'n' and y == 0:
            print("This movement would take you out of bounds.")
        elif move.lower() == 'w' and x != 0:
            x -= 1
        elif move.lower() == 'w' and x == 0:
            print("This movement would take you out of bounds.")
        elif move.lower() == 'e' and x != 6:
            x += 1
        elif move.lower() == 'e' and x == 6:
            print("This movement would take you out of bounds.")
        else:
            print("Invalid input.")
            encounter = 0
        if map[y][x] == 4:
            return "new_floor", x, y
        if map[y][x] == 3:
            map[y][x] = 1
            return "chest", x, y
        if map[y][x] == 5:
            return "boss", x, y
        if map[y][x] == 2:
            return "shop", x, y
        if encounter == 1:
            encounter = random.randint(2,7)
            if encounter == 7:
                return "combat", x, y
        encounter = 1
        
        
def combat(player_health, list_inventory, type):
    dam_mult = 1
    def_mult = 1
    monster_list = ["slime","skeleton","goblin"]
    monster = monster_list[random.randint(0,2)]
    guard_chance = 0
    temp_attack = 0
    temp_m_attack = 0
    health = 0
    if type == 1:
        monster = "dragon"
        attack = (15, 28)
        health = 100
    if monster == "slime":
        attack = (10,15)
        health = 55
    elif monster == "skeleton":
        attack = (20,25)
        health = 35
    elif monster == "goblin":
        attack = (13,18)
        health = 40
    
    
    while health > 0:
        os.system("clear")
        verify = 0
        guard_chance = 0
            
            #-------------Player Turn------------------
        while verify == 0:
            for line in tile_generator.draw_monster(monster):
                print(line)
            for line in tile_generator.draw_menu():
                print(line)
            print(f"\tPlayer Health: {player_health} / 100")
            for line in tile_generator.draw_health(player_health):
                print(line)
            guard_chance = 0
            print(f"A {monster.capitalize()} attacks! What will you do?")
            choice = input("").strip()
            
            if choice.lower() == "strike":
                temp_attack = random.randint(15,23) * dam_mult
                health -= temp_attack
                print(f"You attacked the {monster.capitalize()} for {temp_attack} damage!")
                verify = 1
            elif choice.lower() == "guard":
                temp_guard = random.randint(50,100)
                guard_chance = temp_guard
                print(f"You have a {guard_chance}% chance of completely blocking the next attack!")
                verify = 1
            elif choice.lower() == "inventory":
                temp = inventory(list_inventory)
                list_inventory = temp[0]
                item = temp[1]
                if item == 1:
                    if player_health + 50 > 100:
                        player_health = 100
                    else:
                        player_health += 50
                    print("The potion has healed your wounds!")
                    verify = 1
                elif item == 2:
                    dam_mult = 1.5
                    print("The potion has imbued you with strength!")
                    verify = 1
                elif item == 3:
                    def_mult = 0.65
                    print("The potion has fortified your defense!")
                    verify = 1
                elif item == 0:
                    verify = 0
                
            elif choice.lower() == "flee":
                if monster == "dragon":
                    print("You cannot flee from the dragon!")
                else: 
                    if random.randint(1,3) % 2 == 0:
                        print("You have successfully fled!")
                        time.sleep(3)
                        return("move", player_health, list_inventory)

                    else:
                        print("Unable to flee!")
                    verify = 1
            else:
                print("Invalid Input!")
                
        
        #-------------Monster Turn----------------------
        if health > 0:
            temp_m_attack = random.randint(attack[0], attack[1])
            if guard_chance > 0:
                temp_guard = random.randint(0, 100)
                if temp_guard <= guard_chance:
                    print(f"The {monster.capitalize()} attacks, but you defend yourself!")
                else:
                    print(f"The {monster.capitalize()} attacks for {temp_m_attack} damage!")
                    player_health -= temp_m_attack * def_mult
            else:
                print(f"The {monster.capitalize()} attacks for {temp_m_attack} damage!")
                player_health -= temp_m_attack
        if player_health <= 0:
            print("You have been defeated! Returning to main menu.")
            time.sleep(3)
            return ("",player_health, list_inventory)
        time.sleep(3)

    print(f"The {monster.capitalize()} has been defeated!")
    if monster != "dragon":
        coins = random.randint(0,10)
        if coins > 0:
            print(f"The monster dropped {coins} coins!")
            list_inventory["coins"][0] += coins
        time.sleep(3)
        return ("move", player_health, list_inventory)
    else:
        print("You win!")
        time.sleep(3)
        return("end", player_health, list_inventory)

def inventory(list_inventory):
    item_used = 0
    while True:
        tile_generator.draw_inventory(list_inventory)
        inp = input("Which item would you like to use? ('health', 'damage', 'defense' or 'return' to exit)")
        if inp.lower() == "return":
            return list_inventory, item_used
        elif inp == "health" and list_inventory["pot_health"][0] > 0:
            item_used = 1
            list_inventory["pot_health"][0] -= 1
            return list_inventory, item_used
        elif inp == "damage" and list_inventory["pot_damage"][0] > 0:
            list_inventory["pot_damage"][0] -= 1
            item_used = 2
            return list_inventory, item_used
        elif inp == "defense" and list_inventory["pot_defense"][0] > 0:
            item_used = 3
            list_inventory["pot_defense"][0] -= 1
            return list_inventory, item_used
        else:
            print("Invalid selection!")

def end(health, list_inventory):
    os.system("clear")
    with open("combat/end.txt") as f:
        for line in f:
            print(line.strip("\n"))
    print("You have slain the dragon and completed PyCrawler!!")
    print("Thank you for playing!")
    print("Final Stats: ")
    print(f"Final Health: {health} / 100")
    final_coins = list_inventory["coins"][0]
    print(f"Final coin amount: {final_coins}")
    inp = ""
    while inp.lower() != "quit":
        inp = input("Type 'quit' to return to title screen: ")
        if inp.lower() != "quit":
            print("Invalid Input!")
    return ""

def shop(list_inventory, floor_inventory):
    os.system("clear")
    temp = ""
    should_print = False
    floor_temp = floor_inventory.copy()
    with open("combat/shop.txt") as f:
        for line in f:
            print(line.strip("\n"))
        for i in range(10):
            print("")
            inven_temp = 0
            for h in floor_inventory:

                if inven_temp == 0:
                    temp = tile_generator.pot_health(i)
                elif inven_temp == 1:
                    temp = tile_generator.pot_damage(i)
                else:
                    temp = tile_generator.pot_defense(i)

                if h != 0:
                    print(temp, end = " ")
                else:
                    print(tile_generator.pot_empty(i), end = " ")
                inven_temp += 1
    while True:
        for k in range(len(floor_temp)-1):
            if floor_temp[k] != floor_inventory[k] and floor_inventory[k] == 0:
                should_print = True
                floor_temp = floor_inventory.copy()
        if should_print == True:
            os.system("clear")
            with open("combat/shop.txt") as f:
                for line in f:
                    print(line.strip("\n"))
                for i in range(10):
                    print("")
                    inven_temp = 0
                    for h in floor_inventory:
                    
                        if inven_temp == 0:
                            temp = tile_generator.pot_health(i)
                        elif inven_temp == 1:
                            temp = tile_generator.pot_damage(i)
                        else:
                            temp = tile_generator.pot_defense(i)
        
                        if h != 0:
                            print(temp, end = " ")
                        else:
                            print(tile_generator.pot_empty(i), end = " ")
                        inven_temp += 1
            should_print = False
        inp = ""
        inp = input("What would you like to purchase? ('health', 'damage', 'defense', 'info' to see item descriptions, or 'return' to exit): ")
        
        if inp.lower() == 'info':
            while inp != 'return':
                inp = input("Which item would you like to hear about?: ('health', 'damage', 'defense', or 'return' to go back): ")
                if inp.lower() == 'health':
                    print(f"Healing Potion: {list_inventory['pot_health'][1]}")
                elif inp.lower() == 'damage':
                    print(f"Potion of Strength: {list_inventory['pot_damage'][1]}")
                elif inp.lower() == 'defense':
                    print(f"Potion of Fortitude: {list_inventory['pot_defense'][1]}")
                elif inp.lower() == 'return':
                    inp = 'return'
                else:
                    print("Invalid input!")
                
        elif inp.lower() == 'health':
            if list_inventory["coins"][0] < 10:
                print("Not enough coins!")
            elif floor_inventory[0] == 0:
                print("Sorry, out of stock!")
            elif list_inventory["pot_health"][0] + list_inventory["pot_damage"][0] + list_inventory["pot_defense"][0] == 3:
                print("Doesn't seem like you can hold any more potions!")
            else:
                print("Sold!")
                list_inventory["pot_health"][0] += 1
                list_inventory["coins"][0] -= 10
                floor_inventory[0] -= 1

        elif inp.lower() == 'damage':
            if list_inventory["coins"][0] < 15:
                print("Not enough coins!")
            elif floor_inventory[1] == 0:
                print("Sorry, out of stock!")
            elif list_inventory["pot_health"][0] + list_inventory["pot_damage"][0] + list_inventory["pot_defense"][0] == 3:
                print("Doesn't seem like you can hold any more potions!")
            else:
                print("Sold!")
                list_inventory["pot_damage"][0] += 1
                list_inventory["coins"][0] -= 15
                floor_inventory[1] -= 1

        elif inp.lower() == 'defense':
            if list_inventory["coins"][0] < 15:
                print("Not enough coins!")
            elif floor_inventory[2] == 0:
                print("Sorry, out of stock!")
            elif list_inventory["pot_health"][0] + list_inventory["pot_damage"][0] + list_inventory["pot_defense"][0] == 3:
                print("Doesn't seem like you can hold any more potions!")
            else:
                print("Sold!")
                list_inventory["pot_defense"][0] += 1
                list_inventory["coins"][0] -= 15
                floor_inventory[2] -= 1

        elif inp.lower() == 'return':
            print("Thank you for coming!")
            time.sleep(3)
            return(list_inventory, floor_inventory)
        else:
            print("Invalid selection!")



state = ""
player_health = 100
x = 0
y = 0
floor = 1
map = gen_map(floor)
list_inventory = {"pot_health" : [1, ".."], 
                  "pot_damage" : [0, ".."], 
                  "pot_defense" : [1, ".."], 
                  "coins" : [0, ".."]}
while True:
    if state == "":
        player_health = 100
        floor_inventory = [2,2,2]
        floor = 1
        map = gen_map(0)
        list_inventory = {"pot_health" : [0, "Restores up to 50 health!"], 
                          "pot_damage" : [1, "Multiplies your total damage!"], 
                          "pot_defense" : [0, "Reduces damage taken!"], 
                          "coins" : [0, ".."]}
        player_health = 100
        x = 0
        y = 0
        state = start()

    if state == "move":
        temp = movement(x,y,map, list_inventory, floor, )
        state = temp[0]
        x = temp[1]
        y = temp[2]

    if state == "combat":
        temp = combat(player_health, list_inventory, 0)
        player_health = temp[1]
        state = temp[0]
        list_inventory = temp[2]

    if state == "shop":
        temp = shop(list_inventory, floor_inventory)
        list_inventory = temp[0]
        floor_inventory = temp[1]
        state = "move"

    if state == "new_floor":
        floor += 1
        floor_inventory = [2,2,2]
        map = gen_map(floor)
        state = "move"

    if state == "chest":
        inp = ""
        os.system("clear")
        with open("combat/treasure.txt") as f:
            for line in f:
                print(line.strip("\n"))
        gold = random.randint(15,30)
        list_inventory["coins"][0] += gold
        print(f"You got {gold} coins!")
        while inp.lower() != 'return':
            inp = input("Type 'return' to continue: ")
            if inp.lower() != 'return':
                print("Invalid input!")
        state = "move"

    if state == "boss":
        temp = combat(player_health, list_inventory, 1)
        player_health = temp[1]
        state = temp[0]
        list_inventory = temp[2]

    if state == "end":
        state = end(player_health, list_inventory)