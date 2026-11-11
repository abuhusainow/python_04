import sys
import typing


def ft_ancient_text(user_input: list[str]) -> None:
    file: typing.IO[str] | None = None

    if len(user_input) != 2:
        print(f"Usage: {user_input[0]} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{user_input[1]}'")

    try:
        file = open(user_input[1], "r")
        print("---\n")
        print(f"{file.read()}")
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{user_input[1]}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{user_input[0]}' closed")


if __name__ == "__main__":
    ft_ancient_text(sys.argv)
