from collections import deque
A = deque(list(map(str,input())))
B = deque(list(map(str,input())))
C = deque(list(map(str,input())))

def turn(play):
    if play=="a":
        if len(A) == 0: return "A"
        play = A.popleft()
    elif play=="b":
        if len(B) == 0: return "B"
        play = B.popleft()
    else:
        if len(C) == 0: return "C"
        play = C.popleft()
    return turn(play)
print(turn(A.popleft()))