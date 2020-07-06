test_dictionary = {1: "one", "two":2, 3:3}

print(test_dictionary.get(4,"No 4 found"))

nums = [55,44,33,22,11]

if all([i > 10 for i in nums]):
    print("All greater than 10.")

if any([i%2 == 0 for i in nums]):
    print("At least one divisible by 2.")

for e in enumerate(nums):
    print(e)