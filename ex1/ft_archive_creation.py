import sys
import typing


def ft_ancient_text(filename: str) -> str | None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")  
    except OSError as e:  
        print(f"Error opening file '{filename}': {e}")
        return None

    try:
        content: str = file.read()
        print("---")
        print()
        print(content)
        return content
    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    finally:
        file.close()
        print("\n---")
        print(f"File '{filename}' closed")


def transformation_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    if not lines:
        return ""
    transformed: lines[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed) + "\n"


def save_transformation(filename: str, transformed: str) -> None:
    print(f"Saving data to '{filename}'")
    dest_file: typing.IO[str] | None = None

    try:
        dest_file = open(filename, "w")
        dest_file.write(transformed)
        print(f"Data saved in file '{filename}'")
    except OSError as e:
        print(f"Error saving file '{filename}': {e}")
    finally:
        if dest_file is not None:
            dest_file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    
    content: str | None = ft_ancient_text(sys.argv[1])
    if content is None:
        return

    transformed: str = transformation_data(content)
    print("\nTransform data:")
    print("---")
    print(transformed)
    print("---")

    filename: str = input("Enter new file name (or empty): ").strip()

    if not filename:
        print("Not saving data")
        return
    save_transformation(filename, transformed)    


if __name__ == "__main__":
    main()
