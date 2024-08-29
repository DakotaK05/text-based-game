import player as pl
import item as it



character_classes = {
    "Warrior": {" max health": 150, "current health": 150, "max mana": 100, "current mana": 100, 
    "defense": 30, "endurance": 15,  "strength": 20, "dexterity": 10, "agility": 10, 
    "intelligence": 5, "faith": 5, "luck": 10, "resistance": 15, "charisma": 8, "wisdom": 2,
    "magic": 3, "stealth": 0, "pce": 8, "morality": 100, "sanity": 100, "willpower": 3,
    "alchemy": 0, "beast mastery": 0, "crafting": 1, "armor class": 2, "weapon efficency": 2,
    "parry efficency": 1, "lpis": 3, "critical damage multiplier": 2, "skill efficency multiplier": 2},
    
    "Samurai": {" max health": 150, "current health": 150, "max mana": 100, "current mana": 100, 
    "defense": 25, "endurance": 20,  "strength": 20, "dexterity": 15, "agility": 15, 
    "intelligence": 5, "faith": 5, "luck": 15, "resistance": 15, "charisma": 8, "wisdom": 10,
    "magic": 3, "stealth": 20, "pce": 18, "morality": 110, "sanity": 100, "willpower": 3,
    "alchemy": 0, "beast mastery": 0, "crafting": 2, "armor class": 2, "weapon efficency": 5,
    "parry efficency": 2, "lpis": 5, "critical damage multiplier": 3, "skill efficency multiplier": 3},
    
    "Rogue": {" max health": 100, "current health": 100, "max mana": 115, "current mana": 115, 
    "defense": 10, "endurance": 15,  "strength": 10, "dexterity": 30, "agility": 20, 
    "intelligence": 5, "faith": 5, "luck": 20, "resistance": 15, "charisma": 8, "wisdom": 2,
    "magic": 3, "stealth": 0, "pce": 8, "morality": 100, "sanity": 100, "willpower": 3,
    "alchemy": 0, "beast mastery": 1, "crafting": 4, "armor class": 1, "weapon efficency": 3,
    "parry efficency": 5, "lpis": 6, "critical damage multiplier": 4, "skill efficency multiplier": 4},
    
    "Mage": {" max health": 80, "current health": 80, "max mana": 400, "current mana": 400, 
    "defense": 0, "endurance": 1,  "strength": 8, "dexterity": 4, "agility": 13, 
    "intelligence": 42, "faith": 15, "luck": 40, "resistance": 35, "charisma": -80, "wisdom": 32,
    "magic": 33, "stealth": 0, "pce": 82, "morality": 100, "sanity": 50, "willpower": 3,
    "alchemy": 3, "beast mastery": 2, "crafting": 3, "armor class": -1, "weapon efficency": 0,
    "parry efficency": 0, "lpis": 300, "critical damage multiplier": 2, "skill efficency multiplier": 2.,},
    
    "Archer": {" max health": 120, "current health": 120, "max mana": 120, "current mana": 120, 
    "defense": 5, "endurance": 15,  "strength": 8, "dexterity": 40, "agility": 15, 
    "intelligence": 5, "faith": 5, "luck": 40, "resistance": 15, "charisma": 8, "wisdom": 2,
    "magic": 3, "stealth": 0, "pce": 38, "morality": 100, "sanity": 100, "willpower": 3,
    "alchemy": 0, "beast mastery": 1, "crafting": 1, "armor class": 0, "weapon efficency": 8,
    "parry efficency": 0, "lpis": 53, "critical damage multiplier": 2, "skill efficency multiplier": 2},
    
    "Condemed": {" max health": 50, "current health": 1500, "max mana": 100, "current mana": 100, 
    "defense": 10, "endurance": 25,  "strength": 10, "dexterity": 10, "agility": 30, 
    "intelligence": 15, "faith": 15, "luck": 30, "resistance": 25, "charisma": 18, "wisdom": 12,
    "magic": 12, "stealth": 0, "pce": 10, "morality": 10, "sanity": 50, "willpower": 3,
    "alchemy": 1, "beast mastery": 0, "crafting": 1, "armor class": 1, "weapon efficency": 3,
    "parry efficency": 1, "lpis": 12, "critical damage multiplier": 2, "skill efficency multiplier": 2},
    
    "Martial Artist": {" max health": 300, "current health": 300, "max mana": 250, "current mana": 250, 
    "defense": 40, "endurance": 25,  "strength": 60, "dexterity": 30, "agility": 50, 
    "intelligence": 15, "faith": 15, "luck": 20, "resistance": 25, "charisma": 80, "wisdom": 20,
    "magic": 6, "stealth": 10, "pce": 108, "morality": 200, "sanity": 200, "willpower": 3,
    "alchemy": 0, "beast mastery": 0, "crafting": 2, "armor class": 1, "weapon efficency": 3,
    "parry efficency": 0, "lpis": 30, "critical damage multiplier": 2, "skill efficency multiplier": 3},

    "Paladin": {" max health": 425, "current health": 425, "max mana": 250, "current mana": 250, 
    "defense": 80, "endurance": 60,  "strength": 60, "dexterity": 61, "agility": 10, 
    "intelligence": 20, "faith": 500, "luck": 0, "resistance": 50, "charisma": 50, "wisdom": 50,
    "magic": 50, "stealth": 0, "pce": 999, "morality": 9999, "sanity": 1100, "willpower": 8,
    "alchemy": 3, "beast mastery": 2, "crafting": 6, "armor class": 10, "weapon efficency": 8,
    "parry efficency": 0, "lpis": 99999, "critical damage multiplier": 2, "skill efficency multiplier": 10},
    
    "John Darksoul": {" max health": 1, "current health": 1, "max mana": 0, "current mana": 0, 
    "defense": 0, "endurance": 0,  "strength": 0, "dexterity": 1, "agility": 0, 
    "intelligence": 0, "faith": 0, "luck": 0, "resistance": 0, "charisma": 0, "wisdom": 0,
    "magic": 0, "stealth": 10, "pce": 999, "morality": -9999, "sanity": -100, "willpower": 0,
    "alchemy": 0, "beast mastery": 0, "crafting": 0, "armor class": 0, "weapon efficency": 0,
    "parry efficency": 0, "lpis": 99999, "critical damage multiplier": 10000, "skill efficency multiplier": -10},
    
}



