list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины

number_of_people = len(list_players)
print("количество людей в списке", number_of_people)


def split(list_players):
    return list_players[::2], list_players[1::2]
first_team = list_players[::2]
second_team = list_players[1::2]

print(first_team)
print(second_team)
