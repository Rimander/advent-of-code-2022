class Box:
    character: None
    box_top: None

    def __repr__(self):
        return self.character


def print_stack(_box: Box):
    stack = ''
    if _box is not None:
        stack = _box.character + ' '
        while _box.box_top is not None:
            _box = _box.box_top
            stack += _box.character + ' '
    print(stack)


with open('input.txt') as file:
    lines = file.readlines()

    boxs = []
    boxs_loaded = False
    for line in lines:
        line = line.replace('\n', '')

        # Create box
        if not boxs_loaded:
            if line[1] == '1':
                boxs_loaded = True
            else:
                size = len(line)

                box_id = 0
                for i in range(0, size, 4):
                    if line[i + 1] != ' ':
                        character = line[i + 1]
                        box_top = None

                        if len(boxs) >= (box_id + 1):
                            box_top = boxs[box_id]

                        box = Box()
                        box.character = character
                        box.box_top = box_top

                        if len(boxs) < (box_id + 1):
                            i = 0
                            while i < box_id + 1:
                                if len(boxs) < i + 1:
                                    boxs.append(None)
                                i += 1
                        boxs[box_id] = box

                    box_id += 1

        # Moves
        elif len(line) > 2:
            line = str(line).replace('move ', '').replace('from ', '').replace('to ', '')
            moves = line.split(' ')

            quantity = int(moves[0])
            from_stack = int(moves[1]) - 1  # Start 0
            to_stack = int(moves[2]) - 1  # Start 0

            for times in range(quantity):
                # Remove
                box_stack_from = boxs[from_stack]
                box_under = None

                while box_stack_from is not None and box_stack_from.box_top is not None:
                    box_under = box_stack_from
                    box_stack_from = box_stack_from.box_top

                if box_under is not None:
                    box_under.box_top = None

                if boxs[from_stack] == box_stack_from:
                    boxs[from_stack] = None

                # Add
                box_stack_to = boxs[to_stack]

                if box_stack_to is None:
                    boxs[to_stack] = box_stack_from
                else:
                    while box_stack_to is not None and box_stack_to.box_top is not None:
                        box_stack_to = box_stack_to.box_top

                    box_stack_to.box_top = box_stack_from

    for box in boxs:
        print_stack(box)

    print("")
    print("")
    print("")
    print("")
    # Part - 2
    boxs = []
    boxs_loaded = False
    for line in lines:
        line = line.replace('\n', '')

        # Create box
        if not boxs_loaded:
            if line[1] == '1':
                boxs_loaded = True
            else:
                size = len(line)

                box_id = 0
                for i in range(0, size, 4):
                    if line[i + 1] != ' ':
                        character = line[i + 1]
                        box_top = None

                        if len(boxs) >= (box_id + 1):
                            box_top = boxs[box_id]

                        box = Box()
                        box.character = character
                        box.box_top = box_top

                        if len(boxs) < (box_id + 1):
                            i = 0
                            while i < box_id + 1:
                                if len(boxs) < i + 1:
                                    boxs.append(None)
                                i += 1
                        boxs[box_id] = box

                    box_id += 1

        # Moves
        # move 1 from 2 to 1
        elif len(line) > 2:
            line = str(line).replace('move ', '').replace('from ', '').replace('to ', '')
            moves = line.split(' ')

            quantity = int(moves[0])
            from_stack = int(moves[1]) - 1  # Start 0
            to_stack = int(moves[2]) - 1  # Start 0

            # Move quantity
            size_stack = 0
            box_stack_from = boxs[from_stack]
            while box_stack_from is not None and box_stack_from.box_top is not None:
                size_stack += 1
                box_stack_from = box_stack_from.box_top

            box_stack_from = boxs[from_stack]
            box_under = None
            for s_t in range(size_stack - quantity + 1):
                box_under = box_stack_from
                box_stack_from = box_stack_from.box_top

            ##
            if box_under is not None:
                box_under.box_top = None

            if boxs[from_stack] == box_stack_from:
                boxs[from_stack] = None

            # Add
            box_stack_to = boxs[to_stack]

            if box_stack_to is None:
                boxs[to_stack] = box_stack_from
            else:
                while box_stack_to is not None and box_stack_to.box_top is not None:
                    box_stack_to = box_stack_to.box_top

                box_stack_to.box_top = box_stack_from

    for box in boxs:
        print_stack(box)
