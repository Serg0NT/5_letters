def print_nmb():
    """
    Печатает числа от 0 до 1000,
    кратные трём и не кратные пяти,
    сумма цифр в которых меньше десяти.
    """
    for number in range(0, 1001):
        if number % 3 == 0 and number % 5 != 0 and number != 0:
            sum_figure = 0
            numb = number
            while numb:
                figure = numb % 10
                sum_figure += figure
                numb = numb//10
            if sum_figure < 10:
                print(number)



print_nmb()

