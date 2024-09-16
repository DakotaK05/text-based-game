import enemy as ee
import random as rr
import item as it
import character_creator2 as cc
turn_count = 0     

class Combat:

    def player_turn(player, item, enemy):
        while True:
            player_turn_choice = input("""
1. Melee attack.
2. Ranged Attack.
3. Magic Attack
4. Prayer
5. Use item
""")
            if player_turn_choice == "1":
                player.player_melee_attack()
                break
            elif player_turn_choice == "2":
                player.player_ranged_attack()
                break
            elif player_turn_choice == "3":
                player.player_magic_attack()
                break
            elif player_turn_choice == "4":
                coh = print("1. Combat or 2. Healing")
                if coh == "1":
                    player.player_prayer_attack()
                    break
                elif coh == "2":
                    player.use_healing_prayer()
                    break
                else:
                    print("Invalid Input, try again")
            elif player_turn_choice == "5":
                coh = print("1. Combat or 2. Healing")
                if coh == "1":
                    player.use_combat_item()
                    break
                elif coh == "2":
                    player.use_healing_item()
                    break
                else:
                    print("Invalid Input, try again")

        

    def battle_loop(player, enemy, item,):
        turn_count = 0
        while player.current_health > 0 and enemy.current_health > 0:
            turn_count += 1
            print(turn_count)
            print("PLAYERS TURN")
            player.player_turn()
            print("ENEMYS TURN")


        