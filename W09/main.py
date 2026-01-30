class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} is {self.age} years old."
def main():
    my_dog = Dog("conne",3)
    neighbor_dog = Dog("benet",2)
    print(my_dog)
    print(neighbor_dog)


if __name__ == "__main__":
    main()
