#колода из 36 карт, перемешенная в случайном порядке
#при взятии карты игрок прибавляет ее номинал к своим очкам
#взятая карта удаляется из колоды
#побеждает тот игрок, который набрал 21 очко
#если никто не набрал 21, побеждает тот кто набрал ближе всего к 21
import random

def setup_deck():
    deck = [2,3,4,6,7,8,9,11]*4
    random.shuffle(deck)
    return deck 

def draw_a_card(deck):
    if len(deck) !=0:
        card = deck.pop(-1)
    else:
        card = None
    return card

def update_score(current_score, score_amount):
    current_score = current_score + score_amount #current_score += score_amount
    return current_score

def count_score(score):
    if score == 21:
        return True
    elif score > 21:
        return False
    elif score < 21:
        return None 

def draw_a_decision(text):
    if text == 'y':
        return True
    elif text =='n':
        return False
    else:
        return None

def setup_players(num_players = 1):
    list_of_players = []
    for i in range(1,num_players+1):
        player = {
        'name':f'player N{i}',
        'score': 0,
        'is_bot': False,
        'is_winner':False
        }
        list_of_players.append(player)
    print(list_of_players)
    return list_of_players 


def choose_winner(players):
    winners = []
    win_score = []
    for player in players:
        if player['is_winner'] == True: #if player['is_winner']
            return player['name']
        elif player ['score']< 21:
            win_score.append(player['score'])
            winners.append(player) 
    print(winners)
    win_score.sort()
    if winners:
        for player in players:
            if player['score'] == win_score[-1]:
                return player['name']
    else:
        return 'нет победителя'




s_deck = setup_deck()
while True:
    num_players = input('Введите кол-во игроков')
    try:
        num_players = int(num_players)
    except ValueError:
        print('Введите число, не содерэащее букв и иных символов')
        continue
    except Exception as e:
        print(e)
        continue
    else:
        if num_players>0:
            break
        else:
            print('Введите чило больше нуля')
            continue


players = setup_players(num_players)



for active_player in players:
    player_score = active_player['score']
    b_continue = True
    while b_continue:

        d_card = draw_a_card(s_deck)
        if d_card != None :
            print('вы вытянули:',d_card)
            player_score = update_score(player_score,d_card)
            print(f'У вас {player_score} очков')
            b_win = count_score(player_score)
            if b_win == None:
                pass
            elif b_win == False:
                print('вы проиграли :-(')
                break
            elif b_win == True:
                print('Вы победили')
                active_player['is_winner'] = True
                break
        else:
            print('колода закончилась!')
            break
        while True:
            decision = input('Берем еще карту?\n y/n')
            b_continue = draw_a_decision(decision)
            if b_continue == None:
                print('неверная команда')
                continue
            break
    else:
        print(f'вы закончили игру с {player_score} очков')
    active_player['score'] = player_score
print(players)
print(choose_winner(players))
print('до новых встреч')