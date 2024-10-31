new_line = []

with open('example.txt', 'r') as file:
    for line in file:
        new_line.append(line[::-1])  # Переворачивает каждую строку и добавляет в список

with open('output.txt', 'w') as file:
    file.write(''.join(new_line)) 