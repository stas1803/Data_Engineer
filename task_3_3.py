def thesaurus(*args):
    names = [*args]
    new_dict = {}
    for i in range(len(names)):
        key = names[i][0]
        value = names[i]
        if key in new_dict.keys():
            new_dict[key].append(value)
        else:
            new_dict[key] = []
            new_dict[key].append(value)
    print(new_dict)


thesaurus('Stas', 'Anton', 'Sergei', 'Pavel', 'Anrei')
