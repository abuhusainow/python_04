import sys
import typing


def recover_ancient_text(filename: str) -> None:
    """Read and display the contents of a specified file.

    Parameters:
        filename (str): Path to the target archive file.
    """
    # 1. Output the mandatory headers as specified in the subject output format.
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    # 2. Open the file inside an isolated try-except block.
    # We do NOT open the file outside try/except because if the file does
    # not exist or permissions are denied, open() raises an OSError.
    try:
        # open() creates an operating system file descriptor and returns
        # a stream object. We annotate it with typing.IO[str].
        vault: typing.IO[str] = open(filename, "r")
    except OSError as err:
        # If open() fails, no file object is created.
        # We output the exact exception message and return immediately.
        # Calling vault.close() here would raise an UnboundLocalError.
        print(f"Error opening file '{filename}': {err}")
        return

    # 3. Read the stream and guarantee resource closure with try-finally.
    # The 'with' statement is explicitly forbidden until Exercise 3.
    # Therefore, try-finally is the standard idiom to ensure the file stream
    # is ALWAYS closed, even if an unexpected error occurs while reading.
    try:
        content: str = vault.read()
        # end="" prevents print() from appending a duplicate newline,
        # preserving the exact line structure of the original file.
        print(content, end="")
    except OSError as err:
        print(f"Error reading file '{filename}': {err}")
    finally:
        # io.close() flushes and releases the file descriptor back to the OS.
        vault.close()
        print(f"File '{filename}' closed.")


def main() -> None:
    """Validate CLI arguments and initiate the archive recovery procedure."""
    # sys.argv contains the command-line tokens passed to Python:
    # sys.argv[0] is the script name ('ft_ancient_text.py')
    # sys.argv[1] is the expected argument (<file>)
    # If the count is not exactly 2, display usage instructions and exit.
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    # Pass the first user-provided argument into the recovery function.
    recover_ancient_text(sys.argv[1])


# Ensure code only executes when run directly from the command line,
# not when imported as a module.
if __name__ == "__main__":
    main()