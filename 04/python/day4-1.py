

def inside_range(e1: list, e2: list) -> bool:
    set1 = set(range(e1[0], e1[1]+1))
    set2 = set(range(e2[0], e2[1]+1))
    if set1.issubset(set2) or set2.issubset(set1):
        print (" - overlapping 🧝 jobs")
        return True
    return False


count = 0


with open("../input.txt") as section_data:
    for line in section_data:
        elf1,elf2 = line.strip().split(",")
        print (elf1,elf2, end=" ")

        elf1_array = [int(s) for s in (elf1.split("-"))]
        elf2_array = [int(s) for s in (elf2.split("-"))]
        if inside_range(elf1_array,elf2_array):
            count += 1
        else:
            print("")

print (f"Overlaps: {count}")