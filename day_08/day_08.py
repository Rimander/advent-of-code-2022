def is_visible_col(row_index, col_index, matrix):
    if col_index == 0 or col_index == len(matrix) - 1:
        return True

    tree = matrix[row_index][col_index]
    visible = True

    for r_idx in range(0, row_index):
        visible = visible and tree > matrix[r_idx][col_index]

    if visible:
        return True

    visible = True

    for r_idx_f in range(len(matrix) - 1, row_index, -1):
        visible = visible and tree > matrix[r_idx_f][col_index]

    return visible


def is_visible_row(row_index, col_index, matrix):
    if row_index == 0 or row_index == len(matrix) - 1:
        return True

    tree = matrix[row_index][col_index]
    visible = True

    for c_idx in range(0, col_index):
        visible = visible and tree > matrix[row_index][c_idx]

    if visible:
        return True

    visible = True
    for c_idx_f in range(len(matrix) - 1, col_index, -1):
        visible = visible and tree > matrix[row_index][c_idx_f]

    return visible


def max_visible_up(row_index, col_index, matrix):
    if row_index < 0:
        return 0

    if row_index == 0:
        return 1

    tree = matrix[row_index][col_index]
    visible_count = 0
    for r_idx in range(row_index - 1, -1, -1):
        view_tree = matrix[r_idx][col_index]
        if view_tree < tree:
            visible_count += 1
        elif view_tree >= tree:
            visible_count += 1
            break

    return visible_count


def max_visible_down(row_index, col_index, matrix):
    if row_index == len(matrix) - 1:
        return 0

    tree = matrix[row_index][col_index]
    visible_count = 0
    for r_idx in range(row_index + 1, len(matrix), 1):
        view_tree = matrix[r_idx][col_index]
        if view_tree < tree:
            visible_count += 1
        elif view_tree >= tree:
            visible_count += 1
            break

    return visible_count


def max_visible_right(row_index, col_index, matrix):
    if col_index == len(matrix) - 1:
        return 0

    tree = matrix[row_index][col_index]
    visible_count = 0
    for c_idx in range(col_index + 1, len(matrix), 1):
        view_tree = matrix[row_index][c_idx]
        if view_tree < tree:
            visible_count += 1
        elif view_tree >= tree:
            visible_count += 1
            break

    return visible_count


def max_visible_left(row_index, col_index, matrix):
    if col_index == 0:
        return 0

    tree = matrix[row_index][col_index]
    visible_count = 0
    for c_idx in range(col_index - 1, -1, -1):
        view_tree = matrix[row_index][c_idx]
        if view_tree < tree:
            visible_count += 1
        elif view_tree >= tree:
            visible_count += 1
            break

    return visible_count


with open('input.csv') as file:
    lines = file.readlines()

    tree_matrix = []

    for row in lines:
        row = row.replace('\n', '')
        characters = [int(x) for x in row]
        tree_matrix.append(characters)

    n_rows = len(tree_matrix)
    n_columns = len(tree_matrix[0])

    # Part - 1
    visible = 0
    for r in range(n_rows):
        for c in range(n_columns):
            is_visible = is_visible_col(r, c, tree_matrix) or is_visible_row(r, c, tree_matrix)
            visible += 1 if is_visible else 0
    print(visible)

    # Part - 2
    max_visible = 0
    for r in range(n_rows):
        for c in range(n_columns):
            if r == 0 or c == 0 or r == n_rows - 1 or c == n_columns - 1:
                continue
            max_visible_tmp = 1
            tmp = max_visible_up(r, c, tree_matrix)
            max_visible_tmp *= tmp if tmp > 0 else 1

            tmp = max_visible_down(r, c, tree_matrix)
            max_visible_tmp *= tmp if tmp > 0 else 1

            tmp = max_visible_left(r, c, tree_matrix)
            max_visible_tmp *= tmp if tmp > 0 else 1

            tmp = max_visible_right(r, c, tree_matrix)
            max_visible_tmp *= tmp if tmp > 0 else 1

            if max_visible_tmp > max_visible:
                max_visible = max_visible_tmp

    print(max_visible)
