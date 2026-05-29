
def get_chai_list():
    return ["cup1 ", "cup2 ", "cup3 ", "cup4 "]

def get_chai_generator():
    yield "cup1 "
    yield "cup2 "
    yield "cup3 "
    yield "cup4 "

chai_list = get_chai_list()
print(chai_list)    

chai_generator = get_chai_generator()
print(chai_generator, next(chai_generator), next(chai_generator))