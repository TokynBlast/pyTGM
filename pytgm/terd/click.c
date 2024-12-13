#include <Python.h>
#include <tuple>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>

std::tuple<int, int> Click() {
    int fd = open("/dev/input/event0", O_RDONLY | O_NONBLOCK);
    if (fd < 0) {
        return std::make_tuple(-1, -1);
    }

    struct input_event event;
    while (true) {
        ssize_t bytes = read(fd, &event, sizeof(event));
        if (bytes < sizeof(event)) continue;

        if (event.type == EV_ABS && event.code == ABS_X) {
            close(fd);
            return std::make_tuple(event.value, event.code);
        }
    }

    close(fd);
    return std::make_tuple(-1, -1);  // No click detected
}

static PyObject* py_Click(PyObject* self, PyObject* args) {
    auto result = Click();
    return Py_BuildValue("(ii)", std::get<0>(result), std::get<1>(result));
}

static PyMethodDef methods[] = {
    {"Click", py_Click, METH_NOARGS, "Detect mouse click"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "click",       // Module name
    NULL,           // Documentation
    -1,             // Size of per-interpreter state of the module
    methods         // Method definitions
};

PyMODINIT_FUNC PyInit_click(void) {
    return PyModule_Create(&module);
}
