# python_CPP_TEST
## Задание 1
В этом задании выводятся целые и дробные числа 

Код C++:
```
int cpp_int(int val) {
    return val;
}
double cpp_double(double val) {
    return val;
}
```

Код Python:
```
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
```

![Image1](https://cloud.paov.ru/index.php/s/QYTMryRFmsJJA4B/preview)

## Задание 2
В этом задании выводятся строки и даты

Код C++:
```
char *cpp_string(char *val) {
    return val;
}
char *cpp_time(int year, int month, int day, int hour, int min){
    std::tm tm;
    tm.tm_year = year-1900;
    tm.tm_mon = month-1;
    tm.tm_mday = day;
    tm.tm_hour = hour;
    tm.tm_min = min;
    tm.tm_isdst = 0;
    std::time_t t = std::mktime(&tm);
    char mbstr[100];
    std::strftime(mbstr, sizeof(mbstr), "%D %R", std::localtime(&t));
    std::cout<<"";
    return mbstr;
}
```

Код Python:
```
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
```

![Image2](https://cloud.paov.ru/index.php/s/QYTMryRFmsJJA4B/preview)

## Задание 3
В этом задании выводится массив 3*3

Код C++:
```
int** cpp_nd_array(int arr[3][3]){
    int ** aoarray;
    aoarray = new int*[3];
    for(int i=0;i<3;i++)
    {aoarray[i] = new int[3];
    for(int j=0;j<3;j++)
    {
    aoarray[i][j]=arr[i][j];
    }
    }
    return aoarray;
}
```

Код Python:
```
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
```

![Image3](https://cloud.paov.ru/index.php/s/gKNNcpbQXEZzyRt/preview)

## Задание 4
В этом задании выводится структура для работы с динамическими массивами

Структуры C++:
```
    struct cpp_array_w_l{
    int *arr;
    int lenght;
    };
    struct cpp_array_of_array_w_l{
    cpp_array_w_l *arr;
    int lenght;
    };
```
Классы Python:
```
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
```

Код C++:
```
cpp_array_w_l * cawl(int *arr, int lenght){
    cpp_array_w_l *res = new cpp_array_w_l;
    res->lenght=lenght;
    int * array;
    array = new int [lenght];
    for(int i=0;i<lenght;i++)
    {
    array[i]=arr[i];
    }
    res->arr=array;
    return res;
}
cpp_array_of_array_w_l * caoawl(cpp_array_w_l *arr,int lenght){
    cpp_array_of_array_w_l *res = new cpp_array_of_array_w_l;
    res->lenght = lenght;
    cpp_array_w_l * array;
    array = new cpp_array_w_l [lenght];
    for(int i=0;i<lenght;i++)
    {
    array[i].arr = cawl(arr[i].arr, arr[i].lenght)->arr;
    array[i].lenght = cawl(arr[i].arr, arr[i].lenght)->lenght;
    for(int j=0;j<arr[i].lenght;j++)
    {

//    std::cout<<array[i].arr[j]<<' ';
    }
//    std::cout<<'\n';
    }
    res->arr=array;
    return res;
}
```

Код Python:
```
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
```

![Image4](https://cloud.paov.ru/index.php/s/jGCaWXKPdYbibyW/preview)
