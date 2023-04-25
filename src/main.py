
is_main = (__name__ == '__main__')


def main(): print("Hello, world :)")


# ENTRY.
(
    lambda : 
    main() if is_main 
    else exit(0)
)()


