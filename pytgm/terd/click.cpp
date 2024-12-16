#include <Python.h>
#include <tuple>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>
#include <stdexcept>
#include <iostream>

// Function to detect a mouse click and return the coordinates
std::tuple<int, int> Click() {
    int fd = open("/dev/input/event0", O_RDONLY | O_NONBLOCK);
    if (fd < 0) {
        throw std::runtime_error("Failed to open input device: /dev/input/event0");
    }

    struct input_event event;
    while (true) {
        ssize_t bytes = read(fd, &event, sizeof(event));
        if (bytes < static_cast<ssize_t>(sizeof(event))) {
            continue;
        }

        if (event.type == EV_ABS && event.code == ABS_X) {
            close(fd);
            return std::make_tuple(event.value, event.code);
        }
    }

    close(fd);
    return std::make_tuple(-1, -1);  // No click detected
}

// Python wrapper function for Click()
static PyObject* py_Click(PyObject* self, PyObject* args) {
    try {
        auto result = Click();
        return Py_BuildValue("(ii)", std::get<0>(result), std::get<1>(result));
    } catch (const std::exception& e) {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    }
}

// Method definitions for the Python module
static PyMethodDef methods[] = {
    {"Click", py_Click, METH_NOARGS, "Detect mouse click and return coordinates"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "click",       // Module name
    NULL,          // Documentation
    -1,            // Size of per-interpreter state of the module
    methods        // Method definitions
};

// Module initialization function
PyMODINIT_FUNC PyInit_click(void) {
    return PyModule_Create(&module);
}
