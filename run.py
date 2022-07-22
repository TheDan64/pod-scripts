import random

from collections import defaultdict
from itertools import combinations

prompt = """\
Type one of the following commands:
add [person]
remove [person]
show
next
exit
> """

all_ppl = []
all_pairs = defaultdict(bool)
round = 1

while True:
    command = input(prompt).split(' ')

    if len(command) >= 2 and (command[0] == "add" or command[0] == "a"):
        if command[1] not in all_ppl:
            all_ppl.append(command[1])
            print("added", command[1], '\n')
        else:
            print(command[1], "was already added\n")

    elif len(command) >= 2 and (command[0] == "remove" or command[0] == "r"):
        if command[1] in all_ppl:
            all_ppl.remove(command[1])
            print("removed", command[1], '\n')
        else:
            print(command[1], "was not found\n")

    elif len(command) == 1 and (command[0] == "show" or command[0] == "s"):
        print("all ppl", all_ppl, '\n')
    elif len(command) == 1 and (command[0] == "next" or command[0] == "n"):
        print("Beginning round:", round)
        round += 1

        current_round = {}

        # If we don't shuffle the list, the same person will get left out when
        # there are odd numbers of people
        random.shuffle(all_ppl)

        for p1, p2 in combinations(all_ppl, r=2):
            if p1 in current_round or p2 in current_round or all_pairs[(p1, p2)] or all_pairs[(p2, p1)]:
                continue

            print("Pair", p1, p2)
            all_pairs[(p1, p2)] = True
            current_round[p1] = True
            current_round[p2] = True

        print("")

    elif len(command) == 1 and command[0] == "exit":
        print("done")
        break
    else:
        print("unknown command", command[0])
        continue
