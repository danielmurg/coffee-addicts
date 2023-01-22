"""Main module of the coffee application"""
import sys

from tests.test import Tests
from coffee_addicts import CoffeeAddicts


def check_error(error):
    """Function that prints and checks if error occured during input validation"""
    if error is not None:
        print(error)
        return 1
    return 0


def main():
    """Main function of the coffee app"""
    args = sys.argv[1:]
    user_python_version = sys.version
    py_version = float(user_python_version[:3])
    if py_version < 3.8:
        print(
            f"""Python version required for this app is >= 3.8!
        Current users version: {user_python_version}"""
        )
    else:
        if len(args) != 3:
            print("Exactly 3 arguments required!")
        else:
            tests = Tests()
            if tests.run_tests() == -1:
                print("Program does not work properly!")
            else:
                coffee_addicts = CoffeeAddicts(args[0], args[1], args[2])
                errors_list = coffee_addicts.validate_input()
                total_errors = 0
                for error in errors_list:
                    total_errors += check_error(error)
                if total_errors == 0:
                    closest_coffee_shops = coffee_addicts.compute_distances()
                    if closest_coffee_shops == -1:
                        print(
                            f"{args[2]} is not a valid url/path or the file is corrupted."
                        )
                    else:
                        print(*closest_coffee_shops, sep="\n")


if __name__ == "__main__":
    main()
