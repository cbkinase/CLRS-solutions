def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]

        j = i - 1

        print(f"\n\t\t\tkey: {key}\n")

        while j > -1 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
            print(f"\t\t\t{nums}")

        nums[j + 1] = key
        print(nums)

nums = [5, 2, 4, 6, 1, 3]
ins_nums = nums[:]

insertion_sort(ins_nums)
