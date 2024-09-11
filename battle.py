import enemy as ee
import random as rr
import item as it
import character_creator2 as cc
class Ailments:
    def __init__(self, ailment_name, ailment_damage, ailment_length):
        self.ailment_name = ailment_name
        self.ailment_damage = ailment_damage
        self.ailment_length = ailment_length
    def player_poison_timer(self, player):
        if "Poison" in player.status_ailment:
            starting_turn = 0
            starting_turn += turn_count
            end_turn = starting_turn + self.ailment_length
            while turn_count == end_turn:
                player.remove_status_ailment("Poison")
                break
    def player_cursed_apply(self, player):
        player.current_health = 0
    
    def player_bleeded(self, player):
        bleed_amount = player.current_health / 5
        bleed_amount *= 4
        player.current_health -= bleed_amount
    
    def enemy_poison_timer(self, enemy):
        if "Poison" in enemy.status_ailment:
            starting_turn = 0
            starting_turn += turn_count
            end_turn = starting_turn + self.ailment_length
            while turn_count == end_turn:
                enemy.remove_status_ailment("Poison")
                break
        else: 
            pass
    
    def enemy_cursed_apply(self, enemy):
        enemy.current_health = 0
    
    def enemy_bleeded(self, enemy):
        bleed_amount = enemy.current_health / 5
        bleed_amount *= 4
        enemy.current_health -= bleed_amount






    class Item_Ailments:
        def __init__(self, ailment_name, ailment_amount):
            self.ailment_name = ailment_name
            self.ailment_amount = ailment_amount

turn_count = 0     

def battle_loop(player, enemy, item,):
    turn_count = 0

    
        