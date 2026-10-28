import sys
import typing

def ft_ancient_text(sys_input: list[str]) -> None:
    try:
        file = sys_input[1]
        try:
            print(f"Accessing file '{file}’")
            file_out = open(file)
            print("=== Cyber Archives Recovery ===")
            print("Accessing file '{file_out}'\n---")
            print(file_out)
        except FileNotFoundError:
            print(f"Error opening file '{file} <file>'")
    except IndexError:
        print(f"Usage: {sys_input[0]}")
    


if __name__ == "__main__":
    ft_ancient_text(sys.argv)