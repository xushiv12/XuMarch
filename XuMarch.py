def o(a):
    print(a)
def i(a):
    b=input(a)
    return b
def n(a):
    return int(a)
def c1(a):
    exec("print("+a+")")
def c2(a):
    exec("input("+a+")")
def rdfile(a):
    with open(a,"r",encoding="utf-8") as r:
        return r.read()
def wtfile_w(a,b):
    with open(a,"w",encoding="utf-8") as f:
        f.write(b)
def wtfile_a(a,b):
    with open(a,"a",encoding="utf-8") as f:
        f.write(b)
code=input("Enter filename>>>")
rr=""
with open(code,"r",encoding="utf-8") as r:
    rr=r.read()
rrr=rr.replace("fc","def").replace("value=","return ").replace("f/c","fc").replace("value/=","value=").replace("/@","/").replace("@/","@")
exec(rrr)