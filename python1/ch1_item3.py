'''
โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี 
โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา 
จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด
ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ
'''


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
