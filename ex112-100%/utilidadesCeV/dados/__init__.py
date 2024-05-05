def leiaDinheiro(message=''):
    while True:
        price = str(input(f'{message}')).strip()
        if price.isspace() or price in '' or price.isalpha():
            print(f'\033[31mError, "{price}" is not valid.\033[m')
        else:
            if (not price.isalpha() and not 
                price.isspace() and price.isnumeric() and price.find(',') != -1 and price not in ''):
                price = price.replace(',','.')
                price = float(price)
                break
            if (not price.isalpha() and not 
                price.isspace() and not price.isalnum() and price.isnumeric().__float__ or price.isnumeric() and price not in ''):
                price = float(price)
                break

    return price

# This is what I did, I'm tired man.
