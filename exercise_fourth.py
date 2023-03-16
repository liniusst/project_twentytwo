# A self-driven electric car needs to make a delivery from point A to point B.
# Task Nr. 4

class A:

    def say_hello(self) -> None:
        print("Hello from class A")


class B(A):

    def say_hello(self) -> None:
        print("Hello from class B")
        super().say_hello()


class C(B):

    def say_hello(self) -> None:
        print("Hello from class C")
        super().say_hello()


# hello_b = B()
# hello_b.say_hello()

hello_c = C()
hello_c.say_hello()
