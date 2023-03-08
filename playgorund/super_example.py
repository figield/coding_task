class Base:
    pass


class Mixin(Base):
    def __init__(self):
        print("Mixin stuff")
        super(Mixin, self).__init__()


class ChildB:
    pass


class ChildC(ChildB, Mixin):  # Mixin is now between ChildB and Base
    pass


if __name__ == "__main__":
    ChildC()
    help(ChildC)  # shows that the Method Resolution Order is ChildC->ChildB->Mixin->Base
