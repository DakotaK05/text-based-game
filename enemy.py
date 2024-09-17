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
    def __init__(self, name, enemy_type, max_health, current_health, strength, dexterity, agility, exp_worth, enemy_ai_level=1,
        equipped_melee_weapon=None, equipped_ranged_weapon=None, equipped_ranged_ammo=None, equipped_magic_catalyst=None, equipped_combat_spell=None, 
        equipped_prayer_catalyst=None, equipped_combat_prayer=None, equipped_healing_prayer=None, melee_weapon_inventory=None, ranged_weapon_inventory=None, ranged_ammo_inventory=None, 
        magic_catalyst_inventory=None, combat_magic_inventory=None, prayer_catalyst_inventory=None, combat_prayer_inventory=None, healing_prayer_inventory=None):
        self.name = name #Enemy name
        self.enemy_type = enemy_type
        self.max_health = max_health #Enemy's max Hp
        self.current_health = current_health #Enemy's current Hp
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.agility = agility #chance to dodge a hit
        self.exp_worth = exp_worth
        self.enemy_ai_level = enemy_ai_level
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
    def enemy_decision(self, choice):
        enemy_dictionarys = {
            "Grass": {"max_health": 1, "current_health": 1, "strength": 0, "dexterity": 0, "agility": 70, "enemy_ai_level": 1 } 
        }
        enemy_dictionary = list(enemy_dictionarys.keys())
        attributes = enemy_dictionarys[enemy_dictionary]
        enemy = list(enemy_dictionary.keys())[choice - 1]
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
    
    
    #     _______        _______      ____          ___      ______           ____        _____________
    #    / ______\      /  ___  \    |  _ \        /   |    |  __  \         / __ \      |_____   _____|
    #   | /            | /     \ |   | | \ \      / /| |    | |__| |        / /  \ \           | |
    #   | |            | |     | |   | |  \ \    / / | |    |______/       / /____\ \          | |
    #   | |            | |     | |   | |   \ \__/ /  | |    |  __  \      / /______\ \         | |
    #   | \______      | \_____/ |   | |    \____/   | |    | |__| |     / /        \ \        | |
    #    \_______/      \_______/    |_|             |_|    |______/    /_/          \_\       |_|     

    


           
           
        
        
        
