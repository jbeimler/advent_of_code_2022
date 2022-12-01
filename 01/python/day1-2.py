#!/usr/bin/env python


all_calories: list[int] = []
cur_calories: int = 0
elf_count: int = 0

with open("../elf_data.txt") as elf_data:

    for line_calories in elf_data:
        if not line_calories.strip():
            all_calories.append(cur_calories)
            print(f"🧝‍♀️ number {len(all_calories)} has {cur_calories} calories.")
            cur_calories = 0
        else:
            cur_calories += int(line_calories)

all_calories.sort(reverse=True)
top3_calories = all_calories[:3]
print()
print(f"The 🧝‍♀️ with the most calories has {top3_calories[0]} calories.")
print(f"The top 3 🧝‍♀️ are carrying {sum(top3_calories)} calories")
