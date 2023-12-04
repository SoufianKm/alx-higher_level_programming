#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: object contains basics info about Python lists
 *
 * Return: 0 always
 */
void print_python_list_info(PyObject *p)
{
	int i;

	if (!p)
		return;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
