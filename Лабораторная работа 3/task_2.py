def find_common_participants(first, second, separator=','):
    group1 = first.split(separator)
    group2 = second.split(separator)
    common_participants = list(set(group1).intersection(group2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"Общие участники:{find_common_participants(participants_first_group, participants_second_group, '|')}")
