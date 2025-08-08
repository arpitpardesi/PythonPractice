zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''

v = 'aeiou'
count = 0

for i in zen:
    if i in v:
        count += 1

else:
    print(len(zen) - count)


print(f"Vowels: {count}")

    # print(i)