# 1. Write a Python program to sum all the items in a list.

# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(sum(list1)*3)

# rezolvat


#
# 2. Write a Python program to multiply all the items in a list.
# print(list1*3)
# rezolvat

#
# 3. Write a Python program to get the largest number from a list.
# print(max(list1))
# rezolvat
# 4. Write a Python program to get the smallest number from a list.
# print(min(list1))
# rezolvat


# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# list2 = ['eu', 'tu', 'el', 'ea','eu', 'tu', 'si', 'ea']
# print(len('eu'))


#
#
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
# list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# list3 = [(1,5),(7,6),(5,8),(2,56),(9,10)]
# print(sorted(list3))   #sortarea se face dupa primul element
# list3.sort(key=lambda e:e[1])  #sortarea dupa al dilea element
# print(list3)


# 7. Write a Python program to remove duplicates from a list
# list4 = ['paine', 'oua', 'lapte','paine','oua']
# list4.remove('paine')  #sterge doar primul element denumit 'paine' dar nu stiu cum sa sterg si elementul oua in aceeasi comanda
# print(list4)


# 58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
# l1 = [1, 3, 5, 7, 9, 10]
# l2 =[2,4,6,8]
# l1[-1:]=l2
# print(l1)


# SET

# 1. Write a Python program to create a set.
# s = {'ianuarie','februarie','martie','aprilie'}
# print(type(s))

# 2. Write a Python program to iteration over sets
# s1 = {1,3,5,7}
# for n in s1:
#     print(n, end= ' ')  # nu inteleg de unde 'n' sau 'end='

# 3. Write a Python program to add member(s) in a set.
# s1.add('s')
# print(s1)

# #4. Write a Python program to remove item(s) from a given set.
# s1.remove('s')
# print(s1)


# 5. Write a Python program to remove an item from a set if it is present in the set. Go to the editor
# if 5 in s1:
#     s1.remove(5)
#     print(s1)
# else:
#     print('nu exista in lista')


# 6. Write a Python program to create an intersection of sets
# s2 = {1,2,3,4,5,6,7,8}
# print(s1.intersection(s2))

# optionale

# 1. An online shop sells pet food and accessories. Customers can choose goods and conclude
# their orders on its website. The order is processed according to these rules:
#
#     · A customer enters his order and clicks SUBMIT. Depending in its total value the order is set to either of the
#     following states:
#     - APPROVED, if the value is less than or equal to $100
#     - PENDING if the value is greater then $100 and the shop's personnel have to verify the validity of the online payment
#     · For PENDING orders, shop personnel can click one of the following:
#     - APPROVE if the payment is confirmed, thereby setting the order to the state of APPROVED
#     - CANCEL if the payment is invalid, thereby setting the order to the state of CANCELED
#
# For orders in an APPROVED state, the shop personnel choose the SHIP action after the goods are actually sent,
# thereby setting the order to a state of SHIPPED
# produse = {'crochetePeste':25,'crochetePui':15,'crocheteFicat':18,'conservaPeste':5,'conservaPui':5,'batonCarne':5}
# comanda = produse['crochetePeste']+produse['crochetePui']+produse['conservaPeste']+produse['crochetePeste']
# print(f'valoarea comenzii este de {comanda} dolari')
# plata = int(input('scrie valoarea platii pe care vrei sa o faci!'))
# if comanda  <= 100:
#     print('Aprobat')
# else:
#     print('in asteptare')
#     if plata == comanda:
#      print('Comanda trimisa')
#     else:
#         print('Anulata')

# varianta 2
# produse = {'crochetePeste':25,'crochetePui':15,'crocheteFicat':18,'conservaPeste':5,'conservaPui':5,'batonCarne':5}
# comanda = input('Alege ce vrei sa comanzi')
# valoare_comanda =input(comanda)
# print (valoare_comanda)
# print(f'valoarea comenzii este de {valoare_comanda} dolari')
# plata = int(input('cat vrei sa platesti?'))
# if valoare_comanda  <= 100:
#     print('Aprobat')
# else:
#     print('in asteptare')
#
# if plata >= valoare_comanda:
#     print('trimisa')
#     comanda = 'trimisa'
# else:
#     print('Anulata')


