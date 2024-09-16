import random as rr
import item as it
import enemy as ee
import battle as bt
class Character:
    #    ______   ____________         ____       _________________     ______
    #   / _____| |_____  _____|       / _  \     |______     ______|   / _____|
    #  | |____        |  |           / /_\  \           |   |         | |____ 
    #   \____ \       |  |          /________\          |   |          \____ \ 
    #        \ \      |  |         /  /    \  \         |   |               \ \
    #        | |      |  |        /  /      \  \        |   |               | |
    #    ____/ /      |  |       /  /        \  \       |   |          ____/ /
    #   |_____/       |__|      /__/          \__\      |___|         |_____/
    #
    def __init__(self, name, character_class, current_exp, exp_requirement, max_health, current_health, max_mana, current_mana, level, willpower, 
        endurance, strength, dexterity, agility, faith, luck, intelligence, equipped_melee_weapon=None, equipped_ranged_weapon=None, equipped_ranged_ammo=None,
        equipped_magic_catalyst=None, equipped_combat_spell=None, equipped_prayer_catalyst=None, equipped_combat_prayer=None, equipped_healing_prayer=None, melee_weapon_inventory=None, ranged_weapon_inventory=None, ranged_ammo_inventory=None, 
        magic_catalyst_inventory=None, combat_magic_inventory=None,  prayer_catalyst_inventory=None, combat_prayer_inventory=None, healing_prayer_inventory=None, 
        healing_item_inventory=None, combat_item_inventory=None):
        self.name = name #enemy name
        self.character_class = character_class #enemy character class
        self.level = level
        self.exp = current_exp
        self.exp_requirement = exp_requirement
        self.max_health = max_health #enemys max Hp
        self.current_health = current_health #enemys current Hp
        self.max_mana = max_mana #enemys max MP
        self.current_mana = current_mana #enemys current MP
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.endurance = endurance #Chance to survive a fatal hit / Defense / resistance to status ailments
        self.agility = agility #chance to dodge a hit.
        self.intelligence = intelligence #affects spell damage and how many spells are usable 
        self.faith = faith #affects holy spell and how many can be used.
        self.luck = luck # Chance for criticals
        self.willpower = willpower #revive
        self.equipped_melee_weapon = equipped_melee_weapon if equipped_melee_weapon is not None else []
        self.equipped_ranged_weapon = equipped_ranged_weapon if equipped_ranged_weapon is not None else []
        self.equipped_ranged_ammo = equipped_ranged_ammo if equipped_ranged_ammo is not None else []
        self.equipped_magic_catalyst = equipped_magic_catalyst if equipped_magic_catalyst is not None else []
        self.equipped_combat_spell = equipped_combat_spell if equipped_combat_spell is not None else []
        self.equipped_prayer_catalyst = equipped_prayer_catalyst if equipped_prayer_catalyst is not None else []
        self.equipped_combat_prayer = equipped_combat_prayer if equipped_combat_prayer is not None else []
        self.equipped_healing_prayer = equipped_healing_prayer if equipped_healing_prayer is not None else []
        self.melee_weapon_inventory = melee_weapon_inventory if melee_weapon_inventory is not None else []
        self.ranged_weapon_inventory = ranged_weapon_inventory if ranged_weapon_inventory is not None else []
        self.ranged_ammo_inventory = ranged_ammo_inventory if ranged_ammo_inventory is not None else []
        self.magic_catalyst_inventory = magic_catalyst_inventory if magic_catalyst_inventory is not None else []
        self.combat_spell_inventory = combat_magic_inventory if combat_magic_inventory is not None else []
        self.prayer_catalyst_inventory = prayer_catalyst_inventory if prayer_catalyst_inventory is not None else []
        self.combat_prayer_inventory = combat_prayer_inventory if combat_prayer_inventory is not None else []
        self.healing_prayer_inventory = healing_prayer_inventory if healing_prayer_inventory is not None else []
        self.healing_item_inventory = healing_item_inventory if healing_item_inventory is not None else []
        self.combat_item_inventory = combat_item_inventory if combat_item_inventory is not None else []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Character Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f'Current exp: {self.exp}')
        print(f'Exp until next level: {self.exp_requirement}')
        print(f"Health {self.current_health} / {self.max_health}")
        print(f"Mana: {self.current_mana} / {self.max_mana}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Endurance: {self.endurance}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Faith: {self.faith}")
        print(f"Luck: {self.luck}")
        print(f"Willpower: {self.willpower}")
    
    def level_up(self):
        if self.exp_requirement == self.exp:
            self.level += 1
            self.exp_requirement += 200
            self.exp = 0
            self.max_health += 50
            self.current_health += 50
            self.current_mana += 50
            self.max_mana += 50
            self.strength += 2
            self.dexterity += 2
            self.endurance += 2
            self.agility += 1
            self.intelligence += 2
            self.faith += 2
            self.luck += 1
            print(f'Your level has increased, making you level {self.level}.')
            print(f'Most stats have been raised by 2.')
            if self.level == 15:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 30:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 45:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 60:
                    self.willpower += 1
                    print('Your will power has increased.')
            elif self.level == 75:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 90:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 105:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 120:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 135:
                self.willpower += 1
                print('Your will power has increased.')
            elif self.level == 150:
                self.willpower += 1
                print('Your will power has increased.')
            else: 
                pass
        else: 
            pass
    
    #  _________      ___     _    ___          ___    ________     ___     _    ____________       _______       ______      __        __                 
    # |___   ___|    |   \   | |   \  \        /  /   |  ______|   |   \   | |  |____    ____|     /  ____  \   |  ___ \     |  \      /  |
    #     | |        | |\ \  | |    \  \      /  /    | |_____     | |\ \  | |       |  |         |  /    \  |  | |___| |     \  \    /  /
    #     | |        | | \ \ | |     \  \    /  /     |  _____|    | | \ \ | |       |  |         |  |     | |  |______/       \  \__/  /
    #     | |        | |  \ \| |      \  \  /  /      | |          | |  \ \| |       |  |         |  |     | |  | | \ \         \_    _/  
    #  ___| |___     | |   \   |       \  \/  /       | |______    | |   \   |       |  |         |  \_____/ |  | |  \ \          |  |
    # |_________|    |_|    \__|        \____/        |________|   |_|    \__|       |__|          \________/   |_|   \_\         |__|
    #                                                                                                                    

    def add_melee_weapon(self, melee_weapon):
        self.melee_weapon_inventory.append(melee_weapon)
        print(f"{melee_weapon.name} has been added to your inventory...")
    
    def add_ranged_weapon(self, ranged_weapon):
        self.ranged_weapon_inventory.append(ranged_weapon)
        print(f"{ranged_weapon.name} has been added to your inventory...")
    
    def add_magic_catalyst(self, magic_catalyst):
        self.magic_catalyst_inventory.append(magic_catalyst)
        print(f"{magic_catalyst.name} has been added to your inventory...")
    
    def add_magic_catalyst(self, magic_catalyst):
        self.magic_catalyst_inventory.append(magic_catalyst)
        print(f"{magic_catalyst.name} has been added to your inventory...")
    
    def add_combat_spell(self, combat_spell):
        self.magic_catalyst_inventory.append(combat_spell)
        print(f"{combat_spell.name} has been added to your inventory...")
    
    def add_prayer_catalyst(self, prayer_catalyst):
        self.magic_catalyst_inventory.append(prayer_catalyst)
        print(f"{prayer_catalyst.name} has been added to your inventory...")
    
    def add_combat_prayers(self, combat_prayers):
        self.combat_prayer_inventory.append(combat_prayers)
        print(f"{combat_prayers.name} has been added to your inventory...")
        
    def add_healing_prayers(self, healing_prayers):
        self.healing_prayer_inventory.append(healing_prayers)
        print(f"{healing_prayers.name} has been added to your inventory...")
    
    def add_healing_items(self, healing_items):
        self.healing_item_inventory.append(healing_items)
        print(f"{healing_items.name} has been added to your inventory...")
    
    def add_combat_items(self, combat_items):
        self.healing_item_inventory.append(combat_items)
        print(f"{combat_items.name} has been added to your inventory...")

    
    
    def remove_melee_weapon(self, melee_weapon_name):
        item_to_remove = None
        for item in self.melee_weapon_inventory: 
            if item.name == melee_weapon_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.melee_weapon_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{melee_weapon_name} not found in your inventory.")

    def remove_ranged_weapon(self, ranged_weapon_name):
        item_to_remove = None
        for item in self.ranged_weapon_inventory: 
            if item.name == ranged_weapon_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.ranged_weapon_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{ranged_weapon_name} not found in your inventory.")

    def remove_magic_catalyst(self, magic_catalyst_name):
        item_to_remove = None
        for item in self.magic_catalyst_inventory: 
            if item.name == magic_catalyst_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.magic_catalyst_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{magic_catalyst_name} not found in your inventory.")

    def remove_magic_catalyst(self, magic_catalyst_name):
        item_to_remove = None
        for item in self.magic_catalyst_inventory: 
            if item.name == magic_catalyst_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.magic_catalyst_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{magic_catalyst_name} not found in your inventory.")
    
    def remove_magic_spell(self, combat_spell_name):
        item_to_remove = None
        for item in self.combat_spell_inventory: 
            if item.name == combat_spell_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.combat_spell_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{combat_spell_name} not found in your inventory.")
    
    def remove_prayer_catalyst(self, prayer_catalyst_name):
        item_to_remove = None
        for item in self.prayer_catalyst_inventory: 
            if item.name == prayer_catalyst_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.prayer_catalyst_inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{prayer_catalyst_name} not found in your inventory.")
    
    def remove_combat_prayer(self, combat_prayer_name):
        item_to_remove = None
        for item in self.combat_prayer_inventory: 
            if item.name == combat_prayer_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.combat_prayer_inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{combat_prayer_name} not found in your inventory.")
    
    def remove_healing_prayer(self, healing_prayer_name):
        item_to_remove = None
        for item in self.healing_prayer_inventory: 
            if item.name == healing_prayer_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.healing_prayer_inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{healing_prayer_name} not found in your inventory.")
    
    def remove_healing_item(self, healing_item_name):
        for item in self.healing_item_inventory: 
            if item.name == healing_item_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.healing_item_inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{healing_item_name} not found in your inventory.")
    
    def remove_combat_item(self, combat_item_name):
        for item in self.combat_item_inventory: 
            if item.name == combat_item_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.combat_item_inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your inventory.")
        else:
            print(f"{combat_item_name} not found in your inventory.")
    
    def display_inventory(self):
        print("\nInventory:")
        if not self.melee_weapon_inventory and not self.ranged_weapon_inventory and not self.magic_catalyst_inventory and  not self.magic_catalyst_inventory and not self.combat_spell_inventory and not self.prayer_catalyst_inventory and not self.combat_prayer_inventory and not self.healing_prayer_inventory and not self.healing_item_inventory and not self.combat_item_inventory:
            print("Your inventory is empty.")
        else:
            if not self.melee_weapon_inventory:
                print("You don't have any melee weapons.")
            else:
                print(f"Melee Weapons")
                for item in self.melee_weapon_inventory:
                    print(item)
            if not self.ranged_weapon_inventory:
                print("You don't have any Ranged Weapons.")
            else:
                print("Ranged Weapons")
                for item in self.ranged_weapon_inventory: 
                    print(item)
            if not self.magic_catalyst_inventory:
                print("You don't have any Magic Catalyst.")
            else:
                print("Magic Catalyst")
                for item in self.magic_catalyst_inventory:
                    print(item)
            if not self.magic_catalyst_inventory:
                print("You don't have any Magic Catalyst.")
            else:
                print("Magic Catalyst")
                for item in self.magic_catalyst_inventory:
                    print(item)
            if not self.combat_spell_inventory:
                print("You don't have any Magic Spells.")
            else:
                print("Magic spells")
                for item in self.combat_spell_inventory:
                    print(item)
            if not self.prayer_catalyst_inventory:
                print("You don't have any Prayer Catalysts.")
            else:
                print("Prayer catalysts")
                for item in self.prayer_catalyst_inventory:
                    print(item)
            if not self.combat_prayer_inventory:
                print("You don't have any Combat based Prayers.")
            else:
                print("Combat Prayers")
                for item in self.combat_prayer_inventory:
                    print(item)
            if not self.healing_prayer_inventory:
                print("You don't have any Healing Prayers.")
            else:
                print("Healing Prayers")
                for item in self.healing_prayer_inventory:
                    print(item)
            if not self.healing_item_inventory:
                print("You don't have any Healing Items.")
            else:
                print("Healing Items")
                for item in self.healing_item_inventory:
                    print(item)
            if not self.combat_item_inventory:
                print("You don't have any Combat Items.")
            else:
                print("Combat Items")
                for item in self.combat_item_inventory:
                    print(item)                           
    
    
    
    
    def equip_weapon(self):
        if not self.melee_weapon_inventory and not self.ranged_weapon_inventory and not self.magic_catalyst_inventory and  not self.magic_catalyst_inventory and not self.combat_spell_inventory and not self.prayer_catalyst_inventory and not self.combat_prayer_inventory and not self.healing_prayer_inventory:
            print("You have nothing to equip.")
        else:
            class_type = input("""
What type of item are you looking to equip?
1) Melee Weapon
2) Ranged Weapon
3) Magic Catalyst
4) Magic Catalyst
5) Magic Spell
6) Prayer Catalyst
7) Combat Prayer
8) Healing Prayer
""")
            if class_type == "1" or "Melee Weapon":
                if not self.melee_weapon_inventory:
                    print("You do not have any melee weapons to equip.")
                else:
                    for item in self.melee_weapon_inventory:
                        print(item)
                    chosen_weapon = input("Which Melee Weapon would You like to equip?")
                    if chosen_weapon == item.name in self.melee_weapon_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_melee_weapon:
                            item_to_remove = item
                            self.equipped_melee_weapon.remove(item_to_remove)
                            self.equipped_melee_weapon.append(item_to_add)
                        else:
                            self.equipped_melee_weapon.append(item_to_add)
            elif class_type == "2" or "Ranged Weapon":
                if not self.ranged_weapon_inventory:
                    print("You do not have any ranged weapons to equip.")
                else: 
                    for item in self.ranged_weapon_inventory:
                        print(item)
                    chosen_weapon = input("Which Ranged Weapon would You like to equip?")
                    if chosen_weapon == item.name in self.ranged_weapon_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_ranged_weapon:
                            item_to_remove = item
                            self.equipped_ranged_weapon.remove(item_to_remove)
                            self.equipped_ranged_weapon.append(item_to_add)
                        else: 
                            self.equipped_ranged_weapon.append(item_to_add)
            elif class_type == "3" or "Ranged Ammo":
                if not self.ranged_ammo_inventory:
                    print("You do not have any ranged ammo to equip.")
                else: 
                    for item in self.ranged_ammo_inventory:
                        print(item)
                    chosen_weapon = input("Which Ranged Ammo would You like to equip?")
                    if chosen_weapon == item.name in self.ranged_ammo_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_ranged_ammo:
                            item_to_remove = item
                            self.equipped_ranged_ammo.remove(item_to_remove)
                            self.equipped_ranged_ammo.append(item_to_add)
                        else: 
                            self.equipped_ranged_ammo.append(item_to_add)
                            
            elif class_type == "4" or "Magic Catalyst":
                if not self.magic_catalyst_inventory:
                    print("You do not have any Magic Catalyst to equip.")
                else: 
                    for item in self.magic_catalyst_inventory:
                        print(item)
                    chosen_weapon = input("Which Magic Catalyst would You like to equip?")
                    if chosen_weapon == item.name in self.magic_catalyst_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_magic_catalyst:
                            item_to_remove = item
                            self.equipped_magic_catalyst.remove(item_to_remove)
                            self.equipped_magic_catalyst.append(item_to_add)
                        else: 
                            self.equipped_magic_catalyst.append(item_to_add)
            elif class_type == "5" or "Magic Spell":
                if not self.combat_spell_inventory:
                    print("You do not have any Magic Spells to equip.")
                else: 
                    for item in self.combat_spell_inventory:
                        print(item)
                    chosen_weapon = input("Which Magic Spell would You like to equip?")
                    if chosen_weapon == item.name in self.combat_spell_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_magic_catalyst:
                            item_to_remove = item
                            self.equipped_combat_spell.remove(item_to_remove)
                            self.equipped_combat_spell.append(item_to_add)
                        else: 
                            self.equipped_combat_spell.append(item_to_add)
            elif class_type == "6" or "Prayer Catalyst":
                if not self.combat_spell_inventory:
                    print("You do not have any Prayer Catalyst to equip.")
                else: 
                    for item in self.combat_spell_inventory:
                        print(item)
                    chosen_weapon = input("Which Prayer Catalyst would You like to equip?")
                    if chosen_weapon == item.name in self.combat_spell_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_magic_catalyst:
                            item_to_remove = item
                            self.equipped_combat_spell.remove(item_to_remove)
                            self.equipped_combat_spell.append(item_to_add)
                        else: 
                            self.equipped_combat_spell.append(item_to_add)
            
            elif class_type == "7" or "Combat Prayer":
                if not self.combat_prayer_inventory:
                    print("You do not have any Combat Prayers to equip.")
                else: 
                    for item in self.combat_prayer_inventory:
                        print(item)
                    chosen_weapon = input("Which Combat Prayers would You like to equip?")
                    if chosen_weapon == item.name in self.combat_prayer_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_combat_prayer:
                            item_to_remove = item
                            self.equipped_combat_prayer.remove(item_to_remove)
                            self.equipped_combat_prayer.append(item_to_add)
                        else: 
                            self.equipped_combat_prayer.append(item_to_add)
            elif class_type == "8" or "Healing Prayer":
                if not self.healing_prayer_inventory:
                    print("You do not have any Healing Prayers to equip.")
                else: 
                    for item in self.healing_prayer_inventory:
                        print(item)
                    chosen_weapon = input("Which Healing Prayers would You like to equip?")
                    if chosen_weapon == item.name in self.healing_prayer_inventory:
                        item_to_add = chosen_weapon
                        if item in self.equipped_healing_prayer:
                            item_to_remove = item
                            self.equipped_healing_prayer.remove(item_to_remove)
                            self.equipped_healing_prayer.append(item_to_add)
                        else: 
                            self.equipped_healing_prayer.append(item_to_add)





