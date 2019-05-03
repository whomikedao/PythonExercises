def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


class hero():
    def __init__(self):
        hero_health = 10
        hero_power = 5

    def attack(enemy):
        goblin_health -= hero_power
        print("You do {} damage to the goblin.".format(hero_power))
        if goblin_health <= 0:
            print("The goblin is dead.")
    
    def alive():
        if hero_health > 0
        pass
    
    def print_status()
        print("You have {} health and {} power.".format(hero_health, hero_power))
        

class goblin():
    def __init__(self):
        goblin_health = 6
        goblin_power = 2

    def attack(hero):
        hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

    def alive():
        if goblin_health > 0
        pass

    def print_status():
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))

main()