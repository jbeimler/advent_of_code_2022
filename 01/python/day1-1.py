#!/usr/bin/env python


max_calories: int = 0
cur_calories: int = 0
elf_count: int = 0

with open("../elf_data.txt") as elf_data:

    for line_calories in elf_data:
        if not line_calories.strip():
            print(f"🧝‍♀️ number {elf_count} had {cur_calories} calories.")
            if cur_calories > max_calories:
                max_calories = cur_calories
            cur_calories = 0
            elf_count += 1
        else:
            cur_calories += int(line_calories)
print()
print(f"The 🧝‍♀️  with the most calories has {max_calories} calories.")
