class Melee_Weapon:
    def __init__(self, item_name, item_type, damage_value):
        self.name = item_name
        self.item_type = item_type
        self.damage_value = damage_value
    def __str__(self):
        return f"{self.name} ({self.item_type}, Damage Value: {self.damage_value})"


class Ranged_Weapon:
    def __init__(self, item_name, item_type, damage_value):
        self.name = item_name
        self.item_type = item_type
        self.damage_value = damage_value
    def __str__(self):
        return f"{self.name} ({self.item_type}, Damage Value: {self.damage_value})"

class Ranged_Ammo:
    def __init__(self, item_name, damage_value, amount):
        self.name = item_name
        self.damage_value = damage_value
        self.amount = amount
    def __str__(self):
        return f"{self.name} (Damage Value: {self.damage_value}, Total amount: {self.amount}"

class Magic_Catalyst:
    def __init__(self, item_name, intelligence_requirement):
        self.name = item_name
        self.intelligence_requirement = intelligence_requirement
    def __str__(self):
        return f"{self.name}"

class Combat_Spell:
    def __init__(self, item_name, damage_value, mana_cost, intelligence_requirement):
        self.name = item_name
        self.damage_value = damage_value
        self.mana_cost = mana_cost
        self.intelligence_requirement = intelligence_requirement
    def __str__(self):
        return f"{self.name} (Damage Value: {self.damage_value}, Mana Cost: {self.mana_cost}"

class Prayer_Catalyst:
    def __init__(self, item_name, faith_requirement):
        self.name = item_name
        self.faith_requirement = faith_requirement
    def __str__(self):
        return f"{self.name}"

class Combat_Prayers:
    def __init__(self, item_name, damage_value, mana_cost, faith_requirement):
        self.name = item_name
        self.damage_value = damage_value
        self.mana_cost = mana_cost
        self.faith_requirement = faith_requirement
    def __str__(self):
        return f"{self.name} (Damage Value: {self.damage_value}, Mana Cost: {self.mana_cost}"

class Healing_Prayers:
    def __init__(self, item_name, healing_value, mana_cost, faith_requirement):
        self.name = item_name
        self.healing_value = healing_value
        self.mana_cost = mana_cost
        self.faith_requirement = faith_requirement
    def __str__(self):
        return f"{self.name} (Healing Value: {self.healing_value}, Mana Cost: {self.mana_cost}"

class Healing_Items:
    def __init__(self, item_name, healing_value, amount):
        self.name = item_name
        self.healing_value = healing_value
        self.amount = amount
    def __str__(self):
        return f"{self.name} (Total amount: {self.amount}, Healing Amount: {self.healing_value}, Amount {self.amount})"

class Combat_Items:
    def __init__(self, item_name, damage_value, amount):
        self.name = item_name
        self.damage_value = damage_value
        self.amount = amount
    def __str__(self):
        return f"{self.name} (Damage Value: {self.damage_value}, Amount {self.amount})"