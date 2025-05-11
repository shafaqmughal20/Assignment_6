# Class A with a method show()
class A:
    def show(self):
        print("Class A: show() method")

# Class B inheriting from A and overriding show()
class B(A):
    def show(self):
        print("Class B: show() method")

# Class C inheriting from A and overriding show()
class C(A):
    def show(self):
        print("Class C: show() method")

# Class D inheriting from both B and C
class D(B, C):
    pass

# Create an object of class D
d = D()
d.show()  # Call the show() method from D

# Observe MRO
print("\nMRO of class D:", D.mro())
