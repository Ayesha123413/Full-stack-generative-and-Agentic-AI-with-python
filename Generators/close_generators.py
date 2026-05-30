def local_chai():
    yield "masla chai"
    yield "lemon tea"

def import_chai():
    yield "green tea"
    yield "black tea"


def full_menu():
    yield from local_chai()
    yield from import_chai()


for chai in full_menu():
    print(chai)


def chai_order():
    try:
        yield "waiting for chai order"

    except:
        print("stall is closed")

stall=chai_order()
print(next(stall))  # Start the generator and get the initial message
stall.close()