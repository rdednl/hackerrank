book = {}

def add(contact):
    for _ in [contact[0:i] for i in range(1, len(contact) + 1)]:
        book[_] = book.get(_, 0) + 1

def find(contact):
    return book.get(contact, 0)

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == str('add'):
        add(contact)
    if op == str('find'):
        print(find(contact))