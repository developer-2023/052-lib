def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# it runs main() only if called out by command line
# it doesn't run main() if called out from other running program
if __name__ == "__main__":
    main()

