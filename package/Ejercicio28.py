import random
import functools

def Exercise_28():
    # Normal Version
    numbers = []
    for element in range(1, 11):
        if element % 2 == 0:
            numbers.append(element * 2)
    # List Comprehension
    numbers_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
    # _____________________________________________________________
    # Normal Version
    dict = {}
    for i in range(1, 5):
        dict[i] = i * 2
    # Dictionary Comprehension
    dict_v2 = {i: i * 2 for i in range(1, 5)}
    # _____________________________________________________________
    # Example
    Countries = ['Col', 'Mex', 'Bra', 'Arg']
    Population = {country: random.randint(
        1000, 10000) for country in Countries}
    result = {country: population for (
        country, population) in Population.items() if population < 5000}
    # Example2
    Names = ['Miguel', 'Libny', 'Laura']
    Ages = [24, 20, 1]
    Family = list(zip(Names, Ages))
    new_Dict = {name: age for (name, age) in zip(Names, Ages)}
    # Example3
    text = 'Hola, soy Miguel'
    Vocals = {c: c.upper() for c in text if c in 'aeiou'}
    # _____________________________________________________________
    # Asignar multiples returns a diferentes variables

    def find_volume(lenght=1, widht=2, depth=3):
        return lenght * widht * depth, 'VOLUMEN', 3312

    result, text, width = find_volume(widht=10)
    # _____________________________________________________________
    # Funcion lambda
    increment = lambda x: x * 2
    full_name = lambda name, last_name: f'Su nombre es {name.title()} {last_name.title()}'
    # Example 4
    list_nums, list_nums2 = [1, 2, 3, 4], [5, 6, 7, 8]
    List_nums_v2 = list(map(lambda x, y: x * y, list_nums, list_nums2))
    List_nums_v3 = filter(lambda x: x % 2 == 0, List_nums_v2)
    List_nums_v4 = functools.reduce(lambda counter, item: counter + item, list_nums2)
    # _____________________________________________________________
    # Map
    items = [
        {
            'Producto': 'Camiseta',
            'Price': 12500
        },
        {
            'Producto': 'Blazer',
            'Price': 160000
        },
        {
            'Producto': 'Joger',
            'Price': 45000
        }
    ]

    def add_taxes(item):
        new_item = item.copy()
        new_item['Taxes'] = new_item['Price'] * .19
        return new_item

    prices = list(map(lambda item: item['Price'], items))
    new_items = list(map(add_taxes, items))


if __name__ == "__main__":
    Exercise_28()
