import enemy as ee
import random as rr
import item as it
import character_creator2 as cc

turn_count = 0     
current_turn = None


class Combat:
    def check_for_critical():
        cc = rr.randomint(1,20)
        if cc == 20:
            crit = True
        else:
            crit = False
    
    def check_for_dodge(self):
        dodge_chance_maxmium = 50.0
        dodge_chance = self.agility
        if dodge_chance > dodge_chance_maxmium:
            dodge_chance = dodge_chance_maxmium
        dodge_determiner = rr.randint(1, 100)
        if dodge_chance >= dodge_determiner:
            dodge = True
        else:
            dodge = False
    
    def use_item(self):
        for item in self.healing_item_inventory:
            healing_value = item.healing_value
            name = item.name
            break
        self.current_health += healing_value
        item.amount -= 1
        print(f'{self.name} heals for {healing_value} health, with {name}, using one in the process, leaving {item.amount} left to use/.')
    
    def use_item(self):
        for item in self.healing_item_inventory:
                healing_value = item.healing_value
                name = item.name
                break
        self.current_health += healing_value
        item.amount -= 1
        print(f'{self.name} heals for {healing_value} health, with {name}, using one in the process, leaving {item.amount} left to use/.')
    
    def turn(self, target):
        
        

        pass

    def take_damage(self, damage_value):

        pass
    
    def attack(self, attack_type, damage_value):
        
        pass

    
    
    


        