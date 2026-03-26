# pipx_test/cli.py
import sys

def main():
    print("Hello from pipx_test CLI!")
    if len(sys.argv) > 1:
        print("Arguments passed:", sys.argv[1:])

if __name__ == "__main__":
    main()
