steps, ns = 30000000,[1,3,2] 
last, c = ns[-1], {n: i+1 for i, n in enumerate(ns)}
for i in range(len(ns), steps):
    c[last], last = i, i - c.get(last, i)
print(last)
