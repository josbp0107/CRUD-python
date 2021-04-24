PASSWORD = '1234'

def password_required(func): # func, es la funcion a la que le vamos a aplicar el docorador
    def wrapper(): # Por convención se coloca por nombre a la funcion wrapper
        password = input('Whats your password: ')

        if password == PASSWORD:
            return func()
        else:
            print('The password is wront')
    return wrapper

@password_required # Decorador
def needs_password():
    print("The password is correct.")



def upper(func): 
    # *args y **kwargs, son los argumentos que tienen keywords
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper
@upper
def say_my_name(name):
    return f"Hola {name}"



if __name__ == '__main__':
    needs_password()
    print(say_my_name('Jose'))