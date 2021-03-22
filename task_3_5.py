from random import choice


def get_jokes(num_of_jokes):
    nouns = ['pig', 'dog', 'cat']
    verbs = ["I see", "I'm playing with", "I'm yelling at"]
    adjectives = ['funny', 'sad', 'silly']
    aaa = []
    for i in range(num_of_jokes):
        aaa.append(choice(verbs) + ' ' + choice(adjectives) + ' ' + choice(nouns))
    print(aaa)


get_jokes(3)
