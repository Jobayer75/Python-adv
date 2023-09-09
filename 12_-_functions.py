# Functions are defined by using the "def" keyword.
def say_hi(name, age):
    print("Hello " + name + ", your age is " + age + "!")


say_hi("Jobayer", "25")


# Functions like "say_hi" can even receive an integer if it is properly converted.
def say_hi(name, age):
    print("Hello " + name + ", your age is " + str(age) + "!")


say_hi("Hasina", 70)
