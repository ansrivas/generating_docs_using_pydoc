class TestClass(object):
    """Test class is a great class, which makes everything great.

    Args:
        arg1 (int): Hi I am arg1
        arg2 (int): Hi I am arg2
    """

    def __init__(self, arg1, arg2):
        """This is init docs."""
        self.arg1 = arg1
        self.arg2 = arg2


    def func1(self, arg1):
        """This is func1.

        Args:
            arg1 (int): Hi this is func1 arg1

        Returns:
            something (str): Return is something of type string
        """

        return "something"
