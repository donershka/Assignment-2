from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


n = int(input())
s = MyStack()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        s.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "top":
        print(s.top())
    elif cmd[0] == "empty":
        print(s.empty())