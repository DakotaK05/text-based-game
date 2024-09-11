import item as it
import random as rr
class Enemy:
    #    ______   ____________         ____       _________________     ______
    #   / _____| |_____  _____|       / _  \     |______     ______|   / _____|
    #  | |____        |  |           / /_\  \           |   |         | |____ 
    #   \____ \       |  |          /________\          |   |          \____ \ 
    #        \ \      |  |         /  /    \  \         |   |               \ \
    #        | |      |  |        /  /      \  \        |   |               | |
    #    ____/ /      |  |       /  /        \  \       |   |          ____/ /
    #   |_____/       |__|      /__/          \__\      |___|         |_____/
    def __init__(self, name, enemy_type, max_health, current_health, strength, dexterity, agility, luck, resistance, 
        equipped_melee_weapon=None, equipped_ranged_weapon=None, equipped_ranged_ammo=None, equipped_magic_catalyst=None, equipped_combat_spell=None, 
        equipped_prayer_catalyst=None, equipped_combat_prayer=None, equipped_healing_prayer=None, melee_weapon_inventory=None, ranged_weapon_inventory=None, ranged_ammo_inventory=None, 
        magic_catalyst_inventory=None, combat_magic_inventory=None, prayer_catalyst_inventory=None, combat_prayer_inventory=None, healing_prayer_inventory=None, 
        healing_item_inventory=None, combat_item_inventory=None, status_effect=None):
        self.name = name #Enemy name
        self.enemy_type = enemy_type
        self.max_health = max_health #Enemy's max Hp
        self.current_health = current_health #Enemy's current Hp
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.agility = agility #chance to dodge a hit/ increases weapon speed.
        self.luck = luck # Chance for criticals
        self.resistance = resistance #status resistance
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
        self.status_effect = status_effect if status_effect is not None else []
    def enemy_decision(self):
        enemy_dictionarys = {
            "grass": {} 
        }
        enemy_dictionary = list(enemy_dictionarys.keys())
        attributes = enemy_dictionarys[enemy_dictionary]
        enemy = Enemy(
            self.name,
            enemy_type=None,
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
            status_effect=None
        )
        return enemy
    

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
    def add_ranged_weapon(self, ranged_weapon):
        self.ranged_weapon_inventory.append(ranged_weapon)
    def add_ranged_ammo(self, ranged_ammo):
        self.ranged_ammo_inventory.append(ranged_ammo)
    def add_magic_catalyst(self, magic_catalyst):
        self.magic_catalyst_inventory.append(magic_catalyst)
    def add_combat_spell(self, combat_spell):
        self.magic_catalyst_inventory.append(combat_spell)
    def add_prayer_catalyst(self, prayer_catalyst):
        self.magic_catalyst_inventory.append(prayer_catalyst)
    def add_combat_prayers(self, combat_prayers):
        self.combat_prayer_inventory.append(combat_prayers)
    def add_healing_prayers(self, healing_prayers):
        self.healing_prayer_inventory.append(healing_prayers)
    def add_healing_items(self, healing_items):
        self.healing_item_inventory.append(healing_items)
    def add_combat_items(self, combat_items):
        self.healing_item_inventory.append(combat_items)
    def remove_magic_catalyst(self, magic_catalyst):
        self.magic_catalyst_inventory.remove(magic_catalyst)
    
