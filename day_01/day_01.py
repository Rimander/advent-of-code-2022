file = open("input.txt")
file = file.read()

elf_index = 0
elfs = [0]

for line in file.split("\n"):
    if line != "":
        elfs[elf_index] += int(line)
    else:
        elf_index += 1
        elfs.append(0)

# Part - 1
elfs.sort(reverse=True)
print(elfs[0])

# Part - 2
print(sum(elfs[:3]))
