"""Test Control Flow"""

name = input()
age = int(input())

if name == 'Alice':
    print('Hi, Alice!')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, ALice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
