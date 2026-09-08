def check_number(value: str, name: str) -> float | bool:
    if ',' in value:
        print(f'Please use "." for {name}.')
        return False

    try:
        return float(value)
    except ValueError:
        print(f'Please enter a number for {name}.')
        return False


def counting_square(length_fun: float, width_fun: float) -> float:
    return length_fun * width_fun


def counting_volume(length_fun: float, width_fun: float, height_fun: float) -> float:
    return length_fun * width_fun * height_fun


def main():
    width = input('Enter the width of the figure: ')
    length = input('Enter the length of the figure: ')
    height = input('Enter the height of the figure: ')

    checked_width = check_number(value=width, name='width')
    checked_length = check_number(value=length, name='length')
    checked_height = check_number(value=height, name='height')

    if (
        checked_length is not False
        and checked_width is not False
        and checked_height is not False
    ):
        square = counting_square(length_fun=checked_length, width_fun=checked_width)
        volume = counting_volume(
            length_fun=checked_length,
            width_fun=checked_width,
            height_fun=checked_height
        )

        print(f'{square} square')
        print(f'{volume} volume')


if __name__ == '__main__':
    main()