#     _______        _______      ____          ___      ______           ____        _____________
#    / ______\      /  ___  \    |  _ \        /   |    |  __  \         / __ \      |_____   _____|
#   | /            | /     \ |   | | \ \      / /| |    | |__| |        / /  \ \           | |
#   | |            | |     | |   | |  \ \    / / | |    |______/       / /____\ \          | |
#   | |            | |     | |   | |   \ \__/ /  | |    |  __  \      / /______\ \         | |
#   | \______      | \_____/ |   | |    \____/   | |    | |__| |     / /        \ \        | |
#    \_______/      \_______/    |_|             |_|    |______/    /_/          \_\       |_|     

    def enemy_melee_attack(self, player, item):
        if self.equipped_melee_weapon == None:
            melee_attack_value = self.strength
            status_effect = None
            status_amount = None
            print(f"Having no melee weapon equipped, the enemy results to attacking with their bare hands.")
            player.take_melee_damage(melee_attack_value, status_effect, status_amount)
        else:
            for item in self.equipped_melee_weapon:
                weapon_attack_value = item.damage_value
                status_effect = item.status_effect
                status_amount = item.status_ammount
                break
            pre_attack_value = self.strength * 2 + weapon_attack_value 
            if self.luck >= 60:
                base_crit_chance = rr.random(1, 3)
                if base_crit_chance == 3:
                    melee_attack_value = pre_attack_value * 10
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
                else:
                    melee_attack_value = pre_attack_value
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount) 
            elif self.luck >= 50:
                base_crit_chance = rr.random(1, 5)
                if base_crit_chance == 5:
                    melee_attack_value = pre_attack_value * 10
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
                else:
                    melee_attack_value = pre_attack_value
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
            elif self.luck >= 40:
                base_crit_chance = rr.random(1, 8)
                if base_crit_chance == 8:
                    melee_attack_value = pre_attack_value * 10
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
                else:
                    melee_attack_value = pre_attack_value
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
            elif self.luck >= 30:
                base_crit_chance = rr.random(1, 10)
                if base_crit_chance == 10:
                    melee_attack_value = pre_attack_value * 10
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
                else:
                    melee_attack_value = pre_attack_value
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
            elif self.luck <= 30:
                base_crit_chance = rr.random(1, 15)
                if base_crit_chance == 15:
                    melee_attack_value = pre_attack_value * 10
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
                else:
                    melee_attack_value = pre_attack_value
                    player.take_melee_damage(melee_attack_value, status_effect, status_amount)
            

    
    def enemy_ranged_attack(self, player, item):
        if self.equipped_ranged_weapon == None and self.ranged_ammo_inventory == None:
            melee_attack_value = self.strength
            status_effect = None
            status_amount = None
            print(f"Having no melee weapon equipped, the enemy results to attacking with their bare hands.")
            player.take_melee_damage(melee_attack_value)
        elif self.equipped_ranged_weapon == None and item in self.equipped_ranged_ammo:
            print(f"Having no bow but arrows, {self.name} stabs you with it.")
            for item in self.equipped_ranged_ammo:
                arrow_damage = item.damage_value
                status_effect = item.status_effect
                status_amount = item.status_ammount
                break
            pre_attack_value = self.strength + self.dexterity + arrow_damage
            if self.luck >= 60:
                base_crit_chance = rr.random(1, 3)
                if base_crit_chance == 3:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_melee_damage(ranged_attack_value) 
            elif self.luck >= 50:
                base_crit_chance = rr.random(1, 5)
                if base_crit_chance == 5:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck >= 40:
                base_crit_chance = rr.random(1, 8)
                if base_crit_chance == 8:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck >= 30:
                base_crit_chance = rr.random(1, 10)
                if base_crit_chance == 10:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck <= 30:
                base_crit_chance = rr.random(1, 15)
                if base_crit_chance == 15:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
                player.take_ranged_damage(ranged_attack_value)
        elif item in self.equipped_ranged_weapon and item in self.equipped_ranged_ammo:
            print(f"{self.name} draws their bow and aims it at the player, shooting it at them.")
            for item in self.equipped_ranged_weapon:
                bow_value = item.damage_value
                break
            for item in self.equipped_ranged_ammo:
                arrow_damage = item.damage_value
                status_effect = item.status_effect
                status_amount = item.status_ammount
                break
            pre_attack_value = self.strength + self.dexterity + bow_value + arrow_damage
            if self.luck >= 60:
                base_crit_chance = rr.random(1, 3)
                if base_crit_chance == 3:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_melee_damage(ranged_attack_value) 
            elif self.luck >= 50:
                base_crit_chance = rr.random(1, 5)
                if base_crit_chance == 5:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck >= 40:
                base_crit_chance = rr.random(1, 8)
                if base_crit_chance == 8:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck >= 30:
                base_crit_chance = rr.random(1, 10)
                if base_crit_chance == 10:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
            elif self.luck <= 30:
                base_crit_chance = rr.random(1, 15)
                if base_crit_chance == 15:
                    ranged_attack_value = pre_attack_value * 10
                    player.take_ranged_damage(ranged_attack_value)
                else:
                    ranged_attack_value = pre_attack_value
                    player.take_ranged_damage(ranged_attack_value)
        else:
            melee_attack_value = self.strength
            status_effect = None
            status_amount = None
            print(f"Having no melee weapon equipped, the enemy results to attacking with their bare hands.")
            player.take_melee_damage(melee_attack_value)

    def enemy_magic_attack(self, player,  item):
        if self.equipped_magic_catalyst == None and self.equipped_combat_spell == None:
            melee_attack_value = self.strength
            status_effect = None
            status_amount = None
            print(f"Having no melee weapon equipped, the enemy results to attacking with their bare hands.")
            player.take_melee_damage(melee_attack_value)
        elif item in self.equipped_prayer_catalyst and self.equipped_combat_spell == None:
            print(f"Having no spells with their catalyst, {self.name} rushes at you, preparing to swing his catalyst. ")
            for item in self.equipped_magic_catalyst:
                self.remove_magic_catalyst(item)
                break
            player.take_catalyst_damage()
        elif item in self.equipped_combat_spell and item in self.equipped_magic_catalyst:
            for item in self.equipped_combat_spell:
                pass
        
        else:
            melee_attack_value = self.strength
            status_effect = None
            status_amount = None
            print(f"Having no melee weapon equipped, the enemy results to attacking with their bare hands.")
            player.take_melee_damage(melee_attack_value)






           
           
        
        
        
