class P:
    a=10
    def __init__(self) -> None:
        self.b=30
    def m1(self):
        print("parrent instance method")
    @classmethod
    def m2(cls):
        print("parrent class method")
    @staticmethod
    def m3():
        print("parrent static method")
class C(P):
    a=888
    def __init__(self) -> None:
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
c=C()