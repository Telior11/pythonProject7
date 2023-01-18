money = int(input("Cумма которую планируете положить под проценты? : "))/100
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())
deposit = [money*per_cent_list[0], money*per_cent_list[1], money*per_cent_list[2], money*per_cent_list[3]]
max1 = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать", float(max1))
