N, M = map(int, input().split())
answer = []
ever_listened = set()
ever_seen = set()
for _ in range(N):
    ever_listened.add(input())

for _ in range(M):
    ever_seen.add(input())

ever_seen_listend = ever_listened.intersection(ever_seen)

print(len(ever_seen_listend))
answer = sorted(ever_seen_listend)
for name in answer:
    print(name)