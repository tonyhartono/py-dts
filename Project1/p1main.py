from p1 import *

soal1 = letter_catalog(['Apple', 'Avocado', 'Banana',
                        'Blackberries', 'Blueberries', 'Cherries'], letter='A')
soal2 = counter_item(
    ['Apple', 'Apple', 'Apple', 'Blueberries', 'Blueberries', 'Blueberries'])
soal3 = total_price(counter_item(chart), fruit_price)
soal4 = discounted_price(total_price(
    counter_item(chart), fruit_price), 10, minprice=100)

print(soal1, soal2, soal3, soal4, sep="\n")
print_summary(chart, fruit_price)
