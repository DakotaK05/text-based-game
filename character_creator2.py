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
    
    "Condemed": {"max_health": 250, "current_health": 250, "max_mana": 100, "current_mana": 100, 
                 "level": 1, "strength": 20, "dexterity": 10, "endurance": 15, "agility": 10, "intelligence": 5, 
                 "faith": 5, "luck": 10, "willpower": 3},
    
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
            current_exp=0,
            exp_requirement=100,
            **attributes,
            equipped_melee_weapon=None,
            equipped_ranged_weapon=None,
            equipped_ranged_ammo=None,
            equipped_magic_catalyst=None,
            equipped_combat_spell=None,
            equipped_prayer_catalyst=None,
            equipped_combat_prayer=None,
            equipped_healing_prayer=None,
            melee_weapon_inventory=None,
            ranged_weapon_inventory=None,
            ranged_ammo_inventory=None,
            magic_catalyst_inventory=None,
            combat_magic_inventory=None,
            prayer_catalyst_inventory=None,
            combat_prayer_inventory=None,
            healing_prayer_inventory=None,
            healing_item_inventory=None,
            combat_item_inventory=None,
        )

        give_starting_items(player)
        return player
    else:
        print("Invalid choice. Please restart the program and choose a valid class.")
        input("Press enter to restart.")
        exit()

def give_starting_items(player):
    if player.character_class == "Warrior":
        player.add_melee_weapon(it.Melee_Weapon("Greatsword", "Greatsword", 60))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Rogue":
        player.add_melee_weapon(it.Melee_Weapon("Dagger", "Dagger", 35))
        player.add_ranged_weapon(it.Ranged_Weapon("Bow", "Bow", 25))
        player.add_ranged_ammo(it.Ranged_Ammo("Basic Iron Tipped Arrow", 30, 99))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Mage":
        player.add_melee_weapon(it.Melee_Weapon("Dagger", "Dagger", 35))
        player.add_magic_catalyst(it.Magic_Catalyst("Staff", 15))
        player.add_combat_spell(it.Combat_Spell("Magic Dart", 30, 10, 15))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Samurai":
        player.add_melee_weapon(it.Melee_Weapon("Katana", "Katana", 50))
        player.add_ranged_weapon(it.Ranged_Weapon("Bow", "Bow", 25))
        player.add_ranged_ammo(it.Ranged_Ammo("Basic Iron Tipped Arrow", 30, 99))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Archer":
        player.add_ranged_weapon(it.Ranged_Weapon("Bow", "Bow", 25))
        player.add_ranged_ammo(it.Ranged_Ammo("Basic Iron Tipped Arrow", 30, 99))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Condemed":
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
        
    elif player.character_class == "Martial Artist":
        player.add_melee_weapon(it.Melee_Weapon("Bandages", "Gauntlet", 30))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
    elif player.character_class == "Paladin":
        player.add_melee_weapon(it.Melee_Weapon("Holy GreatSword", "Greatsword", 90))
        player.add_prayer_catalyst(it.Prayer_Catalyst("Cross", 15))
        player.add_healing_prayers(it.Healing_Prayers("Heal", 80, 20, 15))
        player.add_combat_prayers(it.Combat_Prayers("Lightning Shot", 60, 20, 15))
        player.add_healing_items(it.Healing_Items("Health Potion", 90, 3))
def remove_item_from_inventory(player):
    class_type = input("""
What type of item are you looking to remove?
1) Melee Weapon
2) Ranged Weapon
3) Ranged Ammo
4) Magic Catalyst
5) Magic Spell
6) Prayer Catalyst
7) Combat Prayer
8) Healing Prayer
9) Healing Items
10) Combat Items
""")
    if class_type == "1":
        item_to_look_remove = input("Which Melee Weapon are you looking to remove? ")
        player.remove_melee_weapon(item_to_look_remove)
    elif class_type == "2":
        item_to_look_remove = input("Which Ranged Weapon are you looking to remove? ")
        player.remove_ranged_weapon(item_to_look_remove)
    elif class_type == "3":
        item_to_look_remove = input("Which Ranged Ammo are you looking to remove? ")
        player.remove_ranged_ammo(item_to_look_remove)
    elif class_type == "4":
        item_to_look_remove = input("Which Magic Catalyst are you looking to remove? ")
        player.remove_magic_catalyst(item_to_look_remove)
    elif class_type == "5":
        item_to_look_remove = input("Which Magic Spell are you looking to remove? ")
        player.remove_combat_spell(item_to_look_remove)
    elif class_type == "6":
        item_to_look_remove = input("Which Prayer Catalyst are you looking to remove? ")
        player.remove_prayer_catalyst(item_to_look_remove)
    elif class_type == "7":
        item_to_look_remove = input("Which Combat Prayer are you looking to remove? ")
        player.remove_combat_prayer(item_to_look_remove)
    elif class_type == "8":
        item_to_look_remove = input("Which Healing Prayer are you looking to remove? ")
        player.remove_healing_prayer(item_to_look_remove)
    elif class_type == "9":
        item_to_look_remove = input("Which Healing Item are you looking to remove? ")
        player.remove_healing_item(item_to_look_remove)
    elif class_type == "10":
        item_to_look_remove = input("Which Combat Item are you looking to remove? ")
        player.remove_combat_item(item_to_look_remove)
    


def manage_inventory(player):
    while True:
        print("\nInventory Management:")
        print("1. View Inventory")
        print("2. Remove an Item")
        print("3. Equip Something")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            player.display_inventory()
        elif choice == "2":
            remove_item_from_inventory(player)
        elif choice == "3":
            player.equip_weapon
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")