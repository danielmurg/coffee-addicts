"""Main module of the coffee application"""
import argparse
import os
import sys
from packaging import version


sys.path.append(os.path.realpath(__file__)[: os.path.realpath(__file__).find("src")])
from coffee_addicts import CoffeeAddicts


def is_valid_file(parser, arg):
    "Function that validates the file input: Checks if it is .csv"
    if not arg[-4:].lower() == ".csv":
        parser.error(f"The file path/url: {arg} must be from a csv file!")
    else:
        return arg


def main():
    """Main function of the coffee app"""
    parser = argparse.ArgumentParser(
        description="Returns top 3 closest coffee shops from user inputed coordinates"
    )
    parser.add_argument(
        "x_coordinate",
        metavar="x_coord",
        type=float,
        help="A float representing the x coordinate",
    )
    parser.add_argument(
        "y_coordinate",
        metavar="y_coord",
        type=float,
        help="A float representing the y coordinate",
    )
    parser.add_argument(
        "file_path",
        metavar="file_path",
        type=lambda x: is_valid_file(parser, x),
        help="An url or file path of a .CSV file",
    )
    args = parser.parse_args()
    user_python_version = str(sys.version).split(" ", maxsplit=1)[0]
    if version.parse(user_python_version) < version.parse("3.8"):
        print(
            f"""Python version required for this app is >= 3.8!
        Current users version: {user_python_version}"""
        )
        sys.exit()
    else:
        coffee_addicts = CoffeeAddicts(
            args.x_coordinate, args.y_coordinate, args.file_path
        )
        try:
            closest_coffee_shops = coffee_addicts.perform_computations()
            print(*closest_coffee_shops, sep="\n")
            sys.exit()
        except FileNotFoundError as file_not_found:
            print(str(file_not_found))
            sys.exit()


if __name__ == "__main__":
    main()
