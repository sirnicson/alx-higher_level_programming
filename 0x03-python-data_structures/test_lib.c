#include <Python.h>
#include <stdio.h>

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Example code to test Python functions or modules
    PyObject *pName = PyUnicode_DecodeFSDefault("test_module");
    PyObject *pModule = PyImport_Import(pName);
    Py_XDECREF(pName);

    if (pModule != NULL) {
        printf("Module loaded successfully.\n");
        // Call a function from the module if necessary
    } else {
        PyErr_Print();
        fprintf(stderr, "Failed to load module\n");
    }

    // Finalize the Python interpreter
    Py_Finalize();
    return 0;
}
