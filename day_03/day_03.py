CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

with open('input.txt') as file:
    lines = file.readlines()

    # Part - 1
    points = 0
    for line in lines:
        line = line.replace('\n', '')
        first = line[0:int(len(line) / 2)]
        second = line[int(len(line) / 2):]

        equal_item = None
        for f_character in first:
            if f_character in second:
                equal_item = f_character

        if equal_item is not None:
            points += CHARACTERS.index(equal_item) + 1

    print(points)

    # Part - 2
    points = 0
    for index in range(0, len(lines), 3):
        lines_group = lines[index: index + 3]

        l_1 = lines_group[0].replace('\n', '')
        l_2 = lines_group[1].replace('\n', '')
        l_3 = lines_group[2].replace('\n', '')

        equal_item = None
        first_equal = False
        second_equal = False

        for f_character in l_1:
            if f_character in l_2 and f_character in l_3:
                equal_item = f_character

        if equal_item is not None:
            points += CHARACTERS.index(equal_item) + 1

    print(points)
