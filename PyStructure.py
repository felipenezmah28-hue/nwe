#Decision Structure
from selectors import SelectSelector

idade=int(input("digite sua idade:"))
if idade>18:
    print("Maior de idade", idade)
elif idade<16:
    print("Infanto Juvenil", idade)
else:
    print("Infantil", idade)
