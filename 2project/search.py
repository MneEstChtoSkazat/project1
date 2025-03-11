"""
Модуль для поиска подстрок в тексте с использованием различных алгоритмов.

Доступные алгоритмы:
- Алгоритм Кнута-Морриса-Пратта (KMP)
- Алгоритм Бойера-Мура (BM)
- Алгоритм Рабина-Карпа (RK)
- Алгоритм Бойера-Мура-Хорспула (BMH)
- Алгоритм Ахо-Корасик (AK)
"""

import argparse
from typing import Optional, Union
import aho_corasick_search
from algorithms import (
    kmp,
    boyer_moore_horspool_search,
    rabin_karp_search,
    boyer_moore_search,
)


avalible_algorithms = ["kmp", "bm", "rk", "bmh", "ak"]


def parser_args():
    parser = argparse.ArgumentParser(
        description="Поиск подстрок в тексте с помошью различных алгоритмов"
    )
    parser.add_argument("--string", type=str, help="Текст в котором будем искать")
    parser.add_argument("--file", type=str, help="Путь к файлу в котором искать")
    parser.add_argument(
        "--sub_string",
        type=str,
        required=True,
        nargs="+",
        help="Подстрока которую будем искать",
    )
    parser.add_argument(
        "--case_sensitivity", type=bool, help="Флаг чувствительности к регистру"
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["first", "last"],
        default="first",
        help="Метод поиска(по умолчанию в прямом порядке)",
    )
    parser.add_argument(
        "--algorithm",
        type=str,
        required=True,
        help=f"Алгоритм для использования. Доступны {avalible_algorithms}",
    )
    parser.add_argument(
        "--count", type=int, help="Количество совпадений k, которые нужно найти"
    )
    return parser.parse_args()


def search(
    string: str,
    sub_strings: Union[str, list[str]],
    case_sensitivity=False,
    method: str = "first",
    count: Optional[int] = None,
    algorithm: str = "kmp",
) -> Optional[Union[tuple[int, ...], dict[str, tuple[int, ...]]]]:
    if algorithm not in avalible_algorithms:
        raise ValueError("Недоступный алгоритм")
    if not case_sensitivity:
        string = string.lower()
        sub_strings = [i.lower() for i in sub_strings]
    result = {}
    for sub_string in sub_strings:
        if method == "first":
            match algorithm:
                case "kmp":
                    indx = kmp(string, sub_string)
                case "bmh":
                    indx = boyer_moore_horspool_search(string, sub_string)
                case "rk":
                    indx = rabin_karp_search(string, sub_string)
                case "bm":
                    indx = boyer_moore_search(string, sub_string)
                case "ak":
                    indx = aho_corasick_search(string, sub_string)
            if indx is None:
                return None
            result[sub_string] = indx
        elif method == "last":
            match algorithm:
                case "kmp":
                    indx = kmp(string[::-1], sub_string[::-1])
                case "bm":
                    indx = boyer_moore_search(string[::-1], sub_string[::-1])
                case "rk":
                    indx = rabin_karp_search(string[::-1], sub_string[::-1])
                case "bmh":
                    indx = boyer_moore_horspool_search(string[::-1], sub_string[::-1])
                case "ak":
                    indx = aho_corasick_search(string[::-1], sub_string[::-1])
        else:
            raise ValueError(f"Метода {method} не существует")
        if indx is None:
            return None
        result[sub_string] = indx
        if count and indx:
            return indx[:count]

    return result


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None


if __name__ == "__main__":
    args = parser_args()
    if args.file:
        string = read_file(args.file)
    elif args.string:
        string = args.string
    else:
        raise ValueError("Должег быть передан --string или --file.")
    result = search(
        string,
        args.sub_string,
        case_sensitivity=args.case_sensitivity,
        method=args.method,
        algorithm=args.algorithm,
        count=args.count,
    )
    if result:
        for sub, indx in result.items():
            print(
                f"Подстрока {sub} найдена на {'позиции' if len(indx) == 1 else 'позициях'} {indx}"
            )
    else:
        print("Не найдено")
