
Nombre1="Guillermo"
Edad1=25
Peso1=70.50
Casado1= False

Nombre2="Ethan"
Edad2=22
Peso2=75.50
Casado2= True

if Casado1:
    print("Mi nombre es {}, tengo {} años y peso {} kilos".format(Nombre1,Edad1,Peso1))
if Casado2:
    print("Mi nombre es {}, tengo {} años y peso {} kilos".format(Nombre2,Edad2,Peso2))

if Edad1 < Edad2:
    print("{} es menor que {}".format(Nombre1,Nombre2))
if Edad1 > Edad2:
    print("{} es mayor que {}".format(Nombre1, Nombre2))