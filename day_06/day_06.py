def find_duplicates(s):
    elements = {}
    for char in s:
        if elements.get(char, None) != None:
            elements[char] += 1
        else:
            elements[char] = 1
    return [k for k, v in elements.items() if v > 1]


with open('input.txt') as file:
    lines = file.readlines()

    # Part - 1
    index_return = 0

    for line in lines:
        line = line.replace('\n', '')

        for i in range(len(line)):
            line_short = line[i: i + 4]

            if len(line_short) < 4:
                break

            duplicates = find_duplicates(line_short)

            if len(duplicates) == 0:
                index_return = i + 4

                break


        print(index_return)


    # Part - 2
    index_return = 0

    for line in lines:
        line = line.replace('\n', '')

        for i in range(len(line)):
            line_short = line[i: i + 14]

            if len(line_short) < 14:
                break

            duplicates = find_duplicates(line_short)

            if len(duplicates) == 0:
                index_return = i + 14

                break
        print(index_return)