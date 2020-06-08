# Nama: Hartono

# netacad email cth: 'abcd@gmail.com'
email = 'sevenco@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded


def letter_catalog(items, letter='A'):
    # MULAI KODEMU DI SINI
    result = []

    for item in items:
        if item.startswith(letter):
            result.append(item)

    return result

# Graded


def counter_item(items):
    # MULAI KODEMU DI SINI
    uniqueList = []
    result = {}

    for item in items:
        if item not in uniqueList:
            uniqueList.append(item)

    for item in uniqueList:
        result[item] = items.count(item)

    return result

    # dictBuah= {}
    # for buah in items:
    #   dictBuah[buah] = dictBuah.get(buah, 0)+1
    # return dictBuah

# Graded


# dua variable berikut jangan diubah
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries',
          'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# list buah
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple',
         'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {}

for i in range(len(fruits)):
    fruit_price[fruits[i]] = prices[i]


def total_price(dcounter, fprice):
    # MULAI KODEMU DI SINI
    total_price = 0

    for item in dcounter:
        total_price += dcounter[item] * fprice[item]

    return total_price

    # total_price = 0
    # for buah, jumlah in dcounter.items():
    #     total_price += jumlah * fprice[buah]
    # return total_price


def discounted_price(total, discount, minprice=100):
    # MULAI KODEMU DI SINI
    price = total - total * discount / 100 if total >= minprice else total
    return price


def print_summary(items, fprice):
    # MULAI KODEMU DI SINI
    cart = counter_item(items)

    for item in sorted(cart.keys()):
        print(cart[item], item, ":", cart[item] * fruit_price[item])

    print('total :', total_price(cart, fruit_price))
    print('discount price :', discounted_price(
        total_price(cart, fruit_price), 10, 100))
