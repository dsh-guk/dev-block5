"""
Игра «Крестики-нолики».
Для двух человек.
Размер поля - 3x3.
Игра выводится в консоль.
"""


def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x  ")
    print(" x - номер ячейки  ")
    print()


board = list(range(1, 10))  # Список номеров и значений клеток / ячеек игровой доски

# перечисление выигрышных комбинаций:
wins_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():  # отрисовка доски - игрового поля
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):  # ввод X или 0
    while True:
        value = input(f'Укажите номер клетки, куда поставить {player_token}: ')  # выбор номера клетки для X или 0
        # Проверка, что введено число (номер клетки) от 1 до 9, а не что-нибудь другое:
        if not (value in '123456789') or len(value) != 1:
            print('Ошибочный ввод. Повторите.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':  # Проверка, что ячейка уже не занята X или 0
            print('Эта клетка уже занята. Попробуйте другую.')
            continue
        board[value - 1] = player_token  # Запись в список нового значения введёного X или 0
        break


def check_win():  # проверка выигрышных комбинаций на поле
    for each in wins_comb:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():  # основная функция
    counter = 0  # счётчик ходов
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')  # X ходит по нечётным
        else:
            take_input('O')  # O ходит по чётным
        if counter > 3:
            winner = check_win()  # проверка победителя, начиная с 3-го хода
            if winner:
                draw_board()
                print(f'Ура! {winner} выиграл!')
                break
        counter += 1
        if counter > 8:  # при отсутствии выигрышных комбинаций на 9 ходу -> ничья
            draw_board()
            print('Ничья!')
            break


greet()
main()
