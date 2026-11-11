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
        content: str = file.read()
        print(f"{content}")
        print("\n---")
    except OSError as e:
        print(
            "[STDERR] Error opening file",
            f"'{user_input[1]}': {e}", file=sys.stderr
        )
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{user_input[1]}' closed")

    new_content: str = transform(content)

    print("\nTransform data:")
    print("---\n")
    print(new_content)
    print("\n---")

    print("Enter new file name (or empty): ", end="", flush=True)
    new_file: str = sys.stdin.readline().strip()
    if new_file == "":
        print("Not saving data.")
        return
    save_content(new_file, new_content)


def transform(content: str) -> str:
    lst_content: list[str] = content.splitlines()
    if not lst_content:
        return ""
    new_content: list[str] = [f"{line}#" for line in lst_content]
    return "\n".join(new_content)


def save_content(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")

    new_file: typing.IO[str] | None = None

    try:
        new_file = open(filename, "w")
        new_file.write(content)
        print(f"Data saved in file '{filename}'")
    except OSError as e:
        print(f"[STDERR] Error saving to {filename}: {e}", file=sys.stderr)
    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    ft_ancient_text(sys.argv)
