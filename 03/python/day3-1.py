
score = 0

with open("../input.txt") as sack_data:
    for line in sack_data:
        sack = line.strip()
        letter_ascii = ord(set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])).pop())
        if letter_ascii >= ord('a'):
            score = score + letter_ascii - 96
            print (f"Sub: {letter_ascii - 96}")
        else:
            score = score + letter_ascii - 64 + 26
            print (f"Sub: {letter_ascii - 64 + 26}")

print (f"Total: {score}")




