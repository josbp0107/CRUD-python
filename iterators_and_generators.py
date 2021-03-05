#  Iterators and generators

"""
Esta función imprime los numeros de fibonacci

 los generators son simplemente una forma rápida de crear iterables sin la necesidad
 de declarar una clase que implemente el protocolo de iteración. Para crear un generator simplemente declaramos una
 función y utilizamos el keyword YIELD

"""


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a # yield Retorna el siguiente valor en una iteración
        a, b = b, a+b


fib = fibonacci(20)

fib_nums = [num for num in fib]

print(fib_nums)

# Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y
# debemos crear una nueva instancia. Por ejemplo,

# double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)]  # sí funciona