from collections import deque


def demo_deque(maxlen, iterations):
    d = deque(maxlen=maxlen)
    for i in range(iterations):
        d.append(i)
        print(list(d))
    return list(d)


if __name__ == "__main__":
    demo_deque(maxlen=20, iterations=1000)
