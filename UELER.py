import math
for a in range(10):
    for b in range(10):
        for c in range(10):
            d = math.sqrt(a**2 + b**2)
            e = math.sqrt(a**2 + c**2)
            f = math.sqrt(b**2 + c**2)
            print(d, e, f)
            d = str(d).split(".")[0]
            e = str(d).split(".")[0]
            f = str(d).split(".")[0]
            print(d, e, f)
            if d[1] == "0" and e[1] == "0" and f[1] == "0":
                print("["+str(a)+","+str(b)+","+str(c)+"] --> ["+d+","+e+","+f+"]")
    
