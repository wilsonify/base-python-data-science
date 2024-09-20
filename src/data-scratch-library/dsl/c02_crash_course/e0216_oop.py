class CountingClicker:
    """A simple counting clicker."""

    def __init__(self, count=0):
        """Initialize the clicker with a count (default is 0)."""
        self.count = count

    def __repr__(self):
        """Return a string representation of the clicker."""
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """Increment the count by num_times (default is 1)."""
        self.count += num_times

    def read(self):
        """Return the current count."""
        return self.count

    def reset(self):
        """Reset the count to 0."""
        self.count = 0

class NoResetClicker(CountingClicker):
    """A counting clicker that cannot be reset."""

    def reset(self):
        """Override reset to do nothing."""
        pass
