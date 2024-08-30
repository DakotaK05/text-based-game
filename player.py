import random as rr
import item as it
class Character:
    def __init__(self, name, character_class, max_health, current_health, max_mana, current_mana, level, willpower, endurance, strength, dexterity, agility, faith, luck, intelligence, inventory=None, status_ailment=None):
        self.name = name #player name
        self.character_class = character_class #player character class
        self.level = level
        self.max_health = max_health #players max Hp
        self.current_health = current_health #players current Hp
        self.max_mana = max_mana #players max MP
        self.current_mana = current_mana #players current MP
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.endurance = endurance #Chance to survive a fatal hit / Defense / resistance to status ailments
        self.agility = agility #chance to dodge a hit/ increases weapon speed.
        self.intelligence = intelligence #affects spell damage and how many spells are usable 
        self.faith = faith #affects holy spell and how many can be used.
        self.luck = luck # Chance for criticals
        self.willpower = willpower #revive
        self.inventory = inventory if inventory is not None else []
        self.status_ailment = status_ailment if status_ailment is not None else []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Character Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Max Health: {self.max_health}")
        print(f"Current Health: {self.current_health}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Current Mana: {self.current_mana}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Endurance: {self.endurance}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Faith: {self.faith}")
        print(f"Luck: {self.luck}")
        print(f"Willpower: {self.willpower}")
        print(f"Inflicted Status ailments: {self.status_ailment}")
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory...")
    
    def remove_item(self, item_name):
        item_to_remove = None
        for item in self.inventory:
            if item.name == item_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{item_name} not found in your inventory.")
    
    def display_inventory(self):
        print("\nInventory:")
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(item)  # This will use Item's __str__ method
    
        