def secure_archive(
        filename: str,
        action: str = "read",
        content: str = ""
) -> tuple[bool, str]:
    mode: str = "w" if action == "write" else "r"
    try:
        with open(filename, mode) as file:
            if action == "write":
                file.write(content)
                return (True, "Content successfully written to file")
            return (True, file.read())
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not/existing/file.txt"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    read_result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(read_result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if read_result[0] is True:
        print(secure_archive("new_fragment.txt", "write", read_result[1]))


if __name__ == "__main__":
    main()