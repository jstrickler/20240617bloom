from pprint import pprint  # import prettyprint function

spam = 42  # global variable
ham = 'Smithfield'


def eggs(fruit):  # function parameters are local
    name = 'Lancelot'  # local variable
    idiom = 'swashbuckling'  # local variable
    print("Globals:")
    pprint(globals())  # globals() returns dict of all globals
    print()
    print("Locals:")
    pprint(locals())  # locals() returns dict of all locals


eggs('mango')

g = globals()
g['animal'] = "wombat"  # create a new variable, same as     animal = "wombat"

print(f"{animal = }")

g['bark'] = lambda : print("woof woof")

bark()
