import player as pl
import item as it



character_classes = {
    "Warrior": {"max_health": 350, "current_health": 350, "max_mana": 80, "current_mana": 80,
                "level": 1, "strength": 23, "dexterity": 10, "endurance": 20, "agility": 3, "intelligence": 0, 
                "faith": 5, "luck": 10, "willpower": 3},
    
    "Samurai": {"max_health": 200, "current_health": 200, "max_mana": 100, "current_mana": 100, 
                "level": 1, "strength": 12, "dexterity": 20, "endurance": 15, "agility": 12, "intelligence": 0, 
                "faith": 15, "luck": 13, "willpower": 3},
    
    "Rogue": {"max_health": 90, "current_health": 90, "max_mana": 100, "current_mana": 100, 
              "level": 1, "strength": 8, "dexterity": 24, "endurance": 8, "agility": 23, "intelligence": 0, 
              "faith": 0, "luck": 22, "willpower": 3},
    
    "Mage": {"max_health": 80, "current_health": 80, "max_mana": 100, "current_mana": 100, 
             "level": 1,"strength": 20, "dexterity": 10, "endurance": 15, "agility": 10, "intelligence": 5, 
             "faith": 5, "luck": 10, "willpower": 5},
    
    "Archer": {"max_health": 120, "current_health": 120, "max_mana": 120, "current_mana": 120, 
               "level": 1, "strength": 5, "dexterity": 20, "endurance": 16, "agility": 20, "intelligence": 9, 
               "faith": 8, "luck": 22, "willpower": 3},
    
    "Condemed": {"max_health": 250, "current_health": 250,  "max_mana": 100, "current_mana": 100, 
                 "level": 1, "strength": 20, "dexterity": 10, "endurance": 15, "agility": 10, "intelligence": 5, 
                 "faith": 5, "luck": 10, "willpower": 3,},
    
    "Martial Artist": {"max_health": 250, "current_health": 250, "max_mana": 150, "current_mana": 150, 
                       "level": 1, "strength": 22, "dexterity": 20, "endurance": 5, "agility": 20, "intelligence": 5, 
                       "faith": 15, "luck": 10, "willpower": 3},

    "Paladin": {"max_health": 400, "current_health": 400, "max_mana": 200, "current_mana": 200, 
                "level": 1, "strength": 20, "dexterity": 12, "endurance": 19, "agility": 8, "intelligence": 5, 
                "faith": 20, "luck": 9, "willpower": 3},
    
    "John Darksoul": {"max_health": 1, "current_health": 1, "max_mana": 0, "current_mana": 0, 
                      "level": 1, "strength": 0, "dexterity": 1, "endurance": 0, "agility": 0, "intelligence": -100, 
                      "faith": -100, "luck": -100, "willpower": 1},
}

def create_character():
    print("Welcome to the character creator.")
    name = input("Enter your character's name: ")
    print("Choose a class:")
    for idx, class_name in enumerate(character_classes.keys(), start=1):
        print(f"{idx}. {class_name}")
    class_choice = int(input("Enter the number of your choice: "))

    if 1 <= class_choice <= len(character_classes):
        character_class = list(character_classes.keys())[class_choice - 1]
        attributes = character_classes[character_class]
        
        player = pl.Character(
            name,
            character_class,
            **attributes,
            inventory=None,
            status_ailment=None
        )

        give_starting_items(player)
        player.display_stats()
        return player
    else:
        print("Invalid choice. Please restart the program and choose a valid class.")
        input("Press enter to restart.")
        exit()

def give_starting_items(player):
    if player.character_class == "Warrior":
        player.add_item(it.Melee_Weapon("GreatSword", "Greatsword", 60, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Rogue":
        player.add_item(it.Melee_Weapon("Dagger", "Dagger", 7, "Bleed", 35))
        player.add_item(it.Ranged_Weapon("Bow", "Bow", 8))
        player.add_item(it.Ranged_Ammo("Arrow", 8, 99, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Mage":
        player.add_item(it.Melee_Weapon("Dagger", "Dagger", 7, "Bleed", 35))
        player.add_item(it.Magic_Catalyst("Staff", 15))
        player.add_item(it.Combat_Spell("Magic Dart", 10, 10, 15, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Samurai":
        player.add_item(it.Melee_Weapon("Katana", "Katana", 8, "Bleed", 40))
        player.add_item(it.Ranged_Weapon("Bow", "Bow", 8))
        player.add_item(it.Ranged_Ammo("Arrow", 8, 99, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Archer":
        player.add_item(it.Ranged_Weapon("Bow", "Ranged Weapon", 10, 0, 0, 1, None, 0))
        player.add_item(it.Ranged_Ammo("Arrow", 8, 99, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Condemed":
        player.add_item(it.Melee_Weapon("Shackle", "whip", 15, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Martial Artist":
        player.add_item(it.Melee_Weapon("Bandages", "Gauntlet", 2, None, 0))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "Paladin":
        player.add_item(it.Melee_Weapon("Holy GreatSword", "Greatsword", 20, "Blessed", 35))
        player.add_item(it.Prayer_Catalyst("Cross", 15))
        player.add_item(it.Healing_Prayers("Heal", 80, 20, 15))
        player.add_item(it.Combat_Prayers("Lightning Shot", 60, 20, 15, "Shocked", 50))
        player.add_item(it.Healing_Items("Health Potion", 50, 3))
    elif player.character_class == "John Darksoul":
        print("idk")

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
