import random


CHOICES = ['taş','kağıt','makas']
print(
"""
1. Taş
2. Kağıt
3. Makas
"""
)
POINT = 3
while True:
    try:
        number = int(input('Numara gir: '))
        random_choices = random.choice(CHOICES)
        if POINT <= 0:
            print('Hakkınız bitti.')
            break
        elif random_choices == 'taş' and number == 2:
            print(f'Kazandın Bot: {random_choices} Sen: Kağıt')
            break
        elif random_choices == 'kağıt' and number == 3:
            print(f'Kazandın Bot: {random_choices} Sen: Makas')

        elif random_choices == 'makas' and number == 1:
            print(f'Kazandın Bot: {random_choices} Sen: Taş') 
        else:
            print(f'Yanlış. {POINT} Hakkınız kaldı.')
            POINT -= 1
    except ValueError:
        print('Lütfen sayı girin.')