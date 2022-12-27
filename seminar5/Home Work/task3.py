# 3.	Создайте программу для игры в "Крестики-нолики".

def print_field(field, field_numbers):
    for i in range(len(field)):
        print(field[i], end='\t')
        print(field_numbers[i])
def check_win(field):
    if any(i[0] == i[1] == i[2] != '-' for i in field):
        return True
    if any(a == b == c != '-' for a, b, c in zip(*field)):
        return True
    if field[0][0] == field[1][1] == field[2][2] != '-' or field[2][0] == field[1][1] == field[0][2] != '-':
        return True
    return False
def draw(field):
    if all(i[0] and i[1] and i[2] != '-' for i in field):
        return True
    return False
if __name__ == '__main__':
    field = [['-'] * 3 for _ in range(3)]
    field_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    positions = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                 4: (1, 0), 5: (1, 1), 6: (1, 2),
                 7: (2, 0), 8: (2, 1), 9: (2, 2),}
    get_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    wins = {0: "X", 1: '0'}
    print('Начало игры')
    hod = 0
    while True:
        print_field(field, field_numbers)
        print(f'Ход {wins[hod]}')
        inp = int(input(f'Выберите позицию: {get_pos} : '))
        while inp not in get_pos:
            inp = int(input(f'Выберите правильную позицию: {get_pos} : '))
        x, y = positions[inp]
        get_pos.remove(inp)
        field[x][y] = wins[hod]
        if check_win(field):
            print(f'Выйграл {wins[hod]}')
            print('Конец игры')
            break
        if draw(field):
            print('Ничья')
            print('Конец игры')
            break
        hod = (hod + 1) % 2
