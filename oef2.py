def chek_length_type(length_chek_fun) -> float|bool:
    if length_chek_fun.isdigit():
        return float(length_chek_fun)
    elif list(length_chek_fun)[1] == '.':
        return float(length_chek_fun)
    elif list(length_chek_fun)[1] == ',':
        print('Please use "." for length.')
        return False
    else:
        print('Please enter a number for length.')
        return False


def chek_width_type(width_chek_fun) -> float | bool:
    if width_chek_fun.isdigit():
        return float(width_chek_fun)
    elif list(width_chek_fun)[1] == '.':
        return float(width_chek_fun)
    elif list(width_chek_fun)[1] == ',':
        print('Please use "." for width.')
        return False
    else:
        print('Please enter a number for width.')
        return False

def chek_height_type(height_chek_fun) -> float | bool:
    if height_chek_fun.isdigit():
        return float(height_chek_fun)
    elif list(height_chek_fun)[1] == '.':
        return float(height_chek_fun)
    elif list(height_chek_fun)[1] == ',':
        print('Please use "." for height.')
        return False
    else:
        print('Please enter a number for height.')
        return False

def counting_square(length_fun: float, width_fun: float) -> float:
    square = length_fun * width_fun
    return square

def counting_volume(length_fun: float, width_fun: float, height_fun: float) -> float:
    volume = length_fun * width_fun * height_fun
    return volume

width = input('Enter the width of the figure: ')
length = input('Enter the length of the figure: ')
height = input('Enter the height of the figure: ')

cheked_length = chek_length_type(length)
cheked_width = chek_width_type(width)
cheked_height = chek_height_type(height)

if cheked_length is not False and cheked_width is not False and cheked_height is not False :
    result_square = counting_square(
        length_fun=cheked_length,
        width_fun=cheked_width
    )
    result_volume = counting_volume(
        length_fun=cheked_length,
        width_fun=cheked_width,
        height_fun=cheked_height
    )
    print(f'{result_square} square')
    print(f'{result_volume} volume')
