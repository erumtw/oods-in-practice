'''Chapter : 4 - item : 4 - เดาใจไว้แล้วว่าเธอรักฉันแบบที่ฉันรัก'''
class Queue:
    def __init__(self, items=None):
        self.items = [] if items == None else items

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
            return len(self.items)
        
events = {'0': 'Eat', '1': 'Game', '2': 'Learn', '3': 'Movie'}
locations = {'0': 'Res.', '1': 'ClassR.', '2': 'SuperM.', '3': 'Home'}

def cupid(mine: Queue, your: Queue):
    points = 0
    my_al = []
    ur_al = []
    
    while not mine.is_empty():
        mine_temp = mine.deQueue().split(':')
        your_temp = your.deQueue().split(':')
        
        if mine_temp[0] == your_temp[0] and mine_temp[1] != your_temp[1]:
            points += 1
        elif mine_temp[0] != your_temp[0] and mine_temp[1] == your_temp[1]:
            points += 2
        elif mine_temp[0] == your_temp[0] and mine_temp[1] == your_temp[1]:
            points += 4
        else:
            points -= 5
    
        my_al.append(events[mine_temp[0]] + ':' + locations[mine_temp[1]])
        ur_al.append(events[your_temp[0]] + ':' + locations[your_temp[1]])

    return points, my_al, ur_al
        
        
if __name__ == '__main__' :
    
    each_days = input('Enter Input : ').split(',')
    mine_q = Queue([c.split()[0] for c in each_days])
    your_q = Queue([c.split()[1] for c in each_days])
    
    print('My   Queue =', ', '.join(mine_q.items))
    print('Your Queue =', ', '.join(your_q.items))

    p, my_al, ur_al = cupid(mine_q, your_q)
    
    print('My   Activity:Location =', ', '.join(my_al))
    print('Your Activity:Location =', ', '.join(ur_al))
    
    if p >= 7:
        print(f'Yes! You\'re my love! : Score is {p}.')
    elif 0 < p < 7:
        print(f'Umm.. It\'s complicated relationship! : Score is {p}.')
    else:
        print(f'No! We\'re just friends. : Score is {p}.')