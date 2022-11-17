# True, False

def check(x) -> bool:
    print(f"({x} > 0) is {bool(x > 0)}")
    return x > 0


falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), '']
# for e in falsy:
#     print(bool(e))
if check(1) and check(2) and check(-3) and check(6):
    print("YES")
print('='*10)
if check(3) or check(0) or check(-3) or check(6):
    print("YES")