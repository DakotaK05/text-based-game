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
    def __init__(self, name, character_class, max_health, current_health, max_mana, current_mana, level, willpower, 
        endurance, strength, dexterity, agility, faith, luck, intelligence, bleed_resistance, cursed_resistance, poison_resistance, melee_weapon_inventory=None, ranged_weapon_inventory=None, ranged_ammo_inventory=None, 
        magic_catalyst_inventory=None, combat_magic_inventory=None, prayer_catalyst_inventory=None, combat_prayer_inventory=None, healing_prayer_inventory=None, 
        healing_item_inventory=None, combat_item_inventory=None, status_ailment=None):
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
        self.agility = agility #chance to dodge a hit.
        self.intelligence = intelligence #affects spell damage and how many spells are usable 
        self.faith = faith #affects holy spell and how many can be used.
        self.luck = luck # Chance for criticals
        self.willpower = willpower #revive
        self.poison_resistance = poison_resistance
        self.cursed_resistance = cursed_resistance
        self.bleed_resistance = bleed_resistance
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
        self.status_ailment = status_ailment if status_ailment is not None else []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Character Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f'Equipped')
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
        print(f"Inflicted Status ailments: {self.status_ailment}")
    
    def remove_status_ailment(self, status_ailments):
        print(f'You have recovered from {status_ailments}.')
        self.status_ailment.remove(status_ailments)
    
    def add_status_ailment(self, status_ailments):
        print(f"You have been inflicted with {status_ailments}")
        self.status_ailment.remove(status_ailments)

    
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
    
    def add_ranged_ammo(self, ranged_ammo):
        self.ranged_ammo_inventory.append(ranged_ammo)
        print(f"{ranged_ammo.name} has been added to your inventory...")
    
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

    def remove_ranged_ammo(self, ranged_ammo_name):
        item_to_remove = None
        for item in self.ranged_ammo_inventory: 
            if item.name == ranged_ammo_name:
                item_to_remove = item
                break
        if item_to_remove:
            self.ranged_ammo_inventory.remove(item_to_remove)
            print(f"{item_to_remove.name} has been removed from your inventory.")
        else:
            print(f"{ranged_ammo_name} not found in your inventory.")

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
        if not self.melee_weapon_inventory and not self.ranged_weapon_inventory and not self.ranged_ammo_inventory and  not self.magic_catalyst_inventory and not self.combat_spell_inventory and not self.prayer_catalyst_inventory and not self.combat_prayer_inventory and not self.healing_prayer_inventory and not self.healing_item_inventory and not self.combat_item_inventory:
            print("Your inventory is empty.")
        else:
            if not self.melee_weapon_inventory:
                print("You dont have any melee weapons.")
            else:
                print(f"Melee Weapons")
                for item in self.melee_weapon_inventory:
                    print(item)
            if not self.ranged_weapon_inventory:
                print("You dont have any Ranged Weapons.")
            else:
                print("Ranged Weapons")
                for item in self.ranged_weapon_inventory:
                    print(item)
            if not self.ranged_ammo_inventory:
                print("You dont have any Ranged Ammo.")
            else:
                print("Ranged Ammo")
                for item in self.ranged_ammo_inventory:
                    print(item)
            if not self.magic_catalyst_inventory:
                print("You dont have any Magic Catalyst.")
            else:
                print("Magic Catalyst")
                for item in self.magic_catalyst_inventory:
                    print(item)
            if not self.combat_spell_inventory:
                print("You dont have any Magic Spells.")
            else:
                print("Magic spells")
                for item in self.combat_spell_inventory:
                    print(item)
            if not self.prayer_catalyst_inventory:
                print("You dont have any Prayer Catalysts.")
            else:
                print("Prayer catalysts")
                for item in self.prayer_catalyst_inventory:
                    print(item)
            if not self.combat_prayer_inventory:
                print("You dont have any Combat based Prayers.")
            else:
                print("Combat Prayers")
                for item in self.combat_prayer_inventory:
                    print(item)
            if not self.healing_prayer_inventory:
                print("You dont have any Healing Prayers.")
            else:
                print("Healing Prayers")
                for item in self.healing_prayer_inventory:
                    print(item)
            if not self.healing_item_inventory:
                print("You dont have any Healing Items.")
            else:
                print("Healing Items")
                for item in self.healing_item_inventory:
                    print(item)
            if not self.combat_item_inventory:
                print("You dont have any Combat Items.")
            else:
                print("Combat Items")
                for item in self.combat_item_inventory:
                    print(item)                                                            
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
            dodge_chance = rr.random(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value} damage")
                self.health -= melee_attack_value
                if status_effect == "Poison":
                    self.poison_resistance -= status_amount
                    if self.poison_resistance <= 0:
                        self.add_status_ailment(bt.Ailments("Poison", 30, 5))
                    

        elif self.agility >= 65:
            dodge_chance = rr.random(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 60:
            dodge_chance = rr.random(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 55:
            dodge_chance = rr.random(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 50:
            dodge_chance = rr.random(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 45:
            dodge_chance = rr.random(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 40:
            dodge_chance = rr.random(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 35:
            dodge_chance = rr.random(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 30:
            dodge_chance = rr.random(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 25:
            dodge_chance = rr.random(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 20:
            dodge_chance = rr.random(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 15:
            dodge_chance = rr.random(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 10:
            dodge_chance = rr.random(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        elif self.agility >= 5:
            dodge_chance = rr.random(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        else:
            dodge_chance = rr.random(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= melee_attack_value
                print(f"{enemy.name} attacks {self.name} for {melee_attack_value}")
        
    def take_ranged_damage(self, enemy, ranged_attack_value):
        ranged_attack_value -= self.endurance
        if self.agility >= 70:
            dodge_chance = rr.random(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 65:
            dodge_chance = rr.random(1,4)
            if dodge_chance == 4:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 60:
            dodge_chance = rr.random(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 55:
            dodge_chance = rr.random(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 50:
            dodge_chance = rr.random(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 45:
            dodge_chance = rr.random(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 40:
            dodge_chance = rr.random(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 35:
            dodge_chance = rr.random(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 30:
            dodge_chance = rr.random(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 25:
            dodge_chance = rr.random(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 20:
            dodge_chance = rr.random(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 15:
            dodge_chance = rr.random(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 10:
            dodge_chance = rr.random(1,14)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        elif self.agility >= 5:
            dodge_chance = rr.random(1,15)
            if dodge_chance == 15:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")
        else:
            dodge_chance = rr.random(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting')
            else:
                self.current_health -= ranged_attack_value
                print(f"{enemy.name} attacks {self.name} for {ranged_attack_value}")

    def take_catalyst_damage(self, enemy):
        tcd = 500 - self.endurance
        if self.agility >= 70:
            dodge_chance = rr.random(1,3)
            if dodge_chance == 3:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 65:
            dodge_chance = rr.random(1,4)
            if dodge_chance == 4:
                print('''You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves''')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 60:
            dodge_chance = rr.random(1,5)
            if dodge_chance == 5:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 55:
            dodge_chance = rr.random(1,6)
            if dodge_chance == 6:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 50:
            dodge_chance = rr.random(1,7)
            if dodge_chance == 7:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 45:
            dodge_chance = rr.random(1,8)
            if dodge_chance == 8:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 40:
            dodge_chance = rr.random(1,9)
            if dodge_chance == 9:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 35:
            dodge_chance = rr.random(1,10)
            if dodge_chance == 10:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 30:
            dodge_chance = rr.random(1,11)
            if dodge_chance == 11:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 25:
            dodge_chance = rr.random(1,12)
            if dodge_chance == 12:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 20:
            dodge_chance = rr.random(1,13)
            if dodge_chance == 13:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        elif self.agility >= 15:
            dodge_chance = rr.random(1,14)
            if dodge_chance == 14:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
        else:
            dodge_chance = rr.random(1,20)
            if dodge_chance == 20:
                print(f'You dodge the enemies attack, and live to continue fighting. The catalyst hits the ground where you stood. The energy inside the catalyst burst out and exploding in the enemies hand, dealing {tcd} damage to themselves')
                enemy.health -= tcd
            else:
                self.current_health -= tcd
                print(f"The catalyst hits you. The neergy inside bursts out, destroying the catalyst and dealing {tcd} damage to you and the enemy.")
            
        


