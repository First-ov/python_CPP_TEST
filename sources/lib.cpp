#include "lib.hpp"
#include <iostream>
#include <sstream>
#include <iomanip>
#include <ctime>

int cpp_int(int val) {
    return val;
}
double cpp_double(double val) {
    return val;
}

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


