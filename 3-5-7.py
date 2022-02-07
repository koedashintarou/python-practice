nums = [1, 3, 11, 12, 13, 21, 22, 23]

list(filter(lambda x : (x % 2) == 1, nums))

list(filter(lambda x : (x > 13), nums))

list(filter(lambda x : (x < 8), nums))
