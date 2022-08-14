def count_most_voted(lists):
    vote_set = set(lists)
    most_vote = ''

    for e in vote_set:
        if 0 < int(e) < 21:
            most_vote = e
            break
        else:
            return None

    for c in vote_set:
        if 0 < int(c) < 21 and lists.count(most_vote) <= lists.count(c):
            most_vote = c

    for c in vote_set:
        if most_vote != c and lists.count(most_vote) == lists.count(c):
            return None

    if 1 > int(most_vote) > 20:
        return None

    return most_vote


print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
lists = input().split()

if count_most_voted(lists) != None:
    print(count_most_voted(lists))
else:
    print("*** No Candidate Wins ***")
