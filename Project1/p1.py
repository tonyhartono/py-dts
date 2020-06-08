# nama file p1.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

# netacad email cth: 'abcd@gmail.com'
email = 'sevenco@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded


def letter_catalog(items, letter='A'):
    return [item for item in items if item.startswith(letter)]

# Graded


def counter_item(items):
    return {item: items.count(item) for item in sorted(list(set(items)))}

# Graded


# dua variable berikut jangan diubah
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries',
          'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# list buah
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple',
         'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits, prices))


def total_price(dcounter, fprice):
    return sum(dcounter[item] * fprice[item] for item in dcounter)

# Graded


def discounted_price(total, discount, minprice=100):
    return total - total * discount / 100 if (total >= minprice) else total

# Graded


def print_summary(items, fprice):
    cart = counter_item(items)
    for item in sorted(cart):
        print(cart[item], item, ":", cart[item] * fruit_price[item])
    print('total :', total_price(cart, fruit_price))
    print('discount price :', discounted_price(
        total_price(cart, fruit_price), 10, 100))
