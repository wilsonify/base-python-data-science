from collections import deque

if __name__ == "__main__":
    maxlen = 20
    d = deque(maxlen=maxlen)
    for i in range(100):
        d.append(i)
        print(list(d))
