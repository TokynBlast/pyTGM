#include <Python.h>
#include <tuple>

#ifdef _WIN32
#include <io.h>     // For Windows file operations
#include <fcntl.h>
#else
#include <unistd.h> // For POSIX systems
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>
#endif

std::tuple<int, int> Click() {
#ifdef _WIN32
    // Windows-specific implementation (you'll need to customize this)
    // Example: return a dummy value as `/dev/input/event0` is not valid on Windows.
    return std::make_tuple(-1, -1);
#else
    // POSIX implementation
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
#endif
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
