money = int(input("Cумма которую планируете положить под проценты? : "))/100
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
q = list(per_cent.values())
deposit = [money*q[0], money*q[1], money*q[2], money*q[3]]
max1 =max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать", float(max1))