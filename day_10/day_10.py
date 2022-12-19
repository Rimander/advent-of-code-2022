with open('input.csv') as file:
    lines = file.readlines()

    instructions = []

    for row in lines:
        row = row.replace('\n', '')
        if row.startswith('noop'):
            instructions.append('noop')
        else:
            instructions.append(int(row.replace("addx ", '')))

    x = 1
    instruction_loaded = ''
    instructions.reverse()
    n_cycle = 1

    total = 0
    crt = []
    while len(instructions) > 0 or len(str(instruction_loaded)) > 0:
        crt.append('.')

        # Part - 1
        if n_cycle == 20 or (n_cycle - 20) % 40 == 0:
            total += n_cycle * x

        # Part - 2
        if x == n_cycle % 40 or x == (n_cycle % 40) - 1 or x + 1 == (n_cycle % 40)  - 1:
            crt[n_cycle - 1] = "#"

        if len(str(instruction_loaded)) == 0:
            instruction = instructions.pop()
            if instruction != 'noop':
                instruction_loaded = instruction
        else:
            instruction = instruction_loaded
            instruction_loaded = ''
            x += instruction

        n_cycle += 1

    print(total)

    sprite_str = ''.join(crt)
    print(sprite_str[:40])
    print(sprite_str[40:80])
    print(sprite_str[80:120])
    print(sprite_str[120:160])
    print(sprite_str[160:200])
    print(sprite_str[200:240])
