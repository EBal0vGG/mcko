file = open("scientist.txt", encoding="utf-8")  # отвкрываем файл с учеными
file = list(map(lambda s: s.split('#'), file.read().splitlines()[1:]))  # считываем его и разбиваем по "#"
file.sort(key=lambda s: s[2])  # сортируем по дате

with open('scientist_origin.txt', 'w', encoding="utf-8") as file_2:  # создаем файл scientist_origin.txt
    check_scientist = []  # список для проверки препаратов
    police = []  # список людей для полиции
    allopurinol = ()  # оригинальный создатель препарата Аллопуринол
    for scientist in file:  # проходимся по файлу
        preparation = scientist[1]  # название препарата
        if preparation not in check_scientist:  # если препарат создан
            if preparation == "Аллопуринол":  # если это Аллопуринол
                allopurinol = (scientist[0])  # создатель это <ФИО ученого>
            check_scientist.append(preparation)  # добавляем препарат в список созданных
            file_2.write("#".join(scientist) + '\n')  # записываем в файл_2 учёного (не мошенника)
        elif preparation == "Аллопуринол":  # если Аллопуринол уже создан
            police.append((scientist[0], scientist[2]))  # мошенник отправляется в список для полиции
# вывод даных для полиции
print("Разработчиками Аллопуринола были такие люди:")
for scientist in police:
    print(f"{scientist[0]} - {scientist[1]}")
print(f"Оригинальный рецепт принадлежит: {allopurinol}")
