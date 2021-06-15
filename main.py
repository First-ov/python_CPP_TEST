import ctypes
cpplib = ctypes.CDLL('lib.so')


def zad11():
    cpplib.cpp_int.restype = ctypes.c_int
    cpplib.cpp_int.argtypes = [ctypes.c_int, ]
    print('Enter number: \n')
    a = input()
    print(cpplib.cpp_int(int(a)))


def zad12():
    cpplib.cpp_double.restype = ctypes.c_double
    cpplib.cpp_double.argtypes = [ctypes.c_double, ]
    print('Enter number: \n')
    a = input()
    print(cpplib.cpp_double(float(a)))


def zad21():
    cpplib.cpp_string.restype = ctypes.c_char_p
    cpplib.cpp_string.argtypes = [ctypes.c_char_p, ]
    print('Enter string: \n')
    a = input()
    print(cpplib.cpp_string(a.encode('utf-8')).decode('utf-8'))


def zad22():
    cpplib.cpp_time.restype = ctypes.c_char_p
    cpplib.cpp_time.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ]
    print('Enter year month day hour min: \n')
    a = input()
    data = a.split()
    b = cpplib.cpp_time(int(data[0]),
                    int(data[1]),
                    int(data[2]),
                    int(data[3]),
                    int(data[4])
                    )
    str=b
    print(repr(str)[2:-1].encode("utf-8").decode("utf-8"))


def zad3():
    cpplib.cpp_nd_array.argtypes = ((ctypes.c_int * 3) * 3),
    cpplib.cpp_nd_array.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
    list0 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    arr = ((ctypes.c_int * 3) * 3)()
    for i in range(3):
        print('Enter 3 integer: \n')
        a = input()
        data = a.split()
        list0[i] = [int(data[0]), int(data[1]), int(data[2])]
    for i in range(3):
        for j in range(3):
            arr[i][j] = list0[i][j]
    b = cpplib.cpp_nd_array(arr)
    for i in range(3):
        for j in range(3):
            list0[i][j]=b[i][j]
    print(list0)


class cpp_array_w_l(ctypes.Structure):
    _fields_ = [('arr', ctypes.POINTER(ctypes.c_int)),
                ('lenght', ctypes.c_int)]

    def __init__(self, arr, lenght):
        self.lenght = lenght
        self.arr = arr


class cpp_array_of_array_w_l(ctypes.Structure):
    _fields_ = [('arr', ctypes.POINTER(cpp_array_w_l)),
                ('lenght', ctypes.c_int)]

    def __init__(self, arr, lenght):
        self.lenght = lenght
        self.arr = arr


def zad4():
    cpplib.caoawl.restype = ctypes.POINTER(cpp_array_of_array_w_l)
    cpplib.caoawl.argtypes = [ctypes.POINTER(cpp_array_w_l), ctypes.c_int]
    list = [[1], [1, 2], [1, 2, 3]]
    cawls = []
    print('Enter number of strings: \n')
    a = input()
    numofs=int(a)
    for i in range(0, numofs):
        print('Enter integers: \n')
        a = input()
        data = a.split()
        list0=[]
        for d in data:
            list0.append(int(d))
        cawls.append(
            cpp_array_w_l((ctypes.c_int * len(list0))(*list0), len((ctypes.c_int * len(list0))(*list0)))
        )
    pc = (cpp_array_w_l * numofs)(*cawls)
    b = cpplib.caoawl(pc, numofs)
    lenght=b.contents.lenght
    for i in range(lenght):
        lenght1=b.contents.arr[i].lenght
        for j in range(lenght1):
            ar=b.contents.arr[i].arr[j]
            print(str(ar)+' ',end='')
        print('')



print('Enter number of problem or enter 0 to exit:\n')
inp = int(input())
while inp !=0:
    if inp==1:
        print('Enter 1 for int 2 for double 0 to exit:\n')
        inp = int(input())
        if inp == 1:
            zad11()
        elif inp == 2:
            zad12()
        elif inp == 0:
            pass
    elif inp==2:
        print('Enter 1 for string 2 for datetime 0 to exit:\n')
        inp = int(input())
        if inp == 1:
            zad21()
        elif inp == 2:
            zad22()
        elif inp == 0:
            pass
    elif inp==3:
        zad3()
    elif inp==4:
        zad4()
    print('Enter number of problem or enter 0 to exit:\n')
    inp = int(input())