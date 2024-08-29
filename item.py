import opponent as op
import player as pl
class Item:
    def __init__(self, item_name, item_type, damage_value, healing_value, mana_cost):
        self.name = item_name
        self.item_type = item_type
        self.damage_value = damage_value
        self.healing_value = healing_value
        self.mana_cost = mana_cost
    def __str__(self):
        return f"{self.name} ({self.item_type}, Damage Value: {self.damage_value}, Healing Value: {self.healing_value}, Mana Cost: {self.mana_cost}"