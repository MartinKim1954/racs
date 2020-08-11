class A:
    def a(self):
        self.a = 1
        print("I'm A.a")

class B(A):
    def b(self):
        self.b = 2
        print("I'm B.b")

class C(B):
    def c(self):
        self.c = 3
        print("I'm C.c")


Z = C()
Z.a()
Z.b()
Z.c()
print(Z.a)
print(Z.b)
print(Z.c)
