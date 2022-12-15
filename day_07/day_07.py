class File:
    name = ''
    size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = []
        self.files = []

    def move_up(self):
        return self.parent

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def add_dir(self, name):
        dirs = [x for x in self.directories if x.name == name]
        if len(dirs) <= 0:
            self.directories.append(Directory(name, self))

    def move_to_dir(self, name):
        dirs = [x for x in self.directories if x.name == name]
        return dirs[0]

    def get_size(self):
        return sum([x.size for x in self.files]) + sum([x.get_size() for x in self.directories])


def recursive_search_arr(directory, directories_accepted):
    max_size = 100000
    for dir_ in directory.directories:
        if dir_.get_size() <= max_size:
            directories_accepted.append(dir_)
        recursive_search_arr(dir_, directories_accepted)


def recursive_all_arr(directory, directories_accepted):
    for dir_ in directory.directories:
        directories_accepted.append(dir_)
        recursive_all_arr(dir_, directories_accepted)


with open('input.csv') as file:
    lines = file.readlines()
    base_dir = Directory("/", None)
    dir_obj = {'dir': base_dir}

    for line in lines:
        line = str(line).replace('\n', '')

        # Command CD
        if line.startswith('$ cd '):
            line = line.replace('$ cd ', '')
            if line == '/':
                pass
            elif line == '..':
                # Move up
                dir_obj['dir'] = dir_obj['dir'].move_up()
            else:
                # Move to dir
                dir_obj['dir'] = dir_obj['dir'].move_to_dir(line)

        # Command dir
        elif line.startswith('dir '):
            line = line.replace('dir ', '')
            dir_obj['dir'].add_dir(line)

        # Command ls
        elif line.startswith('$ ls'):
            pass

        # File
        else:
            file_size = line.split(' ')[0]
            file_name = line.replace(file_size, '').strip()
            dir_obj['dir'].add_file(file_name, int(file_size))

    arr_dir = []
    recursive_search_arr(base_dir, arr_dir)
    print("PART - 1")
    print(sum([d.get_size() for d in arr_dir]))

    # Part - 2
    arr_dir = []
    recursive_all_arr(base_dir, arr_dir)
    arr_dir = sorted(arr_dir, key=lambda x: x.get_size(), reverse=True)

    total_size = 70_000_000
    min_size = 30_000_000
    used = base_dir.get_size()

    dir_to_remove = None

    index = 0
    dir_size = len(arr_dir)

    while index < dir_size:
        dir_selected = arr_dir[index]
        size_selected = dir_selected.get_size()

        if total_size - used + size_selected >= min_size:
            dir_to_remove = dir_selected
            index += 1
        else:
            index = dir_size

    print("PART - 2")
    print(dir_to_remove.name)
    print(dir_to_remove.get_size())
