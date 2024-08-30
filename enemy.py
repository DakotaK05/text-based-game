class Enemy:
    def __init__(self, name, max_health, current_health, max_mana, current_mana, level, endurance, strength, dexterity, agility, faith, luck, intelligence, ai_level=0, inventory=None, status_ailment=None):
        self.name = name #player name
        self.level = level
        self.max_health = max_health #players max Hp
        self.current_health = current_health #players current Hp
        self.max_mana = max_mana #players max MP
        self.current_mana = current_mana #players current MP
        self.strength = strength #How much damage melee weapons do on top of their value
        self.dexterity = dexterity #How much damage melee weapons/bows/daggers do on top of their value
        self.endurance = endurance #Chance to survive a fatal hit / Defense / resistance to status ailments
        self.agility = agility #chance to dodge a hit/ increases weapon speed.
        self.luck = luck # Chance for criticals
        self.ai_level = ai_level
        self.inventory = inventory if inventory is not None else []
        self.status_ailment = status_ailment if status_ailment is not None else []

