def num_translate(number):
    dig_2_str = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'cuatro', 'five':'cinco'}
    number_list = list(number)
    number_low = number.lower()
    if number_list[0].isupper() and number_low in dig_2_str:
        print(dig_2_str.get(number_low).capitalize())
    else:
        print(dig_2_str.get(number))


num_translate('One')
