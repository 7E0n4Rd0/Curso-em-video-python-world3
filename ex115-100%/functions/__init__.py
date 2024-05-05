from time import sleep

def readInt(message=''):
    """
    This function will try to read only Integer numbers.
    :param message: receives a text.
    return: the integer number that the user typed.
    """
    while True:
        try:
            number = int(input(message))
        except (ValueError, TypeError):
            print('\033[31mError!! Enter only integer numbers\033[m')
        except Exception as error:
            print(f'The problem was caused by: {error.__class__}')
        except KeyboardInterrupt:
            print('\033[31mThe user choosed to not inform the number.\033[m')
            return 0
        else:
            break
    return number


def registerPerson():
    """
    Register peoples data: Name and age, the function will not register if the name is empty or age is zero.
    return: a tuple called personData.
    """
    file = open('pythonexercícios_W03/ex115/data.txt', 'a+')
    name = str(input('Name: ')).strip().title()
    age = readInt('Age: ')
    if (age == 0 or name in ''):
        print(f'Unsucessful registration. Name was {name} and age was {age}')
        sleep(2)
    elif (f"('{name}',{age})" in file):
        print(f'Unsucessful registration. This person was registered.')
        personData = -1
        sleep(2)
    else:
        personData = (name, age)
        try:
            file.writelines(f'{personData}\n')
        except:
            print('Occured an error during the registering data.')
        else:
            print('Sucessful Registration.')
        sleep(2)


def queryData(directory=''):
    """
    Shows all the data of the people who was registered.
    """
    file = open(directory, "r")
    for line in file:
        line = line.strip()
        dataTuple = eval(line)
        name, age = dataTuple
        print(f'{name:<35} {age:>3} years old.')
    sleep(5)
    file.close()