def add_sprinkles(func):
    func(flavour)
    def wrapper(flavour, sprinkles):
        if sprinkles=="y":
            print("Sprinkles have been added!")
    return wrapper
@add_sprinkles
def get_ice_cream(flavour):
    print(flavour.capitalize()+"ice cream has been served!")

flav=input("Enter flavour:")
sprinkles=input("Do you want sprinkles(y/n):")

get_ice_cream(flav)