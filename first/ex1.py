inp = "one=1 two=2 three=3"
lst = list(inp.split())
tmp_lst = [y.split("=") for y in lst]
for i in range(len(tmp_lst)):
     tmp_lst[i][1] = int(tmp_lst[i][1])
d = dict(tmp_lst)
print(*sorted(d.items()))