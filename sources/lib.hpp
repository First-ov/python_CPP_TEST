#include <iostream>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif
    int** cpp_nd_array(int arr[3][3]);
    int cpp_int(int val);
    double cpp_double(double val);
    char *cpp_time(int year, int month, int day, int hour, int min);
    char *cpp_string(char *val);
    int *cpp_array(int *cpp_array);
    struct cpp_array_w_l{
    int *arr;
    int lenght;
    };
    struct cpp_array_of_array_w_l{
    cpp_array_w_l *arr;
    int lenght;
    };
    cpp_array_of_array_w_l * caoawl(cpp_array_w_l *arr,int lenght);
    cpp_array_w_l * cawl(int *arr, int lenght);
#ifdef __cplusplus
}
#endif