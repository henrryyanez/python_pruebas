#Error comun con Int enteror y Str string

age = 23
# message = "Happy " + age + "rd Birthday!"  Da error porque "age" tiene tipo numero pero el resultado es en string
message = "Happy " + str(age) + "rd Birthday!"  #Le agregamos el "str" y convertimos en string

print(message)
