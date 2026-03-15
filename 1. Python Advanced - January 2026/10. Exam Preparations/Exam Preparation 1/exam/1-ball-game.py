from collections import deque

strenghts_stack = [int(el) for el in input().split()]
accuracy_queue = deque([int(el) for el in input().split()])
goals = 0

while strenghts_stack and accuracy_queue:
    current_strength = strenghts_stack[-1]
    current_accuracy = accuracy_queue[0]

    result = current_strength + current_accuracy

    if result == 100:
        strenghts_stack.pop()
        accuracy_queue.popleft()
        goals += 1
    elif result < 100:
        if current_strength < current_accuracy:
            strenghts_stack.pop()
        elif current_strength > current_accuracy:
            accuracy_queue.popleft()
        else:
            strenghts_stack[-1] += current_accuracy
            accuracy_queue.popleft()
    else:
        strenghts_stack[-1] -= 10
        accuracy_queue.append(accuracy_queue.popleft())

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals > 0:
    print(f"Goals scored: {goals}")

if  (not strenghts_stack and accuracy_queue) or (strenghts_stack and not accuracy_queue):
    if strenghts_stack:
        print(f"Strength values left: {', '.join([str(x) for x in strenghts_stack])}")
    if accuracy_queue:
        print(f"Accuracy values left: {', '.join([str(x) for x in accuracy_queue])}")