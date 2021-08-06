class test:
    def mark(self):
        print("mark")


class maths:
    def formula(self):
        print("maths formula")


class physics(test,maths):
    def phy(self):
        print("phsics needs maths and test")


p=physics()
p.phy()
p.formula()
p.mark()

print("hello",input())