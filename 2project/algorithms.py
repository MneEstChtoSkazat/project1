# Алгоритм Кнута-Морриса-Пратта


def longest_prefix(substring):
    i = 1
    j = 0

    p = [0] * len(substring)
    while i < len(substring):
        if substring[i] == substring[j]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p


def kmp(string, substring):
    len_str, len_sub_str = len(string), len(substring)
    i = 0
    j = 0
    indices = []
    p = longest_prefix(substring)
    while i < len_str:
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == len_sub_str:
                indices.append(i - j)
                j = p[j - 1]

        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    if indices:
        return tuple(indices)
    return None


def boyer_moore_horspool_search(text, pattern):
    t = text
    a = pattern
    S = set()  # уникальные символы в образе
    M = len(t)  # число символов в образе
    d = {}  # словарь смещений

    for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
        if t[i] not in S:  # если символ еще не добавлен в таблицу
            d[t[i]] = M - i - 1
            S.add(t[i])

    if t[M - 1] not in S:  # отдельно формируем последний символ
        d[t[M - 1]] = M

    d["*"] = M  # смещения для прочих символов

    print(d)

    # Этап 2: поиск образа в строке

    N = len(a)

    if N >= M:
        i = M - 1  # счетчик проверяемого символа в строке

        while i < N:
            k = 0
            j = 0
            flBreak = False
            for j in range(M - 1, -1, -1):
                if a[i - k] != t[j]:
                    if j == M - 1:
                        off = (
                            d[a[i]] if d.get(a[i], False) else d["*"]
                        )  # смещение, если не равен последний символ образа
                    else:
                        off = d[
                            t[j]
                        ]  # смещение, если не равен не последний символ образа

                    i += off  # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if (
                not flBreak
            ):  # если дошли до начала образа, значит, все его символы совпали
                print(f"образ найден по индексу {i - k + 1}")
                break
        else:
            return None
    else:
        return None


def rabin_karp_search(string, substring):
    return string, substring


def boyer_moore_search(string, substring):
    return string, substring
