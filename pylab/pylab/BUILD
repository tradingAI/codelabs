package(default_visibility = ["//visibility:public"])

py_library(
    name = "py_default_lib",
    srcs = [
        "helloworld.py",
        "np_random.py",
    ],
    deps = [
        "//pylab/common:py_default_lib",
    ],
)

py_test(
    name = "helloworld_test",
    srcs = ["helloworld_test.py"],
    deps = [
        ":py_default_lib",
    ],
)

py_test(
    name = "np_random_test",
    srcs = ["np_random_test.py"],
    deps = [
        ":py_default_lib",
    ],
)
