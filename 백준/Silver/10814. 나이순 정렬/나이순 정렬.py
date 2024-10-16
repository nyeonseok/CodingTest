import sys

n = int(sys.stdin.readline().strip())

people = []


for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    people.append((int(a), b)) 


sorted_people = sorted(people, key=lambda x: x[0])


for person in sorted_people:
    print(person[0], person[1])
