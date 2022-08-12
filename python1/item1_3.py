def count_most_voted(lists):
    most_vote = list[0]
    vote_set = set(lists)
    
    for c in vote_set:
        if 0 < int(c) < 21:
            if lists.count(most_vote) < lists.count(c):
                most_vote = c
        else:
            return None
            
    return most_vote
        
        
print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
lists = input().split()

if count_most_voted(lists) != None:
    print(count_most_voted(lists)) 
else:
    print("*** No Candidate Wins ***")
