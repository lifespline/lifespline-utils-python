"""This is the documentation of the demo module.
"""

class Demo:
    """This is the documentation of the Demo class.
    """

    def __init__(self) -> None:
        pass

    def demo(self):
        """This is the documentation of the constructor of the Demo class.

        This is a pointer to the OtherDemo class :class:`OtherDemo`

        Usage:

        .. doctest::

            >>> from demo import Demo
            >>> demo = Demo.demo()

        .. note::

            this is a note to the documentation
        """
        __init__(self)

class OtherDemo:
    """This is the documentation for the OtherDemo class.
    """

    def __init__(self) -> None:
        pass

    def other_demo(self):
        """This is the documentation of the constructor of the OtherDemo class.

        This is a pointer to the Demo class :class:`Demo`

        Usage:

        .. doctest::

            >>> from demo import OtherDemo
            >>> demo = OtherDemo.demo()

        .. note::

            this is a note to the documentation
        """
        __init__(self)
