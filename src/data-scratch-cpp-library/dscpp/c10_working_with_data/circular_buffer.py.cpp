from collections import deque

if __name__ == "__main__":
    d = deque(maxlen=20)
    for i in range(1000):
        d.append(i)
        print(list(d))
