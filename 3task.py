def sort_stack(stack):
    temp = []

    while stack:
        current = stack.pop()

        while temp and temp[-1] > current:
            stack.append(temp.pop())

        temp.append(current)

    while temp:
        stack.append(temp.pop())

    return stack


n = int(input())
stack = list(map(int, input().split()))

print(*sort_stack(stack))