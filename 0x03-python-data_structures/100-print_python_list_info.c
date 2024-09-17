#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t i;
    Py_ssize_t size;
    Py_ssize_t allocated;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Provided object is not a Python list\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
