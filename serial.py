"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Make a new generator, beginning with start."""
        self.start = start
        self.current = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} next={self.current}>"

    def generate(self):
        """Generate the current serial and update the next serial."""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Reset number to original start"""
        self.current = self.start
