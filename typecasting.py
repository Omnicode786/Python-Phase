import typing


def main():
    print("This is a typecasting program")
    height = 9
    width = 6
    area = (width*height) / 2
    print("The area comes out to be", area)
    # now this can also be done using type casting
    print("The area comes out to be", str(area))
    # now the type of area is still float as this only changes during the runtime and area would stil remain what it was before its just a cast on top of the orignaL ONE

    print(type(area))
    print("5 * 3 = " + str(5*3))


main()
def typing1():
    # Define a variable of type str
    z: str = "Hello, world!"
    # Define a variable of type int
    x: int = 10
    # Define a variable of type float
    y: float = 1.23
    # Define a variable of type list
    list_of_numbers: typing.List[int] = [1, 2, 3]
    # Define a variable of type tuple
    tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
    # Define a variable of type dict
    dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
    # Define a variable of type set
    set_of_numbers: typing.Set[int] = {1, 2, 3}
typing1()