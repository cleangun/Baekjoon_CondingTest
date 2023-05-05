import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print("*")
    exit(0)

star = [" "] * (2**n)
star[0] = "*"
def print_star(star):
    for idx in range(len(star)):
        if "*" not in star[idx:]:
            break
        if star[idx] == "*":
            print("*",end="")
        else:
            print(" ",end="")
    print()

def make_star(star,level):
    if level >= (2**n):
        return
    fill = star.copy()
    for idx in range(len(star)):
        if star[idx] == "*":
            fill[idx+1] = "*"
    passlist = ["*"]
    for idx in range(1,len(fill)):
        if ((fill[idx] == "*") and (fill[idx-1] == " ")) or \
            ((fill[idx] == " ") and (fill[idx-1] == "*")):
                passlist.append("*")
        else:
            passlist.append(" ")
    make_star(passlist,level+2)
    print_star(fill)
    print_star(star)
    return


make_star(star,1)