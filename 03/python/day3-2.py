from itertools import islice

def read_in_chunks(file_path, n):
    with open(file_path) as fh:
        while True:
            lines = list(islice(fh, n))
            if lines: yield lines
            else:     break

score = 0

for lines in read_in_chunks("../input.txt",3):
        print (lines)
        letter_ascii = ord(set(lines[0].strip()).intersection(set(lines[1].strip()).intersection(set(lines[2].strip()))).pop())
        print (chr(letter_ascii))
        if letter_ascii >= ord('a'):
            score = score + letter_ascii - 96
            print (f"Sub: {letter_ascii - 96}")
        else:
            score = score + letter_ascii - 64 + 26
            print (f"Sub: {letter_ascii - 64 + 26}")

print (f"Total: {score}")




