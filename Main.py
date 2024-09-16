from random import random

from Bowling import Bowling

davis = Bowling("Davis")

# Test case 1: All gutter balls
for _ in range(20):
    davis.roll(0)

print("\nAll Gutter balls")
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))
davis.print_score_table()
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))

davis = Bowling("Davis")

# Test case 2: All Strikes
for _ in range(20):
    davis.roll(10)

print('\nAll Strikes')
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))
davis.print_score_table()
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))

davis = Bowling("Davis")

# Test case 3: All Spares
for _ in range(21):
    davis.roll(5)

print('\nAll Spares')
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))
davis.print_score_table()
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))

davis = Bowling("Davis")

# Test case 4: Random rolls
davis.roll(10)
davis.roll(9)
davis.roll(1)
davis.roll(5)
davis.roll(5)
davis.roll(7)
davis.roll(2)
davis.roll(10)
davis.roll(10)
davis.roll(3)
davis.roll(6)
davis.roll(7)
davis.roll(3)
davis.roll(7)
davis.roll(1)
davis.roll(9)
davis.roll(0)

print('\nRandom rolls')
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))
davis.print_score_table()
print('-' * len(
    '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))



print("\n\nShow that the frames can update with each roll\n")
davis = Bowling("Davis")
for i in range(20):
    pins = input(f"Roll {i + 1}, Pins Knocked: ")
    davis.roll(int(pins))
    davis.print_score_table()
    print('-' * len(
        '          Frame 1     Frame 2     Frame 3     Frame 4     Frame 5     Frame 6     Frame 7     Frame 8     Frame 9     Frame 10    Total'))

