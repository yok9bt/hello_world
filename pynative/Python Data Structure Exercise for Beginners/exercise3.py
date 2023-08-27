sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# # First try
# for x in range(0,len(sample_list),3):
#     l = sample_list[x:x+3]
#     print(l)
#     l.reverse()
#     print(l)

for x in range(0,len(sample_list),3):
    s = slice(x, x+3)
    print(sample_list[s])
    print(list(reversed(sample_list[s])))
