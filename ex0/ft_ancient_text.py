import sys
import typing


def ft_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")  # r is default for open()
    except OSError as e:  # catches both FileNotFound- and Permissionerror
        print(f"Error opening file '{filename}': {e}")
        return

    try:
        content: str = file.read()
        print("---")
        print()
        print(content)
    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
    finally:
        file.close()
        print("\n---")
        print(f"File '{filename}' closed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        ft_ancient_text(sys.argv[1])
