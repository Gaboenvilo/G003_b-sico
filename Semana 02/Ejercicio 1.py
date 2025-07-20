"Crear dos variables para los valores de nombre, profesión y ciudad"
"Crear 2 variables para la remuneración de enero y febrero (más de 1500)"
"Crear 1 variable donde se sumará el ingreso de los dos meses de enero y febrero"
"Mostrar en pantalla el mensaje de:"

"Hola soy 'nombre' mi profesión es 'profesión' mi ciudad es "" y mi remnuneración acumulada es de 'remuneracion_total'"


def datos(nombre, profesión,ciudad,ingreso_enero, ingreso_febrero):
    n= nombre
    p=profesión
    c=ciudad
    ie=ingreso_enero
    ife=ingreso_febrero
    suma=ie+ife
    return("hola soy {} mi profesión es {} mi ciudad es {} y mi remuneración acumulada es de {}".format(n,p,c,suma))
primera_persona = datos("Arturo", "médico", "Arequipa", 3000, 2500)
segunda_persona = datos("Rafael", "abogado", "Buenos aires", 2000, 1700)

print(primera_persona)
print(segunda_persona)


