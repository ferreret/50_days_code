"""
Coding Exercise (k-th symbol in Grammar)

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10. 
For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110. Given two integer n and k
return the kth (1-indexed) symbol in the nth row of a table of n rows.

0
01
0110
01101001
0110100110010110

Fijate que la fila 4 es la fila 3 concatenada consigo misma invertida y con los 0s cambiados por 1s y viceversa.
"""


def kth_symbol(n, k):
    # write your code here
    # if n == 1:
    #     return 0
    # if kth_symbol(n - 1, (k + 1) // 2) == 0:
    #     return 0 if k % 2 == 1 else 1
    # else:
    #     return 1 if k % 2 == 1 else 0

    if n == 1:
        return 0

    seq_length = 2 ** (n - 1)
    mid = seq_length // 2

    if k <= mid:
        return kth_symbol(n - 1, k)
    else:
        return 1 - kth_symbol(n - 1, k - mid)


if __name__ == "__main__":
    print(kth_symbol(4, 5))  # 1
    print(kth_symbol(1, 1))  # 0
    print(kth_symbol(2, 1))  # 0
    print(kth_symbol(2, 2))  # 1