# 2. Company X sells merchandise to wholesale and retail outlets.Wholesale customers receive a two percent discount
# on all orders. The company also encourages both wholesale and retail customers to pay cash on delivery by offering
# a two percent discount for this method of payment. Another two percent discount is given on orders of 50 or more units
# Each column represents a certain type of order.
#
#####
# client1 = input('wholesale: da/nu')
# order_units = int(input('Introdu nr. de produse pe care le cumperi:'))
# pay_metod = input('cash:da/nu')
# total_payments = order_units*5
# if client1 == 'da':
#     if order_units >= 50:
#         if pay_metod == 'da':
#             total_payments =total_payments-(total_payments *6/100)
#             print(f'Total Payment amount with 6% discount is: {total_payments}')
#         else:
#             total_payments = total_payments-(total_payments*4/100)
#             print(f'Total Payment amount with 4% discount is: {total_payments}')
#     if order_units< 50:
#         if pay_metod == 'da':
#             total_payments = total_payments - (total_payments*4/100)
#             print(f'Total payment amount with 4% dscount is {total_payments}')
#         else:
#             total_payments = total_payments - (total_payments * 2 / 100)
#             print(f'Total Payment amount with 2% discount is: {total_payments}')
# elif client1 == "nu":
#      if order_units >= 50:
#          if pay_metod == 'da':
#             total_payments = total_payments - (total_payments*4/100)
#             print(f'Total payment amount with 4% discount is:{total_payments}')
#          else:
#              print(f'Total payment amount with 2% discount is:{total_payments}')
#      if order_units < 50:
#         if pay_metod == 'da':
#             total_payments = total_payments - (total_payments * 2/100)
#             print(f'Total payment amount with 2% discount is:{total_payments}')
#         else:
#             print(f'Total payment mount is: {total_payments}')


# 3. If a client has over 65 years, then it will be offered to him a discount of 15%.
# Otherwise if the customer does not have over 65 years, if the person travels with at least one account they will have a discount of 10%
# For both seniors and non seniors it will be applied an additional discount of 10% if they will travel during winter.
# Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel in
# the first class (in any season) or 1% handling fee otherwise.

# client1 = int(input('varsta'))
# client2 = input('calatoreste singur: da/nu')
# price_for_travel = 100
# travel_winter = input('winter: da/nu')
# first_class = input('first class: da/nu')
# if client1 > 65:
#     price_for_travel = price_for_travel - (price_for_travel*15/100)
#     print(f'Price with discount for age more then 65 years is: {price_for_travel}') # am trecut print pt verificare
#     if travel_winter == 'da':
#         price_for_travel = price_for_travel-(price_for_travel*10/100)
#         print(f'price with discount of age and winter is:{price_for_travel}')   # am trecut print pt verificare
#     if first_class == 'da':
#         price_for_travel = price_for_travel + (price_for_travel*3/100)
#         print(f'price with discount  and tax is:{price_for_travel}')
#     else:
#         price_for_travel = price_for_travel +(price_for_travel*1/100)
#         print(f'price with 1% tax is:{price_for_travel}')
# else:
#     if client2 == 'nu':
#         price_for_travel = price_for_travel- (price_for_travel*10/100)
#         print(f'price with discount for age less then 65 years an travel with least 1 account is:{price_for_travel}')   # am trecut print pt verificare
#     else:
#         print(f'price is {price_for_travel}')      # am trecut print pt verificare
#     if travel_winter == 'da':
#         price_for_travel = price_for_travel-(price_for_travel*10/100)
#         print(f'price with discount of winter is:{price_for_travel}')    # am trecut print pt verificare
#     if first_class == 'da':
#         price_for_travel = price_for_travel + (price_for_travel*3/100)
#         print(f'price with discount is:{price_for_travel}')
#     else:
#         price_for_travel = price_for_travel +(price_for_travel*1/100)
#         print(f'price with 1% discoun is:{price_for_travel}')         # am trecut print pt verificare
# rezolvat

# 1. Write the code for defining a riddle in which the person has to guess a number that is set as correct.
# The person has three tries to guess the animal, and if they haven't guessed the third time a message will be ' \
#         'returned to them: you lost the game, please try again.
# Between tries they will receive the following message: The number is wrong, you have <number_left> of tries left
# If the person guesses the number they will receive a message: Contrats, you got it right!
# The program will also receive as input if the player wants to play (yes/no)

# quess_number = 11
# play = input('wants to play: yes/no')
# total_tries = 3
# number_left = total_tries
#
# if play == 'yes':
#  print("let's play")
#  chossen_number = int(input(' choose a number'))
#  if quess_number == chossen_number:
#      print('Contrast, you got it right')
#  else:
#      number_left = total_tries - 1
#      print(f'The number is wrong, you have {number_left} of tries left')
#      chossen_number = int(input(' choose a number'))
#      if quess_number == chossen_number:
#          print('Contrast, you got it right')
#      else:
#       number_left = number_left-1
#       print(f' The number is wrong, you have {number_left} of tries left')
#       chossen_number = int(input('chose a number'))
#       if quess_number == chossen_number:
#          print('Contrast, you got it right')
#       else:
#          print('You lost the game, please try again!')
# else:
#     print(" You don't want to play?")


# rezolvat


