"""Module which contains all the test for the coffee store application"""
from src.coffee_addicts import CoffeeAddicts


class Tests:
    """Test class"""

    def test_distance_function(self):
        """Function that tests the distance function"""
        coffee_data_good = CoffeeAddicts(
            47.6,
            -122.4,
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        outputs_good = [
            "Starbucks Seattle2,0.0645",
            "Starbucks Seattle,0.0861",
            "Starbucks SF,10.0793",
        ]

        coffee_data_bad = CoffeeAddicts(47.6, -122.4, "invalid_path.csv")
        outputs_bad = -1

        assert (
            coffee_data_good.compute_distances(),
            coffee_data_bad.compute_distances(),
        ) == (outputs_good, outputs_bad)

    def test_x_coordinate_validation(self):
        """Function that test the validation of the first argument
        (x coordinate inputed by the user)"""
        coffee_data_good = CoffeeAddicts(
            47.6,
            -122.4,
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        output_good = [None, None, None]

        coffee_data_bad = CoffeeAddicts(
            "sda",
            -122.4,
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        output_bad = [
            """Invalid input for x coordinate: sda.
            Input must be a float type number (i.e. 20.33)""",
            None,
            None,
        ]

        assert (
            coffee_data_good.validate_input(),
            coffee_data_bad.validate_input(),
        ) == (output_good, output_bad)

    def test_y_coordinate_validation(self):
        """Function that test the validation of the second argument
        (y coordinate inputed by the user)"""
        coffee_data_good = CoffeeAddicts(
            47.6,
            -122.4,
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        output_good = [None, None, None]

        coffee_data_bad = CoffeeAddicts(
            47,
            "sda",
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        output_bad = [
            None,
            """Invalid input for y coordinate: sda.
            Input must be a float type number (i.e. 20.33)""",
            None,
        ]

        assert (
            coffee_data_good.validate_input(),
            coffee_data_bad.validate_input(),
        ) == (output_good, output_bad)

    def test_file_path_validation(self):
        """Function that test the validation of the third argument
        (file path/URL inputed by the user)"""
        coffee_data_good = CoffeeAddicts(
            47.6,
            -122.4,
            "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv",
        )
        output_good = [None, None, None]

        coffee_data_bad = CoffeeAddicts(47, -122, "invalid_file")
        output_bad = [
            None,
            None,
            """Invalid input for file_path: invalid_file.
            Input must be a csv file.""",
        ]

        assert (
            coffee_data_good.validate_input(),
            coffee_data_bad.validate_input(),
        ) == (output_good, output_bad)

    def run_tests(self):
        """Main function for test runs"""
        try:
            self.test_x_coordinate_validation()
            self.test_y_coordinate_validation()
            self.test_file_path_validation()
            self.test_distance_function()
        except AssertionError:
            return -1
        return 0
