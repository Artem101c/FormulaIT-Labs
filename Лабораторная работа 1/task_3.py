list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_players = len(list_players)
count_players_in_group = count_players // 2
first_group = list_players[:count_players_in_group:]
second_group = list_players[count_players_in_group::]
print(first_group)
print(second_group)
