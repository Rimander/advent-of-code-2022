
with open('input.txt') as file:
    lines = file.readlines()
    
    # Part - 1
    points = 0
    for line in lines:
        line = line.replace('\n', '')
        first = line.split(',')[0]
        second = line.split(',')[1]

        first_min = int(first.split('-')[0])
        first_max = int(first.split('-')[1])

        second_min = int(second.split('-')[0])
        second_max = int(second.split('-')[1])

        if first_min <= second_min and first_max >= second_max:
            points += 1
        elif second_min <= first_min and second_max >= first_max:
            points += 1

    print(points)

    # Part - 2
    points = 0
    for line in lines:
        line = line.replace('\n', '')
        first = line.split(',')[0]
        second = line.split(',')[1]

        first_min = int(first.split('-')[0])
        first_max = int(first.split('-')[1])

        second_min = int(second.split('-')[0])
        second_max = int(second.split('-')[1])

        if first_min <= second_min <= first_max:
            points += 1
        elif first_min <= second_max <= first_max:
            points += 1
        elif second_min <= first_min <= second_max:
            points += 1
        elif second_min <= first_max <= second_max:
            points += 1

    print(points)