def create_character():
    print("Welcome.")
    # Get the character's name
    name = input("Enter your character's name: ")
    # Choose a class
    print("Choose a class:")
    for idx, class_name in enumerate(character_classes.keys(), start=1):
        print(f"{idx}. {class_name}")
    class_choice = int(input("Enter the number of your choice: "))

    if 1 <= class_choice <= len(character_classes):
        character_class = list(character_classes.keys())[class_choice - 1]
        attributes = character_classes[character_class]
        player = pl.Character(name, character_class, **attributes, inventory=None, status_ailment=None)
        give_starting_items(player)
        return player
    else:
        print("Invalid choice. Please restart the program and choose a valid class.")
        input("Press enter to restart.")
        exit()

def give_starting_items(player):
    if player.character_class == "Warrior":
        player.add_item(it.Item("GreatSword", "Melee Weapon", 10, 0, 0,))
        player.add_item(it.Item("Shield", "Defense Weapon", 5, 0, 0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Rogue":
        player.add_item(it.Item("Dagger", "Melee Weapon", 7, 0, 0,))
        player.add_item(it.Item("Bow", "Ranged Weapon", 8, 0, 0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Mage":
        player.add_item(it.Item("Dagger", "Melee Weapon", 7, 0, 0, ))
        player.add_item(it.Item("Staff", "Magic Catalyst", 8, 0, 0,))
        player.add_item(it.Item("Spellbook", "Magic", 10, 0, 10, "Energy"))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Samurai":
        player.add_item(it.Item("Katana", "Melee Weapon", 8, 0, 0,))
        player.add_item(it.Item("Bow", "Ranged Weapon", 4, 0, 0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Archer":
        player.add_item(it.Item("Bow", "Ranged Weapon", 10, 0, 0,))
        player.add_item(it.Item("Shield", "Defense Weapon", 5, 0, 0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Condemed":
        player.add_item(it.Item("Shield", "Defense Weapon", 5, 0, 0,))
        player.add_item(it.Item("Shackle", "Melee Weapon", 15, 0, 0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "Martial Artist":
        player.add_item(it.Item("Bandages", "Melee Weapon", 2, 0,0,))
        player.add_item(it.Item("Health Potion", "Healing Item", 0, 50, 0,))
    elif player.character_class == "John Darksoul":
        print("nuh uh")

def remove_item_from_inventory(player):
    item_name = input("Enter the name of the item you want to remove: ")
    player.remove_item(item_name)

def manage_inventory(player):
    while True:
        print("\nInventory Management:")
        print("1. View Inventory")
        print("2. Remove an Item")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            player.display_inventory()
        elif choice == "2":
            remove_item_from_inventory(player)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")