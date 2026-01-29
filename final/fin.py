import random

gold = 100
food = 10
deaf_potion = 2

monsters = {
    'тролль': {'hp': 30, 'atk': 12, 'gold': 25, 'action': 'удар дубинкой'},
    'маг огня': {'hp': 18, 'atk': 15, 'gold': 20, 'action': 'удар жаром'},
    'маг льда': {'hp': 18, 'atk': 15, 'gold': 20, 'action': 'удар холодом'},
    'летучие мыши': {'hp': 10, 'atk': 5, 'gold': 30, 'action': 'дезориентация'},
    'разбойник': {'hp': 20, 'atk': 10, 'gold': 10, 'action': 'удар мечом'}
}

# для нага
bite_used_this_floor = False
grab_used_this_floor = False
current_floor_for_abilities = 1  # Для сброса способностей при смене этажа

def upt_inventory():
    return [f'Золото: {gold}, Еда: {food}, Ослабляющее зелье: {deaf_potion}']

inventory = upt_inventory()

pix = [10, 7]  # hp, atk
nag = [30, 14]
arach = [22, 10]

do_you1 = ['магический удар', 'укус', 'бежать']
do_you2 = ['удар мечом', 'укус', 'захват', 'уворот']
do_you3 = ['обездвижить', 'выстрел из лука', 'уворот']
you3_dop = ['иссушить']

mon = ['тролль', 'маг огня', 'маг льда', 'летучие мыши', 'разбойник']
monster = random.choice(mon)

