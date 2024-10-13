import random

def empty(line):
    lst = [" /    \      /    \ ", 
           "/      \____/      |", 
           "\      /    \      /", 
           " \____/      \____/ ", 
           " /    \      /    \ ", 
           "/      \____/      |",
           "\      /    \      /",
           " \____/      \____/ ",
           " /    \      /    \ ",
           "/      \____/      |",
           "\______/    \______/"]
    return lst[line]

def player(line):
    lst = ["        __     _    ", 
           "       /__\_  //    ", 
           "      //____\//     ", 
           "    _| /-_-\)|/_    ", 
           "   (___\ _ //___\   ", 
           "   (  ||\_//  *  \  ",
           "    \_| \_((*   *)) ",
           "    ( |__|_\*   *// ",
           "    (o/  _  \_*_/   ",
           "    //\__|__/\      ",
           "   // |  | |  |     "]
    return lst[line]

def shop(line):
    lst = ["                    ", 
           "                    ",
           "      ______┌─────┐ ", 
           "     /     /\    $$$", 
           "    /     /--\   $$$", 
           "   /     /----\   $ ", 
           "  /     /------\    ",
           " /     /--------\   ",
           "/_____/----------\_ ",
           "                    ",
           "                    "]
    return lst[line]

def chest(line):
    lst = ["                    ", 
           "                    ", 
           "     __________     ", 
           "    /\____;;___\    ", 
           "   | /         /    ", 
           "   `. ________/     ",
           "    |\(%()*^^()^\   ",
           "    | |---------|   ",
           "    \ |    ))   |   ",
           "     \|_________|   ",
           "                    "]
    return lst[line]

def stairs(line):
    lst = ["                    ", 
           "                    ",
           "                    ", 
           "    /_________\     ", 
           "   |L_________J|    ", 
           "  |/___________\|   ", 
           "  |L___________J|   ",
           " |/_____________\|  ",
           " |L_____________J|  ",
           "_/               \_ ",
           "                    "]
    return lst[line]

def boss(line):
    lst = ["                    ", 
           "                    ",
           "       ______       ", 
           "      /      \      ", 
           "     |  () () |     ", 
           "      \   ^  /      ", 
           "       ||||||       ",
           "       ||||||       ",
           "                    ",
           "                    ",
           "                    "]
    return lst[line]

def pot_health(line):
    lst = ["        .___,       ",
           "        <   >       ",
           "         ) (        ",
           "        /`-.\       ",
           "       /     \      ",
           "      / _    _\     ",
           "     :,' `-.' `:    ",
           "     | HEALTH  |    ",
           "      \       /     ",
           "       `.___.'      "]
    return lst[line]

def pot_damage(line):
    lst = ["                    ", 
           "         __         ",
           "       _[__]_       ",
           "      /_    _\      ",
           "      )_`` '_(      ",
           "      |;:    |      ",
           "      |ATTACK|      ",
           "      |;: .._|      ",
           "      `-....-'      ",
           "                    "]
    return lst[line]

def pot_defense(line):
    lst = ["                    ",
           "        ___         ", 
           "       [___ ]       ",
           "     .-'.   '-.     ",
           "    /:;/    _.-'\   ",
           "    |:._     .--|   ",
           "    |:.DEFENSE -|   ",
           "    |:._       .|   ",
           "    |:._        |   ",
           "    `-._______.-'   "]
    return lst[line]

def pot_empty(line):
    lst = ["┌──────────────────┐", 
           "│                  │",
           "│                  │",
           "│                  │",
           "│   OUT OF STOCK   │",
           "│                  │",
           "│                  │",
           "│                  │",
           "│                  │",
           "└──────────────────┘"]
    return lst[line]

def gen_map():
    map = [[10, 1, 1, 1, 1, 1, 1], 
           [1, 1, 1, 1, 1, 1, 1], 
           [1, 1, 1, 1, 1, 1, 1], 
           [1, 1, 1, 1, 1, 1, 1], 
           [1, 1, 1, 1, 1, 1, 1]]
    shop = 0,0
    chest = 0,0
    stairs = random.randint(3,6),random.randint(2,4)
    while shop[0] == chest[0] and shop[1] == chest[1]:
        shop = random.randint(0,6), random.randint(0,4)
        chest = random.randint(0,6), random.randint(0,4)
    while (stairs[0] == shop[0] and stairs[1] == shop[1]) or (stairs[0] == chest[0] and stairs[1] == chest[1]):
        stairs = random.randint(3,6), random.randint(2,4)
    map[shop[1]][shop[0]] = map[shop[1]][shop[0]] * 2
    map[chest[1]][chest[0]] = map[chest[1]][chest[0]] * 3
    map[stairs[1]][stairs[0]] = map[stairs[1]][stairs[0]] * 4
    return map

def draw_map(map):
    for i in range(len(map)):
        for k in range(11):
            print("")
            for h in map[i]:
                if h % 10 == 0:
                    print(player(k), end=" ")
                elif h == 2:
                    print(shop(k), end=" ")
                elif h == 3:
                    print(chest(k), end=" ")
                elif h == 4:
                    print(stairs(k), end=" ")
                else:
                    print(empty(k), end=" ")

def draw_monster(type):
    lst = []
    with open(f"combat/{type}.txt") as f:
        for line in f:
            lst.append(line.strip("\n"))
    return lst

def draw_health(health):
    bar = "\t"
    lst = []
    max_health = health
    if health <= 100:
        for i in range(100):
            if health > 0:
                bar += "▓"
                health -= 1
            else:
                bar += "░"
    else:
        for i in range(max_health):
            if health > 0:
                bar += "▓"
                health -= 1
            else:
                bar += "░"
    for i in range(3):
        lst.append(bar)
    return lst

def draw_menu():
    lst = []
    with open(f"combat/menu.txt") as f:
        for line in f:
            lst.append(line.strip("\n"))
    return lst

def draw_inventory(inventory):
    compact = []
    while inventory["pot_health"][0] > 0:
        compact.append(1)
        inventory["pot_health"][0] -= 1
    while inventory["pot_damage"][0] > 0:
        compact.append(2)
        inventory["pot_damage"][0] -= 1
    while inventory["pot_defense"][0] > 0:
        compact.append(3)
        inventory["pot_defense"][0] -= 1
    while len(compact) < 3:
        compact.append(0)
    for item in compact:
        if item == 1:
            inventory["pot_health"][0] += 1
        if item == 2:
            inventory["pot_damage"][0] += 1
        if item == 3:
            inventory["pot_defense"][0] += 1
    if not (1 in compact or 2 in compact or 3 in compact):
        with open("combat/empty.txt") as f:
            for line in f:
                print(line.strip("\n"))
    else:
        for i in range(10):
            print("")
            for item in compact:
                if item == 0:
                    print("                    ", end = " ")
                if item == 1:
                    print(pot_health(i), end = " ")
                if item == 2:
                    print(pot_damage(i), end = " ")
                if item == 3:
                    print(pot_defense(i), end = " ")           