# 2. We have a movie cinema that runs movies every day. We can have information about the movie name and movie date, movie hour,
# the room where it takes place, the price of the ticket and the available seats in each room.
#
# The room information will be stored in a dictionary, that will be made of a bunch of other dictionaries containing each room,
# and each room will have multiple key:value pairs containing information about chairs and wether they are active or not
# The available seats will be generated with the range function and assigned with numbers from 1 to 50 (assuming we have 50 seats in each room).
#
# The movies will be stored in a dictionary which will made of a bunch of other dictionaries representing each movie and
# containing multiple key:value pairs representing the date and the hour when the movie will run.
#
# We will also have a dictionary containing movies and rooms which will have inside multiple key:value pairs representing
# as keys the movies and as values the rooms in which they are running.
# We need to write a program that will take as input from the user the name of the movie they want to watch, the date and hour they prefer.
# The program will allocate for each reservation a seat in the room that the movie is running by marking that specific seat as occupied.
# The program will return a message on the screen: Your reservation was confirmed. We will be waiting you on <movie_date> at <movie_hour>.
# The movie will run in room <room_name> and your seat has the number <seat_number>

#Varianta 1 de dict

# cinema = {'movie1': {'room1': {'ora': 10, 'pret': 20, 'locuri': 50}, 'movie1': {'ora': 12, 'pret': 22, 'locuri': 50},
#                      'movie1': {'ora': 14, 'pret': 24, 'locuri': 50}, 'movie1': {'ora': 16, 'pret': 26, 'locuri': 50}},
#           'movie2': {'room2': {'ora': 10, 'pret': 20, 'locuri': 50}, 'movie2': {'ora': 12, 'pret': 22, 'locuri': 50},
#                      'movie2': {'ora': 14, 'pret': 24, 'locuri': 50}, 'movie2': {'ora': 16, 'pret': 26, 'locuri': 50}},
#           'movie3': {'room3': {'ora': 10, 'pret': 20, 'locuri': 50}, 'movie3': {'ora': 12, 'pret': 22, 'locuri': 50},
#                      'movie3': {'ora': 14, 'pret': 24, 'locuri': 50}, 'movie3': {'ora': 16, 'pret': 26, 'locuri': 50}}
# }
#varianta 2 de dict
# rooms = {'sala1': {'total_scaune': 50, 'scaune_libere': 'scaune_libere.range[1:50]'},
#          'sala2': {'total_scaune': 50, 'scaune_libere': 'scaune_libere.range[1:50]'},
#          'sala3': {'total_scaune': 50, 'scaune_libere': 'scaune_libere.range[1:50]'}
#          }
# movies = {'movie1': {'data': '01.01.2022', 'ora': 10},'movie1':{'data': '02.01.2022', 'ora': 18},
#           'movie2': {'data': '03.01.2022', 'ora': 12},'movie1':{'data': '04.01.2022', 'ora': 20},
#           'movie2': {'data': '05.01.2022', 'ora': 14},'movie1':{'data': '06.01.2022', 'ora': 22}
#           }
# rulare = {'movie1': 'sala1', 'movie2': 'sala2','movie3': 'sala3'}
# film = input('Alege filmul : movie1/movie2/movie3')
# if film == 'movie1':
#     sala_rulare = 'sala1'
#     data = input('Alege data: 01.01.2022/02.01.2022')
#     if data == '01.01.2022' or data == '02.01.2022':
#         ora = input('Alege ora: 10/18: ')
#         if ora == '10' or ora == '18':
#             print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
#            f' \nFilmul va rula in {sala_rulare} si locul tau are numarul.... ')
# elif film == 'movie2':
#     data = input('Alege data - 03.01.2022 sau 04.01.2022')
#     if data == '03.01.2022' or data == '04.01.2022':
#         ora = input('Alege ora - ora 12 sau ora 20')
#         if ora == '12' or ora == '20':
#             sala_rulare = 'sala2'
#             print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
#                   f' \nFilmul va rula in {sala_rulare} si locul tau are numarul.... ')
# elif film == 'movie3':
#     data = input('Alege data - 05.01.2022 sau 06.01.2022')
#     if data == '05.01.2022' or data == '06.01.2022':
#         ora = input('Alege ora - ora 14 sau ora 22')
#         if ora == '14' or ora == '22':
#             sala_rulare = 'sala3'
#             print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
#                   f' \nFilmul va rula in {sala_rulare} si locul tau are numarul.... ')
# else:
#     print(' Filmul ales nu ruleaza!')



#elif film == 'movie2' and ('data' == '03.01.2022' and 'ora' == 12) or ('data' == '04.01.2022' and 'data'==20):
#     sala_rulare = 'sala2'
#     print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
#               f' Filmul va rula in {sala_rulare} si locul tau are numarul.... ')
# elif film == 'movie3' and ('data' == '05.01.2022' and 'ora' == 14) or ('data' == '06.01.2022' and 'data'==22):
#     sala_rulare = 'sala3'
#     print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
#               f' Filmul va rula in {sala_rulare} si locul tau are numarul.... ')
# else:
#     print(' Filmul ales nu ruleaza!')


#print(f'Rezervare dumneavoastra a fost confirmata. Va asteptam in data de {data} la ora {ora}.'
     # f' Filmul va rula in {sala_rulare} si locul tau are numarul.... ')