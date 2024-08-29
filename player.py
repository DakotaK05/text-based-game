import random as rr
import item as it
import character_creator2 as cc
class Character:
    def __init__(self, name, character_class, max_health, current_health, max_mana, current_mana, defense, critical_damage, skill_efficency, parry_efficency, lpis, weapon_efficency, pce, morality, crafting, alchemy, armor_class, willpower, beast_mastery, endurance, sanity, strength, stealth, dexterity, agility, faith, luck, intelligence, resistance, charisma, wisdom, magic, inventory=None, status_ailment=None):
        self.name = name #player name
        self.character_class = character_class #player character class
        self.max_health = max_health #players max Hp
        self.current_health = current_health #players current Hp
        self.max_mana = max_mana #players max MP
        self.current_mana = current_mana #players current MP
        self.defense = defense #How much damage each hit is reduced by 
        self.endurance = endurance #Chance for player to survive a fatal hit
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.agility = agility #chance to dodge a hit
        self.intelligence = intelligence #affects spell damage per point
        self.faith = faith #affects holy spell damage per point
        self.luck = luck # Chance for criticals
        self.resistance = resistance # resistance to status ailments
        self.charisma = charisma #IDK yet
        self.wisdom = wisdom # spell hit chance
        self.magic = magic #spell requirements and how many can be used at once.
        self.stealth = stealth # USELESS
        self.pce = pce #useless
        self.morality = morality #IDK
        self.sanity = sanity #IM GOING INSANE MAKING THIS CRAP
        self.willpower = willpower #revive
        self.alchemy = alchemy #allows one to make potions
        self.beast_mastery = beast_mastery #allows one to have minions
        self.crafting = crafting #pretty self explanitory
        self.armor_class = armor_class #How good their armor is
        self.weapon_efficency = weapon_efficency #weapon skill
        self.parry_efficency = parry_efficency #yep
        self.lpis = lpis #kill me
        self.critical_damage = critical_damage
        self.skill_efficency = skill_efficency
        self.inventory = inventory if inventory is not None else []
        self.status_ailment = status_ailment if status_ailment is not None else []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Character Class: {self.character_class}")
        print(f"Max Health: {self.max_health}")
        print(f"Current Health: {self.current_health}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Current Mana: {self.current_mana}")
        print(f"Defense: {self.defense}")
        print(f"Endurance: {self.endurance}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Faith: {self.faith}")
        print(f"Luck: {self.luck}")
        print(f"Resistance: {self.resistance}")
        print(f"Charisma: {self.charisma}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Magic stat level: {self.magic}")
        print(f"Stealth Level: {self.stealth}")
        print(f"PCE: {self.pce}")
        print(f"Morality level: {self.morality}")
        print(f"Sanity Level: {self.sanity}")
        print(f"Willpower: {self.willpower}")
        print(f"Alchemy Level: {self.alchemy}")
        print(f"Beast Mastery Level: {self.beast_mastery}")
        print(f"Crafting Efficency Level: {self.crafting}")
        print(f"Armor Class: {self.armor_class}")
        print(f"Weapon Efficency: {self.weapon_efficency}")
        print(f"Parry Efficency: {self.parry_efficency}")
        print(f"LPIS: {self.lpis}")
        print(f"Critical damage Multiplier: {self.critical_damage}")
        print(f"Skill efficency: {self.skill_efficency}")
        print(f"Inflicted Status ailments: {self.status_ailment}")
        print(f"Inventory: {self.inventory}")
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
                print(item)  # This will use Item's __str__ metho
    
        