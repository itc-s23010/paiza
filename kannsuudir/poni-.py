results = [input().split() for _ in range(5)]

if all(d == e for d, e in results):
    print("OK")
else:
    print("NG")
