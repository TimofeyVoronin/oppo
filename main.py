# -*- coding: utf-8 -*-
"""Sea Data Processor.

Модуль предоставляет функции для чтения данных о море от пользователя,
их обработки и сохранения в текстовый файл.
"""

import sys


class Sea:
    """Представляет море с названием, глубиной и соленостью."""

    def __init__(self, name, depth, salinity):
        """Инициализирует экземпляр класса Sea.

        Args:
            name: Строка с названием моря.
            depth: Число с плавающей точкой, представляющее глубину.
            salinity: Число с плавающей точкой, представляющее соленость.
        """
        self.name = name
        self.depth = depth
        self.salinity = salinity

    def __str__(self):
        """Возвращает строковое представление объекта Sea."""
        return f'"{self.name}" {self.depth} {self.salinity}'


def read_sea_data():
    """Читает данные о море от пользователя и создает объект Sea.

    Returns:
        Экземпляр класса Sea с данными, введенными пользователем.
    """
    user_input = input()
    tokens = user_input.strip().split()

    try:
        salinity = float(tokens[-1])
        depth = float(tokens[-2])
        name_tokens = tokens[:-2]
        name = ' '.join(name_tokens)
    except (ValueError, IndexError):
        print("Некорректный формат ввода.", file=sys.stderr)
        sys.exit(1)

    return Sea(name, depth, salinity)


def save_sea_data(sea, filename):
    """Сохраняет данные о море в текстовый файл.

    Args:
        sea: Экземпляр класса Sea для сохранения.
        filename: Строка с именем файла для сохранения данных.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{sea}\n')


def main():
    """Основная функция для обработки данных о море."""
    sea = read_sea_data()
    print(sea)
    save_sea_data(sea, 'моря.txt')


if __name__ == '__main__':
    main()
