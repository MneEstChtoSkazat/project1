import array
import random
import argparse
from typing import Callable, Optional


def my_sort(
    array: list,
    reverse: bool = False,
    key: Optional[Callable] = None,
    cmp: Optional[Callable] = None,
    algorithm="timsort",
) -> list:
    pass

    if key:
        array = [key(x) for x in array]
    if algorithm == "timsort":
        return timsort(array)
    elif algorithm == "mergesort":
        return merge_sort(array)
    elif algorithm == "quicksort":
        return quick_sort(array)
    elif algorithm:
        return insertion_sort(array)

    else:
        raise ValueError(f"Неизвестный алгоритм {algorithm}")


def merge_sort(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def split_and_merge(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]
    if len(a1) > 1:
        a1 = split_and_merge(a1)
    if len(a2) > 1:
        a2 = split_and_merge(a2)
    return merge_sort(a1, a2)


def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)]
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hig = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hig)
    return a


def insertion_sort(a):
    N = len(a)

    for i in range(1, N):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break
    return a


def main():
    parser = argparse.ArgumentParser(
        description="Сортировка массива с выбором алгоритма."
    )
    parser.add_argument(
        "-i", "--input", type=str, help="Путь к файлу с исходным массивом"
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        choices=["timsort", "mergesort", "quicksort", "insert"],
        default="timsort",
        help="Алгоритм сортировки",
    )
    parser.add_argument(
        "-r", "--reverse", action="store_true", help="Сортировать в обратном порядке"
    )

    args = parser.parse_args()
    sorted_array = my_sort(array, reverse=args.reverse, algorithm=args.algorithm)
    print(sorted_array)


def timsort(a):
    return


if __name__ == "main":
    main()
