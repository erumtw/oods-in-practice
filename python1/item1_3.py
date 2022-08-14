# from random import randrange

def count_most_voted(lists):
    most_vote = list[0]
    vote_set = set(lists)

    for c in vote_set:
        if 0 < int(c) < 21:
            # print(f"{c:2} = {lists.count(c)}")
            if lists.count(most_vote) < lists.count(c):
                most_vote = c
        else:
            return None

    for c in vote_set:
        if most_vote != c and lists.count(most_vote) == lists.count(c):
            return None

    return most_vote


print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
lists = input().split()
# lists = [randrange(1,20) for i in range(voters)]
# print(lists)

if count_most_voted(lists) != None:
    print(count_most_voted(lists))
else:
    print("*** No Candidate Wins ***")