#     _______        _______      ____          ___      ______           ____        _____________
#    / ______\      /  ___  \    |  _ \        /   |    |  __  \         / __ \      |_____   _____|
#   | /            | /     \ |   | | \ \      / /| |    | |__| |        / /  \ \           | |
#   | |            | |     | |   | |  \ \    / / | |    |______/       / /____\ \          | |
#   | |            | |     | |   | |   \ \__/ /  | |    |  __  \      / /______\ \         | |
#   | \______      | \_____/ |   | |    \____/   | |    | |__| |     / /        \ \        | |
#    \_______/      \_______/    |_|             |_|    |______/    /_/          \_\       |_|    
#
    def take_melee_damage(self, enemy, item, melee_attack_value, status_effect, status_amount): 
        melee_attack_value -= self.endurance
        if self.agility >= 70:
            dodge_chance = rr.randint(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value} damage")
                self.health -= melee_attack_value
                    

        elif self.agility >= 65:
            dodge_chance = rr.randint(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 60:
            dodge_chance = rr.randint(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 55:
            dodge_chance = rr.randint(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 50:
            dodge_chance = rr.randint(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 45:
            dodge_chance = rr.randint(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 40:
            dodge_chance = rr.randint(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 35:
            dodge_chance = rr.randint(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 30:
            dodge_chance = rr.randint(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 25:
            dodge_chance = rr.randint(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 20:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 15:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 10:
            dodge_chance = rr.randint(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 5:
            dodge_chance = rr.randint(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        else:
            dodge_chance = rr.randint(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
    def take_ranged_damage(self, enemy, ranged_attack_value):
        ranged_attack_value -= self.endurance
        if self.agility >= 70:
            dodge_chance = rr.randint(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 65:
            dodge_chance = rr.randint(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 60:
            dodge_chance = rr.randint(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 55:
            dodge_chance = rr.randint(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 50:
            dodge_chance = rr.randint(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 45:
            dodge_chance = rr.randint(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 40:
            dodge_chance = rr.randint(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 35:
            dodge_chance = rr.randint(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 30:
            dodge_chance = rr.randint(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 25:
            dodge_chance = rr.randint(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 20:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 15:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 10:
            dodge_chance = rr.randint(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 5:
            dodge_chance = rr.randint(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        else:
            dodge_chance = rr.randint(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
   
    
    def take_catalyst_damage(self, enemy):
        tcd = 500 - self.endurance
        if self.agility >= 70:
            dodge_chance = rr.randint(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 65:
            dodge_chance = rr.randint(1,4)
            if dodge_chance == 4:
                print('''You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves''')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 60:
            dodge_chance = rr.randint(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 55:
            dodge_chance = rr.randint(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 50:
            dodge_chance = rr.randint(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 45:
            dodge_chance = rr.randint(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 40:
            dodge_chance = rr.randint(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 35:
            dodge_chance = rr.randint(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 30:
            dodge_chance = rr.randint(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 25:
            dodge_chance = rr.randint(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 20:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 15:
            dodge_chance = rr.randint(1,14)
            if dodge_chance == 14:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        else:
            dodge_chance = rr.randint(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
    
    def take_magic_damage(self, magic_damage_value, enemy):
        if self.agility >= 70:
            dodge_chance = rr.randint(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 65:
            dodge_chance = rr.randint(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 60:
            dodge_chance = rr.randint(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 55:
            dodge_chance = rr.randint(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 50:
            dodge_chance = rr.randint(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 45:
            dodge_chance = rr.randint(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 40:
            dodge_chance = rr.randint(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 35:
            dodge_chance = rr.randint(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 30:
            dodge_chance = rr.randint(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 25:
            dodge_chance = rr.randint(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 20:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 15:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 10:
            dodge_chance = rr.randint(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        elif self.agility >= 5:
            dodge_chance = rr.randint(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")
        else:
            dodge_chance = rr.randint(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= magic_damage_value
                print(f"{enemy.name} attacks {self.name} for {magic_damage_value}")


    def take_prayer_damage(self, enemy, prayer_damage_value):
        if self.agility >= 70:
            dodge_chance = rr.randint(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 65:
            dodge_chance = rr.randint(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 60:
            dodge_chance = rr.randint(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 55:
            dodge_chance = rr.randint(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 50:
            dodge_chance = rr.randint(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 45:
            dodge_chance = rr.randint(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 40:
            dodge_chance = rr.randint(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 35:
            dodge_chance = rr.randint(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 30:
            dodge_chance = rr.randint(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 25:
            dodge_chance = rr.randint(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 20:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 15:
            dodge_chance = rr.randint(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 10:
            dodge_chance = rr.randint(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        elif self.agility >= 5:
            dodge_chance = rr.randint(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
        else:
            dodge_chance = rr.randint(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= prayer_damage_value
                print(f"{enemy.name} attacks {self.name} for {prayer_damage_value}")
    
    def player_melee_attack(self, enemy, item):
        if not self.equipped_melee_weapon:
            print("Not having a melee weapon equipped, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
        else:
            for item in self.equipped_melee_weapon:
                pre_attack_value = item.damage_value
                break
            if self.luck >= 70:
                dd = rr.randint(1, 3)
                if dd == 3:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            elif self.luck >= 60: 
                dd = rr.randint(1, 5)
                if dd == 5:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            elif self.luck >= 50: 
                dd = rr.randint(1, 7)
                if dd == 7:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            elif self.luck >= 40: 
                dd = rr.randint(1, 9)
                if dd == 9:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            elif self.luck >= 30: 
                dd = rr.randint(1, 11)
                if dd == 11:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            elif self.luck >= 20: 
                dd = rr.randint(1, 13)
                if dd == 13:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
            else: 
                dd = rr.randint(1, 15)
                if dd == 15:
                    print("CRITICAL")
                    melee_damage_value = pre_attack_value * 10
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
                else:
                    melee_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {melee_damage_value} damage.")
                    enemy.ee_take_melee_damage(melee_damage_value)
        
    def player_ranged_attack(self, enemy,  item):
        if not self.equipped_ranged_weapon and self.equipped_ranged_ammo:
            print("Not having a ranged weapon or ammo equipped, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
        elif not self.ranged_weapon_inventory and item in self.equipped_ranged_ammo:
            for item in self.equipped_ranged_ammo:
                pre_attack_value = item.damage_value + self.dexterity + self.strength
                item.amount -= 1
                break
            print("Not having a way to shoot your arrows as the enemy, you rush at the enemy to stab them with one of your arrows, losing one in the process.")
            if self.luck >= 70:
                dd = rr.randint(1,3)
                if dd == 3:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 60:
                dd = rr.randint(1,5)
                if dd == 5:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 50:
                dd = rr.randint(1,7)
                if dd == 7:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 40:
                dd = rr.randint(1,9)
                if dd == 9:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 30:
                dd = rr.randint(1,11)
                if dd == 11:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 20:
                dd = rr.randint(1,13)
                if dd == 13:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            else:
                dd = rr.randint(1,15)
                if dd == 15:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
        elif item in self.equipped_ranged_ammo and item in self.equipped_ranged_weapon:
            for item in self.equipped_ranged_weapon:
                damage_value = item.damage_value
                break
            for item in self.equipped_ranged_ammo:
                damage_value2 = item.damage_value
                break
            pre_attack_value = damage_value + damage_value2 + self.dexterity + self.strength
            if self.luck >= 70:
                dd = rr.randint(1,3)
                if dd == 3:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 60:
                dd = rr.randint(1,5)
                if dd == 5:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 50:
                dd = rr.randint(1,7)
                if dd == 7:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 40:
                dd = rr.randint(1,9)
                if dd == 9:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 30:
                dd = rr.randint(1,11)
                if dd == 11:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            elif self.luck >= 20:
                dd = rr.randint(1,13)
                if dd == 13:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
            else:
                dd = rr.randint(1,15)
                if dd == 15:
                    print("CRITICAL")
                    ranged_damage_value = pre_attack_value * 5
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
                else:
                    ranged_damage_value = pre_attack_value
                    print(f"You swing at {enemy.name} for {ranged_damage_value} damage.")
                    enemy.ee_take_ranged_damage(ranged_damage_value)
        else: 
            print("Not having a ranged weapon or ammo equipped, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
    
    def player_magic_attack(self, enemy, item, magic_damage_value):
        if not self.equipped_combat_spell and not self.equipped_magic_catalyst:
            print("Not having a spell or catalyst, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
        elif item in self.equipped_combat_spell and item in self.equipped_magic_catalyst:
            for item in self.equipped_magic_catalyst:
                catintreq = item.intelligence_requirement
                break
            for item in self.equipped_combat_spell:
                magic_damage_value = item.damage_value + self.intelligence
                spellintreq = item.intelligence_requirement
                spell_name = item.name
                mana_cost = item.mana_cost
                break
            if self.intelligence < spellintreq or catintreq:
                print("Not having the stats for your equipped items, you rush at the enemy with your fists before swinging.")
                melee_damage_value = self.strength
                enemy.ee_take_melee_damage(melee_damage_value)
            else:
                print(f'You shoot the spell, {spell_name}, at the enemy, costing {mana_cost} mana.')
                self.current_mana -= mana_cost
                enemy.ee_take_magic_damage(magic_damage_value)
        elif item in self.equipped_magic_catalyst and not self.equipped_combat_spell:
            print("Not having a spell, You rush to slam your catalyst agains the enemy.")
            enemy.ee_take_catalyst_damage()
        else:
            print("Missing a requirement, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
    def player_prayer_attack(self, enemy, item, prayer_damage_value):
        if not self.equipped_combat_prayer and not self.equipped_prayer_catalyst:
            print("Not having a prayer or catalyst, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
        elif item in self.equipped_prayer_catalyst and item in self.equipped_combat_prayer:
            for item in self.equipped_prayer_catalyst:
                catfaireq = item.faith_requirement
                break
            for item in self.equipped_combat_prayer:
                spelfaithreq = item.faith_requirement
                mana_cost = item.mana_cost
                prayer_damage_value = item.damage_value + self.faith
                name = item.name
                break
            if self.faith < spelfaithreq or catfaireq:
                print("Not having the stats for your equipped items, you rush at the enemy with your fists before swinging.")
                melee_damage_value = self.strength
                enemy.ee_take_melee_damage(melee_damage_value)
            else:
                print(f'You pray for, {name}, to strike your enemies, in which it does, dealing {prayer_damage_value}, which costs {mana_cost}')
                self.health -= mana_cost
                enemy.ee_take_prayer_damage(prayer_damage_value)
    def use_healing_prayer(self, item, enemy):
        if not self.equipped_healing_prayer and not self.equipped_prayer_catalyst:
            print("Not having a spell or catalyst, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
        elif item in self.equipped_healing_prayer and item in self.equipped_prayer_catalyst:
            for item in self.equipped_prayer_catalyst:
                faithcatreq = item.faith_requirement
                break
            for item in self.equipped_healing_prayer:
                healing = item.healing_value + self.faith
                prayfaitrq = item.faith_requirement
                name = item.name
            if self.faith < prayfaitrq or faithcatreq:
                print("Not having the stats for your equipped items, you rush at the enemy with your fists before swinging.")
                melee_damage_value = self.strength
                enemy.ee_take_melee_damage(melee_damage_value)
            else:
                print(f'You pray for {name}, healing you {healing} health.')
                self.current_health += healing
        else:
            print("Missing a requirement, you rush at the enemy with your fists before swinging.")
            melee_damage_value = self.strength
            enemy.ee_take_melee_damage(melee_damage_value)
    def use_healing_item(self, item):
        for item in self.healing_item_inventory:
            print(item)
        item_choice = input("Which item would you like to use?")
        if item_choice in self.healing_item_inventory:
            item.amount -= 1
            print(f'You use a single {item.name}.')
            self.current_health += item.healing_amount
            if item.amount == 0:
                self.healing_item_inventory.append(item)
                
            



            


