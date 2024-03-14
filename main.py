class FileOpen:
    """
    A context manager for opening files.

    Attributes:
        file (str): The path to the file.
        mode (str): The mode in which the file is opened.
        file_content: The file object returned upon opening the file.

    Methods:
        __enter__: Enters the context and opens the file in the specified mode.
        __exit__: Exits the context and closes the file.

    """
    def __init__(self, file_name: str, mode: str = "r") -> None:
        """
        Initializes a FileOpen object.

        Args:
            file_name (str): The path to the file to be opened.
            mode (str, optional): The mode in which the file should be opened. Default is 'r'
                (read mode).
        """
        self.file = file_name
        self.mode = mode

    def __enter__(self) -> any:
        """
        Enters the context and opens the file in the specified mode.

        Returns:
            Any: The file object returned upon opening the file.
        """
        self.file_content = open(self.file, self.mode)
        return self.file_content

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exits the context and closes the file.

        Args:
            exc_type: The type of exception (if any) that occurred within the context.
            exc_val: The exception value.
            exc_tb: The traceback.
        """
        self.file_content.close()


def main(file_name, mode = "r") -> None:
    with FileOpen(file_name, mode) as file:
        context = file.read()
    print(context)


if __name__ == "__main__":
    main("test.txt")

