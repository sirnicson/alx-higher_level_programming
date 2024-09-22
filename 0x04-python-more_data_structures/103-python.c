#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list.
 * @p: A PyObject pointer to the Python list.
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid PyObject: not a list\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the list: %zd\n", size);
    printf("[*] Allocated: %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: A PyObject pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid PyObject: not a bytes object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[*] Python bytes info\n");
    printf("[*] Size of the bytes: %zd\n", size);
    printf("[*] First %zd bytes: ", size > 10 ? 10 : size);
    for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
    {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