game_started = False
while not game_started:
    print('Добро пожаловать в игру! Вас ждут увлекательное приключение '
          'в подземелье и сражения с разными тварями! Начнём?')
    print('Да или нет? (Для выхода введите "выход")')
    nach = input()

    if nach.lower() == 'выход':
        print('До свидания!')
        break

    if nach.lower() == 'да':
        print('Отлично! Давайте выберем вам расу (Учтите, что у каждой свои особенности!):')
        ras_vybran = False
        selected_ras = None

        while not ras_vybran:
            print('1 - Пикси')
            print('2 - Наг')
            print('3 - Арахна')
            print('(Для выхода введите "выход")')
            ras = input()

            if ras.lower() == 'выход':
                print('До свидания!')
                exit()

            if ras not in ['1', '2', '3']:
                print('Пожалуйста, выберите одну из предложенных рас: 1, 2 или 3')
                continue

            if ras == '1':
                print('Пикси - маленькое крылатое существо. Не путайте с феями!')
                print('Они довольно коварны и вредны. Поговаривают, что их страшно боятся Тролли, из-за')
                print('какого-то древнего проклятия.')
                print('Их рост - 0,15м, вес - 0,08кг, сила атаки - 7 (после каждой противник слабеет), а здоровье всего 10.')
                print('Но пусть вас это не огорчает раньше времени, ведь из-за их роста в них')
                print('не так легко попасть пулей, ножом или кувалдой, хотя, беспорно, после первого же попадания')
                print('шансов выжить не так много. Имеет возможность уйти с поля боя в любой момент, упустив при этом награду.')
                print('Ваш выбор окончательный? Да или нет?')
                ut = input()

                if ut.lower() == 'выход':
                    print('До свидания!')
                    exit()

                if ut.lower() == 'да':
                    print('Отлично, начинаем!')
                    ras_vybran = True
                    selected_ras = '1'
                    game_started = True
                    hp = pix[0]
                    atk = pix[1]
                elif ut.lower() == 'нет':
                    print('Давайте еще подумаем!')
                else:
                    print('Ответ не ясен. Давайте попробуем еще раз выбрать расу.')

            elif ras == '2':
                print('Наг - человек, вместо ног которого змеиный хвост. Или змея, у которой вместо головы человеческое тулово.')
                print('Длина тела - 8м , что дает возможность задушить врага, но и отнимает изворотливость.')
                print('Вес - 250кг, сила атаки - 14, здоровье - 30. Наг ядовит, после укуса у жертвы за щитанные секунды густеет кровь.')
                print('Как и обычные змеи, наги хладнокровны, из-за чего в боях с магами льда сила атаки снижается.')
                print('Ваш выбор окончательный? Да или нет?')
                ut = input()

                if ut.lower() == 'выход':
                    print('До свидания!')
                    exit()

                if ut.lower() == 'да':
                    print('Отлично, начинаем!')
                    ras_vybran = True
                    selected_ras = '2'
                    game_started = True
                    hp = nag[0]
                    atk = nag[1]
                elif ut.lower() == 'нет':
                    print('Давайте еще подумаем!')
                else:
                    print('Ответ не ясен. Давайте попробуем еще раз выбрать расу.')

            elif ras == '3':
                print('Арахна - Кентавр, но из паука. Тело огромного членистоногого, а на месте головы человеческое тулово.')
                print('Рост - 2,5м, вес - 100кг, здоровье 22, сила атаки - 10. За счет умения лазать по стенам - весьма изворотлива.')
                print('Как и обычные пауки, арахна умеет вырабатывать паутину, с помощью которой может обездвижить врагов (Но не магов огня).')
                print('После обездвиживания она их иссушает, высасывая всю кровь (Не работает на летучих мышах, у нее есть принципы)')
                print('и восстанавливает свое здровье на 5 единиц.')
                print('Ваш выбор окончательный? Да или нет?')
                ut = input()

                if ut.lower() == 'выход':
                    print('До свидания!')
                    exit()

                if ut.lower() == 'да':
                    print('Отлично, начинаем!')
                    ras_vybran = True
                    selected_ras = '3'
                    game_started = True
                    hp = arach[0]
                    atk = arach[1]
                elif ut.lower() == 'нет':
                    print('Давайте еще подумаем!')
                else:
                    print('Ответ не ясен. Давайте попробуем еще раз выбрать расу.')

        if selected_ras == '1':
            print('Вы выбрали Пикси.')
            print('HP: 10')
            print('ATK: 7')
            print('Вес: 0,08кг')
            print('Рост: 0,15м')
            print('Ловкость: 9/10')
            print('Противник попадает в вас с вероятностью 50%')
            print('Противник ТРОЛЛЬ сразу покидает бой и вы получаете награду.')
            print('После каждой вашей атаки, кроме НР противник теряет ATK.')
            print('Вы можете покинуть бой в любой момент, упустив при этом награду.')
            print('Оружие: Магия')
        elif selected_ras == '2':
            print('Вы выбрали Нага.')
            print('НР: 30')
            print('АТК: 14')
            print('Вес: 250кг')
            print('Рост: 8м')
            print('Ловкость: 3/10')
            print('Противник ЛЕТУЧИЕ МЫШИ не наносит вам урон.')
            print('У вас есть возможность задушить противника или отравить, укусив.')
            print('В бою с противником МАГ ЛЬДА вы теряете АТК.')
            print('Оружие: Меч')
        elif selected_ras == '3':
            print('Вы выбрали Арахну.')
            print('НР: 22')
            print('АТК: 10')
            print('Вес: 100кг')
            print('Рост: 2,5м')
            print('Ловкость: 7/10')
            print('У вас есть возможность обездвижить противника и иссушить его, восстановив 5 единиц НР.')
            print('Вы не можете иссушить противника ЛЕТУЧИЕ МЫШИ.')
            print('Вы не можете обездвижить противника МАГ ОГНЯ.')
            print('Оружие: Лук и стрелы')

        print('-' * 100)
        print('Вы отправляетесь в подземелье, состоящее из трёх этажей.')
        print('После прохождения пяти комнат на одном этаже, вы проходите на следующий.')
        print('С каждым этажом сложность будет увеличиваться.')
        print('На пути вам будут попадаться комнаты боя, комнаты с сундуками и комнаты отдыха, где вы сможете')
        print('прокачать свое оружие, подлечиться и, непосредственно, отдохнуть.')
        print('У вас есть инвентарь, где хранятся ваши вещи и куда будут складываться новые.')
        print('В процессе игры вы сложете туда заглядывать и использовать вещи от туда.')
        print(f'На данный момент у вас: {inventory}')
        print('-' * 100)

        floor = 1
        room_count = 0
        total_rooms_passed = 0

        while floor <= 3:
            print(f'\n{"=" * 50}')
            print(f'ЭТАЖ {floor}')
            print(f'{"=" * 50}')

            # Сброс нага после этажа
            if floor != current_floor_for_abilities:
                bite_used_this_floor = False
                grab_used_this_floor = False
                current_floor_for_abilities = floor
                print(f'Способности нага сброшены для нового этажа!')

            for room_num in range(1, 6):
                print(f'\nКомната {room_num}/5 (Всего пройдено: {total_rooms_passed})')

                room = ['Комната боя', 'Комната с сундуком', 'Комната отдыха']
                left = random.choice(room)
                right = random.choice(room)

                s = ['10 золота', '30 золота', '50 золота', '5 еда', '5 еда', 'Ослабляющее зелье', 'Крысиная тушка']
                sunduk = random.choice(s)

                print('Вы внутри, вас встречает развилка! Куда идём?(лево/право). (Для выхода введите "выход")')
                print(f'Лево - {left}, право - {right}.')
                way = input().lower()

                if way == 'выход':
                    print('До свидания!')
                    exit()

                while way not in ['лево', 'право']:
                    print('Только лево или право, будьте добры.')
                    way = input().lower()

                    if way == 'выход':
                        print('До свидания!')
                        exit()

                # Комната с сундуком
                if (way == 'лево' and left == 'Комната с сундуком') or (
                        way == 'право' and right == 'Комната с сундуком'):
                    print('Вы в маленькой комнате с маленьким сундуком.')
                    print(f'Внутри сундука: {sunduk}')

                    if sunduk == '10 золота':
                        gold += 10
                        inventory = upt_inventory()
                        print(f'Вы нашли 10 золота! Теперь у вас {gold} золота.')
                    elif sunduk == '30 золота':
                        gold += 30
                        inventory = upt_inventory()
                        print(f'Вы нашли 30 золота! Теперь у вас {gold} золота.')
                    elif sunduk == '50 золота':
                        gold += 50
                        inventory = upt_inventory()
                        print(f'Вы нашли 50 золота! Теперь у вас {gold} золота.')
                    elif sunduk == '5 еда':
                        food += 5
                        inventory = upt_inventory()
                        print(f'Вы нашли 5 еды! Теперь у вас {food} еды.')
                    elif sunduk == 'Ослабляющее зелье':
                        deaf_potion += 1
                        inventory = upt_inventory()
                        print(f'Вы нашли Ослабляющее зелье! Теперь у вас {deaf_potion} зелий.')
                    else:
                        print('Видимо, кто-то пришёл сюда раньше вас. Беда.')

                    print('Открыть инвентарь: и. Продолжить: д')
                    inv = input().lower()
                    if inv == 'и':
                        print(inventory)

                # Комната отдыха
                elif (way == 'лево' and left == 'Комната отдыха') or (way == 'право' and right == 'Комната отдыха'):
                    print('Вы в комнате отдыха.')

                    in_rest_room = True
                    while in_rest_room:
                        print('\nЧто вы хотите сделать?')
                        print('д - идти дальше')
                        print('п - прокачка оружия')
                        print('и - инвентарь')
                        print('выход - выйти из игры')

                        do = input().lower()

                        if do == 'выход':
                            print('До свидания!')
                            exit()
                        while do not in ['д', 'п', 'и']:
                            print('Только д, п или и, будьте добры.')
                            do = input().lower()

                            if do == 'выход':
                                print('До свидания!')
                                exit()
                        if do == 'и':
                            print(f'Инвентарь: {inventory}')
                            print(f'Ваше здоровье: {hp}')
                            print('Хотите восстановить здоровье, потратив 1 еда?(да/нет).')
                            foodut = input().lower()
                            while foodut not in ['да', 'нет']:
                                print('Только да или нет, будьте добры.')
                                foodut = input().lower()
                            if foodut == 'да':
                                if food <= 0:
                                    print('У вас недостаточно еды.')
                                else:
                                    food -= 1
                                    inventory = upt_inventory()
                                    if selected_ras == '1':
                                        hp = pix[0]
                                    elif selected_ras == '2':
                                        hp = nag[0]
                                    elif selected_ras == '3':
                                        hp = arach[0]
                                    print(f'Здоровье восстановлено! Теперь у вас {hp} HP.')

                        elif do == 'п':
                            print('Вы в меню прокачки. Хотите улучшить оружие?(да/нет)')
                            buf = input().lower()
                            while buf not in ['да', 'нет']:
                                print('Только да или нет, будьте добры.')
                                buf = input().lower()
                            if buf == 'да':
                                if selected_ras == '1':
                                    print('Оружие: магия. Хотите изучить древние фолианты и улучшить свои умения '
                                          'на 5 за 15 монет?(да/нет), инвентарь(и)')
                                    bufut = input().lower()
                                    while bufut not in ['да', 'нет', 'и']:
                                        print('Только да, нет или и, будьте добры.')
                                        bufut = input().lower()
                                    if bufut == 'и':
                                        print(inventory)
                                        print('Продолжить улучшение? (Да/нет)')
                                        bufut = input().lower()
                                        while bufut not in ['да', 'нет']:
                                            print('Только да или нет, будьте добры.')
                                            bufut = input().lower()
                                        if bufut == 'да':
                                            if gold >= 15:
                                                pix[1] += 5
                                                atk = pix[1]
                                                gold -= 15
                                                inventory = upt_inventory()
                                                print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                            else:
                                                print('Недостаточно золота!')
                                        elif bufut == 'нет':
                                            print('Тогда воюем дальше.')
                                    elif bufut == 'да':
                                        if gold >= 15:
                                            pix[1] += 5
                                            atk = pix[1]
                                            gold -= 15
                                            inventory = upt_inventory()
                                            print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                        else:
                                            print('Недостаточно золота!')
                                    elif bufut == 'нет':
                                        print('Тогда воюем дальше.')

                                elif selected_ras == '2':
                                    print('Оружие: меч. Хотите перековать его и увеличить свою мощь на 5 за 15 монет?(да/нет), инвентарь(и)')
                                    bufut = input().lower()
                                    while bufut not in ['да', 'нет', 'и']:
                                        print('Только да, нет или и, будьте добры.')
                                        bufut = input().lower()
                                    if bufut == 'и':
                                        print(inventory)
                                        print('Продолжить улучшение? (Да/нет)')
                                        bufut = input().lower()
                                        while bufut not in ['да', 'нет']:
                                            print('Только да или нет, будьте добры.')
                                            bufut = input().lower()
                                        if bufut == 'да':
                                            if gold >= 15:
                                                nag[1] += 5
                                                atk = nag[1]
                                                gold -= 15
                                                inventory = upt_inventory()
                                                print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                            else:
                                                print('Недостаточно золота!')
                                        elif bufut == 'нет':
                                            print('Тогда воюем дальше.')
                                    elif bufut == 'да':
                                        if gold >= 15:
                                            nag[1] += 5
                                            atk = nag[1]
                                            gold -= 15
                                            inventory = upt_inventory()
                                            print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                        else:
                                            print('Недостаточно золота!')
                                    elif bufut == 'нет':
                                        print('Тогда воюем дальше.')

                                elif selected_ras == '3':
                                    print('Оружие: Лук и стрелы. Хотите перетянуть лук и наточить стрелы,')
                                    print('дабы увеличить свою скорость поражения на 5 за 15 монет?(да/нет), инвентарь(и)')
                                    bufut = input().lower()
                                    while bufut not in ['да', 'нет', 'и']:
                                        print('Только да, нет или и, будьте добры.')
                                        bufut = input().lower()
                                    if bufut == 'и':
                                        print(inventory)
                                        print('Продолжить улучшение? (Да/нет)')
                                        bufut = input().lower()
                                        while bufut not in ['да', 'нет']:
                                            print('Только да или нет, будьте добры.')
                                            bufut = input().lower()
                                        if bufut == 'да':
                                            if gold >= 15:
                                                arach[1] += 5
                                                atk = arach[1]
                                                gold -= 15
                                                inventory = upt_inventory()
                                                print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                            else:
                                                print('Недостаточно золота!')
                                        elif bufut == 'нет':
                                            print('Тогда воюем дальше.')
                                    elif bufut == 'да':
                                        if gold >= 15:
                                            arach[1] += 5
                                            atk = arach[1]
                                            gold -= 15
                                            inventory = upt_inventory()
                                            print(f'Ваш АТК теперь {atk}, баланс: {gold}.')
                                        else:
                                            print('Недостаточно золота!')
                                    elif bufut == 'нет':
                                        print('Тогда воюем дальше.')

                        elif do == 'д':
                            print('Вы покидаете комнату отдыха.')
                            in_rest_room = False

                # Комната боя
                elif (way == 'лево' and left == 'Комната боя') or (way == 'право' and right == 'Комната боя'):
                    print('Вы вошли в комнату боя!')

                    monster_name = random.choice(['тролль', 'маг огня', 'маг льда', 'летучие мыши', 'разбойник'])
                    monster = monsters[monster_name].copy()

                    # Увел сил на этажах
                    if floor == 2:
                        monster['atk'] += 5
                        print(f'Внимание: На 2 этаже враги сильнее! ATK увеличен на 5.')
                    elif floor == 3:
                        monster['atk'] += 7
                        print(f'Внимание: На 3 этаже враги еще сильнее! ATK увеличен на 7.')

                    print(f'Вы встречаете {monster_name}, ваши действия?')

                    battle_over = False
                    reward = 0

                    # Пикси  Тролль
                    if selected_ras == '1' and monster_name == 'тролль':
                        print('Повезло, Тролль вас испугался и убежал, выронив несколько монет.')
                        reward = monster['gold']
                        gold += reward
                        inventory = upt_inventory()
                        battle_over = True
                        print(f'Ваша награда: {reward} Золота')

                    # Наг  Летучие мыши
                    elif selected_ras == '2' and monster_name == 'летучие мыши':
                        print('Летучие мыши не могут навредить нагу! Вы спокойно проходите мимо, давя особо наглых '
                            'мышей голыми руками.')
                        reward = monster['gold']
                        gold += reward
                        inventory = upt_inventory()
                        battle_over = True
                        print(f'Ваша награда: {reward} Золота')

                    # Обычный бой
                    if not battle_over:
                        print(f'Противник: {monster_name}')
                        print(f'HP противника: {monster["hp"]}, ATK: {monster["atk"]}')
                        print(f'Действие противника: {monster["action"]}')
                        print(f'Ваше здоровье: {hp}')
                        print(f'Ваша атака: {atk}')

                        monster_atk_weakened = False  # Для пикси
                        monster_disabled = False  # Для арахны (обездвижен)
                        next_turn_disabled = False  # Для арахны (пропуск хода противника)
                        can_drain = False  # Для арахны (можно иссушить)
                        nag_weak = False  # Для нага против мага льда

                        # наг лёд
                        if selected_ras == '2' and monster_name == 'маг льда':
                            nag_weak = True
                            print('Внимание: Из-за холода ваша атака снижена на 4 единицы!')
                            atk_temp = atk - 4

                        if monster_name == 'летучие мыши':
                            print('Внимание: Летучие мыши дезориентируют! Ваши атаки слабеют на половину.')

                        while monster['hp'] > 0 and hp > 0 and not battle_over:
                            print('\n' + '-' * 50)
                            print(f'Ваш ход!')

                            if selected_ras == '1':
                                print(f'Вы можете: {do_you1}')
                                print('и - открыть инвентарь')
                                action = input('Выберите действие: ').lower()

                                if action == 'и':
                                    print(f'Инвентарь: {inventory}')
                                    if deaf_potion > 0:
                                        print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                        print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                        use_potion = input().lower()
                                        if use_potion == 'да':
                                            deaf_potion -= 1
                                            monster['hp'] -= 10
                                            inventory = upt_inventory()
                                            print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                            continue
                                    else:
                                        print('У вас нет зелий для использования.')
                                    continue

                                while action not in ['магический удар', 'укус', 'бежать']:
                                    print('Пожалуйста, выберите одно из предложенных действий.')
                                    action = input('Выберите действие: ').lower()

                                    if action == 'и':
                                        print(f'Инвентарь: {inventory}')
                                        if deaf_potion > 0:
                                            print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                            print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                            use_potion = input().lower()
                                            if use_potion == 'да':
                                                deaf_potion -= 1
                                                monster['hp'] -= 10
                                                inventory = upt_inventory()
                                                print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                                continue
                                        else:
                                            print('У вас нет зелий для использования.')
                                        continue

                                if action == 'магический удар':
                                    damage = atk
                                    if monster_name == 'летучие мыши':
                                        damage = max(1, damage // 2)

                                    monster['hp'] -= damage
                                    monster['atk'] -= 5
                                    monster_atk_weakened = True

                                    print(f'Вы наносите магический удар на {damage} урона!')
                                    print(f'Противник слабеет! Теперь его ATK: {monster["atk"]}')

                                elif action == 'укус':
                                    damage = max(1, atk // 2)
                                    if monster_name == 'летучие мыши':
                                        damage = max(1, damage // 2)

                                    monster['hp'] -= damage
                                    monster['atk'] -= 5
                                    monster_atk_weakened = True

                                    print(f'Вы кусаете противника на {damage} урона!')
                                    print(f'Противник слабеет! Теперь его ATK: {monster["atk"]}')

                                elif action == 'бежать':
                                    print('Вы сбегаете с поля боя!')

                                    room = ['Комната боя', 'Комната с сундуком', 'Комната отдыха']
                                    left = random.choice(room)
                                    right = random.choice(room)
                                    print(f'Вы оказываетесь на развилке: Лево - {left}, Право - {right}')
                                    battle_over = True
                                    break

                            elif selected_ras == '2':  # Наг

                                available_actions = do_you2.copy()
                                if bite_used_this_floor:
                                    available_actions = [a for a in available_actions if a != 'укус']
                                if grab_used_this_floor:
                                    available_actions = [a for a in available_actions if a != 'захват']

                                print(f'Вы можете: {available_actions}')
                                print('и - открыть инвентарь')
                                action = input('Выберите действие: ').lower()

                                if action == 'и':
                                    print(f'Инвентарь: {inventory}')
                                    if deaf_potion > 0:
                                        print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                        print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                        use_potion = input().lower()
                                        if use_potion == 'да':
                                            deaf_potion -= 1
                                            monster['hp'] -= 10
                                            inventory = upt_inventory()
                                            print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                            continue
                                    else:
                                        print('У вас нет зелий для использования.')
                                    continue

                                while action not in available_actions:
                                    print('Пожалуйста, выберите одно из предложенных действий.')
                                    action = input('Выберите действие: ').lower()

                                    if action == 'и':
                                        print(f'Инвентарь: {inventory}')
                                        if deaf_potion > 0:
                                            print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                            print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                            use_potion = input().lower()
                                            if use_potion == 'да':
                                                deaf_potion -= 1
                                                monster['hp'] -= 10
                                                inventory = upt_inventory()
                                                print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                                continue
                                        else:
                                            print('У вас нет зелий для использования.')
                                        continue

                                current_atk = atk_temp if nag_weak else atk

                                if action == 'удар мечом':
                                    damage = current_atk
                                    if monster_name == 'летучие мыши':
                                        damage = max(1, damage // 2)

                                    monster['hp'] -= damage
                                    print(f'Вы наносите удар мечом на {damage} урона!')

                                elif action == 'укус' and not bite_used_this_floor:
                                    bite_used_this_floor = True
                                    print('Вы кусаете противника! Яд начинает действовать...')
                                    print('Противник совершит еще один ход и умрет от яда!')
                                    monster_poisoned = True

                                elif action == 'захват' and not grab_used_this_floor:
                                    grab_used_this_floor = True
                                    print('Вы захватываете противника!')
                                    print('Противник задушен и мгновенно умирает!')
                                    monster['hp'] = 0

                                elif action == 'уворот':
                                    print('Вы готовитесь уворачиваться!')

                            elif selected_ras == '3':  # Арахна

                                available_actions = do_you3.copy()
                                if monster_disabled and can_drain and monster_name != 'летучие мыши':
                                    available_actions.append('иссушить')

                                print(f'Вы можете: {available_actions}')
                                print('и - открыть инвентарь')
                                action = input('Выберите действие: ').lower()

                                if action == 'и':
                                    print(f'Инвентарь: {inventory}')
                                    if deaf_potion > 0:
                                        print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                        print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                        use_potion = input().lower()
                                        if use_potion == 'да':
                                            deaf_potion -= 1
                                            monster['hp'] -= 10
                                            inventory = upt_inventory()
                                            print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                            continue
                                    else:
                                        print('У вас нет зелий для использования.')
                                    continue

                                while action not in available_actions:
                                    print('Пожалуйста, выберите одно из предложенных действий.')
                                    action = input('Выберите действие: ').lower()

                                    if action == 'и':
                                        print(f'Инвентарь: {inventory}')
                                        if deaf_potion > 0:
                                            print(f'У вас есть {deaf_potion} Ослабляющих зелий.')
                                            print('Использовать зелье для ослабления врага на 10 HP? (да/нет)')
                                            use_potion = input().lower()
                                            if use_potion == 'да':
                                                deaf_potion -= 1
                                                monster['hp'] -= 10
                                                inventory = upt_inventory()
                                                print(f'Вы использовали зелье! У врага осталось {monster["hp"]} HP.')
                                                continue
                                        else:
                                            print('У вас нет зелий для использования.')
                                        continue

                                if action == 'выстрел из лука':
                                    damage = atk
                                    if monster_name == 'летучие мыши':
                                        damage = max(1, damage // 2)

                                    monster['hp'] -= damage
                                    print(f'Вы выпускаете стрелу на {damage} урона!')

                                elif action == 'уворот':
                                    print('Вы готовитесь уворачиваться!')

                                elif action == 'обездвижить':
                                    if monster_name == 'маг огня':
                                        print('Не удается обездвижить мага огня! Его пламя сжигает паутину.')
                                    else:
                                        monster_disabled = True
                                        next_turn_disabled = True
                                        can_drain = (monster_name != 'летучие мыши')
                                        print(f'Вы обездвижили {monster_name} паутиной!')

                                elif action == 'иссушить' and can_drain:
                                    if monster_name == 'летучие мыши':
                                        print('Не удается иссушить летучих мышей! У вас есть принципы.')
                                    else:
                                        print('Вы иссушаете противника, выпивая его кровь!')
                                        print('Вы восстанавливаете 5 HP!')
                                        monster['hp'] = 0
                                        hp = min(hp + 5, arach[0])
                                        monster_disabled = False
                                        can_drain = False

                            if monster['hp'] <= 0:
                                reward = monster['gold']
                                gold += reward
                                inventory = upt_inventory()
                                print(f'Вы победили {monster_name}!')
                                print(f'Ваша награда: {reward} Золота')
                                battle_over = True
                                break

                            if not battle_over and not next_turn_disabled:
                                print(f'\nХод противника!')
                                print(f'{monster_name} использует {monster["action"]}!')

                                # Попадание для пикси
                                if selected_ras == '1':
                                    if random.random() < 0.5:  # 50% шанс попадания
                                        damage = monster['atk']
                                        if monster_atk_weakened:
                                            damage = max(0, damage)

                                        hp -= damage
                                        print(f'{monster_name} попадает по вам на {damage} урона!')
                                        print(f'Ваше здоровье: {hp}')
                                    else:
                                        print(f'{monster_name} промахивается!')
                                else:
                                    damage = monster['atk']

                                    if selected_ras == '2' and action == 'уворот':
                                        damage = max(0, damage - 5)
                                        print('Благодаря увороту урон уменьшен на 5!')

                                    if selected_ras == '3' and action == 'уворот':
                                        damage = max(0, damage - 7)
                                        print('Благодаря увороту урон уменьшен на 7!')

                                    if monster_name == 'летучие мыши' and selected_ras == '2':
                                        damage = 0
                                        print('Летучие мыши не могут навредить нагу!')

                                    hp -= damage
                                    print(f'{monster_name} наносит {damage} урона!')
                                    print(f'Ваше здоровье: {hp}')
                                #укус
                                if selected_ras == '2' and action == 'укус' and 'monster_poisoned' in locals():
                                    print('Яд подействовал! Противник умирает.')
                                    monster['hp'] = 0
                                    reward = monster['gold']
                                    gold += reward
                                    inventory = upt_inventory()
                                    print(f'Ваша награда: {reward} Золота')
                                    battle_over = True
                                    break

                            if next_turn_disabled:
                                next_turn_disabled = False

                            if hp <= 0:
                                print(f'\n{"=" * 50}')
                                print('ВЫ УМЕРЛИ!')
                                print(f'{"=" * 50}')
                                print('Игра начинается заново...')

                                gold = 100
                                food = 10
                                deaf_potion = 2
                                inventory = upt_inventory()

                                if selected_ras == '1':
                                    hp = pix[0]
                                    atk = pix[1]
                                elif selected_ras == '2':
                                    hp = nag[0]
                                    atk = nag[1]
                                elif selected_ras == '3':
                                    hp = arach[0]
                                    atk = arach[1]

                                # Наг для этажа
                                bite_used_this_floor = False
                                grab_used_this_floor = False


                                print('Возвращаемся к началу игры...')
                                game_started = False
                                break

                    if not battle_over and hp > 0:
                        print(f'Вы покидаете комнату боя. Ваше здоровье: {hp}')

                room_count += 1
                total_rooms_passed += 1
                print(f'\nВы прошли комнату {room_num}/5 на этаже {floor}.')

            if floor < 3:
                print(f'\n{"=" * 50}')
                print(f'Поздравляем! Вы прошли этаж {floor}!')
                print(f'Переходим на этаж {floor + 1}')
                print(f'{"=" * 50}')
                floor += 1
                room_count = 0
            else:
                print(f'\n{"=" * 50}')
                print('ПОЗДРАВЛЯЕМ! ВЫ ПРОШЛИ ВСЕ ТРИ ЭТАЖА ПОДЗЕМЕЛЬЯ!')
                print('Игра завершена!')
                print(f'{"=" * 50}')
                break

        print(f'\nВаш финальный результат:')
        print(f'Золото: {gold}')
        print(f'Еда: {food}')
        print(f'Зелья: {deaf_potion}')
        print(f'Пройдено комнат: {total_rooms_passed}')
        break

    elif nach.lower() == 'нет':
        print('Тогда пока!')
        break
    else:
        print('Ответ не ясен.')








