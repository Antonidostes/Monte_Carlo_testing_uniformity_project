import numpy as np


def D_stat(numbers, N):
    numbers_sorted = np.sort(numbers)

    dp = np.max(np.arange(1, N + 1) / N - numbers_sorted)
    dm = np.max(numbers_sorted - np.arange(N) / N)
    return np.maximum(dp, dm)


def Chi_stat(numbers, N):
    summ = 0
    numbers = np.sort(numbers)
    interval = N * 0.01
    border = interval
    expected = N * 0.01
    i = 0
    while i < len(numbers):
        counter = 0
        while numbers[i] < border and i < len(numbers):
            counter += 1
            i += 1
        border += interval
        summ += (counter - expected) ** 2 / expected
    return summ

