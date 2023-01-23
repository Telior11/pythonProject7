tickets = int(input("Введите количество необходимых билетов: "))
visitors = 1

sum = 0
while visitors <= tickets != 0:
    age_for_ticket = int(input(f'Укажите для какого возраста приобретается билет № {visitors} ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 18 <= age_for_ticket < 25:
        sum += 990
        print('Стоимость билета: 990 руб.')
    elif 25 <= age_for_ticket:
        sum += 1390
        print('Стоимость билета: 1390 руб.')
    visitors += 1

if tickets > 3:
    sale = sum - ((sum / 100) * 10)
    print(f'Сумма к оплате {sale} руб., применена 10%-ая скидка за покупку более 3-x билетов')
else:
    print(f'Сумма к оплате {sum} руб.')
print("")
print("Хорошего отдыха и ждем вас снова!!!")