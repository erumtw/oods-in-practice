'''กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan เพื่อที่จะวางขายในวันรุ่งขึ้น  
โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  
โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย / คือ 
ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  
ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D  ->  เป้นการนำหนังสือด้านหน้าออกจากชั้น
E <value>  ->  เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง'''


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

# def is_duplicate(arr):
#     print (len(arr), len(set(arr)))

#     for e in set(arr):
#         if arr.count(e) > 1:
#             return True
        
#     return False

if __name__ == "__main__":
    
    inp = input('Enter Input : ').split('/')
    
    bookshelf = Queue(inp[0].split())
    orders = inp[1].split(',')
    
    for c in orders:
        if c != '':
            if 'E' in c:
                bookshelf.enQueue(c[2])
            elif c == 'D':
                if not bookshelf.is_empty(): 
                    bookshelf.deQueue()
    
    books = bookshelf.items
    print(len(books))
    print(len(set(books)))
    if len(books) != len(set(books)):
        print('Duplicate')
    else:
        print('NO Duplicate')
