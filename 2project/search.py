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


def parser():
    parser = argparse.ArgumentParser(
        description="Поиск подстрок в тексте с помошью различных алгоритмов"
    )
    parser.add_argument("--string", type=str, help="Текст в котором будем искать")
    parser.add_argument("--sub_string", type=str, help="Подстрока которую будем искать")
    parser.add_argument(
        "--case_sensitivity", type=bool, help="Флаг чувствительности к регистру"
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["first", "last"],
        default="first",
        help="mетод поиска(по умолчанию в прямом порядке)",
    )
    parser.add_argument(
        "--algotithm",
        type=str,
        help=f"Алгоритм для использования. Доступный {avalible_algorithms}",
    )
    parser.add_argument(
        "--count", type=int, help="количество совпадений, которые нужно найти"
    )
    return parser.parse_args()


def search(
    string: str,
    sub_string: Union[str, list[str]],
    case_sensitivity=False,
    method: str = "first",
    count: Optional[int] = None,
    algorithm: str = "kmp",
) -> Optional[Union[tuple[int, ...], dict[str, tuple[int, ...]]]]:
    if algorithm not in avalible_algorithms:
        raise ValueError("Недоступный алгоритм")
    if not case_sensitivity:
        string = string.lower()
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
        if indx == None:
            return None
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

        if indx == None:
            return None
    else:
        raise ValueError(f"Метода {method} не существует")

    def read_file(x):
        try:
            with open(x, "r") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Ошибка: файл '{x}' не найден.")
            return None


if __name__ == "__main__":
    args = parser()
    if args.file:
        string = read_file(args.file)
    elif args.string:
        string = args.string
    else:
        raise ValueError(" ")
    result = search(
        string,
        args.substring,
        case_sensitivity=args.case_sensitive,
        method=args.method,
        count=args.count,
        algorithm=args.algorithm,
    )
    if result:
        for sub in result.items():
            print(f"Подстрока {sub} найдена на позиции(ях) {result}")
    print("Не найдено")
