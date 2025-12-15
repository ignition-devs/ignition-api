# ARCHIVED REPOSITORY NOTICE

This repo is a mirror of what used to be the `jython` branch under [`Ignition`](https://github.com/thecesrom/Ignition), and it is now read-only because of the following reasons:

1. Issues in PyCharm when Jython is set as the project interpreter
    1. "ImportError: No module named _shaded_thriftpy" running console with Jython ([PY-44759](https://youtrack.jetbrains.com/issue/PY-44759))
    1. _shaded_thriftpy.parser.exc.ThriftParserError with Jython 2.7.1 as intepreter ([PY-50491](https://youtrack.jetbrains.com/issue/PY-50491))
1. Issue in Jython when trying to import modules under `com.inductiveautomation`
    1. Jython 2.7.2 ImportError: No module named <my_package_name> when running `import com.<my_package_name>` ([jython#131](https://github.com/jython/jython/issues/131))
