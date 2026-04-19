# Subsequence print

def subseq(arr, index, current):
    if index == len(arr):
        print(current)
        return

    # include
    subseq(arr, index+1, current + [arr[index]])

    # exclude
    subseq(arr, index+1, current)


subseq([1,2], 0, [])


# Permutations
def permute(s, path):
    if not s:
        print(path)
        return

    for i in range(len(s)):
        permute(s[:i] + s[i+1:], path + s[i])


permute("ab", "")


# N numbers sum in recursive
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n-1)

print(sum_n(5))