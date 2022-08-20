import calculations.pakiety_zad3

kapital_poczatkowy = float(input('Podaj poczatkowy kapital: '))
oprocentowanie = float(input('Podaj oprocentowanie: '))
trwanie = int(input('Podaj czas trwania inwestycji: '))

wynik = calculations.pakiety_zad3.wart_lokaty(kapital_poczatkowy, oprocentowanie, trwanie)
print(f'{wynik:.2f}')

