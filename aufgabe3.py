cache = []
sudoku = []

with open('sudoku0.txt', encoding='utf-8-sig') as fileobj:
    for row in fileobj:
        if row != '\n':
            cache.append(row.rstrip('\n'))
for row in cache:
    sudoku.append(row.split())

