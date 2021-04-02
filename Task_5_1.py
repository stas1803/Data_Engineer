def generator(nums):
    for nums in range(nums):
        if nums % 2 == 0:
            yield nums


odd_to_15 = generator(16)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
