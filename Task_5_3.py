from itertools import zip_longest

tutors = ['Stas', 'Alex', 'Anton', 'Tom']
classes = ['9A', '7A', '8B']

school = zip_longest(tutors, classes)
print(next(school))
print(next(school))
print(next(school))
print(next(school))