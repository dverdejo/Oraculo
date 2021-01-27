import random

name = input("¿Cuál es tu nombre?  ")
question = input("¿Cuál es tu pregunta?  ")

print("Bienvenid@ " + name + ". Tu pregunta fue: " + question + "¡Veamos que dice el Oraculo!")

answer = ""
random_number = random.randint(1, 9)


if random_number == 1:
  print("Confía en el tiempo. Suele dar dulces salidas a amrgas dificultades.")
elif random_number == 2:
  print("El fracaso más grande es nunca haberlo intentado.")
elif random_number == 3:
  print("Si buscas resultados distintos, no hagas siempre lo mismo.")
elif random_number == 4:
  print("No puedes dirigir el viento, pero si ajustar las velas.")
elif random_number == 5:
  print("Si el plan no funciona, cambia el plan. No la meta.")
elif random_number == 6:
  print("La mejor forma de predecir el futuro es crearlo.")
elif random_number == 7:
  print("Nada es una perdida de tiempo si aprendiste algo de eso.")
elif random_number == 8:
  print("Si quieres ver el arcoiris tienes que primero tolerar la lluvia.")
else:
  print("Las dificultades preparan a personas comunes para destinos extraordinarios.")

