"""Module used for identyfing the three closest cofffee stores from a user"""
import math
from typing import List
import pandas as pd


class CoffeeAddicts:
    """Coffee addicts class that validates the input and coputes the
    distance between the user and all the coffee shops"""

    def __init__(self, coord_x, coord_y, file_path) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.file_path = file_path

    def validate_input(self) -> List:
        """Function that validates the inputs"""
        try:
            float(self.coord_x)
            error_message_coord_x = None
        except ValueError:
            error_message_coord_x = f"""Invalid input for x coordinate: {self.coord_x}.
            Input must be a float type number (i.e. 20.33)"""

        try:
            float(self.coord_y)
            error_message_coord_y = None
        except ValueError:
            error_message_coord_y = f"""Invalid input for y coordinate: {self.coord_y}.
            Input must be a float type number (i.e. 20.33)"""

        if self.file_path[-4:].lower() == ".csv":
            error_message_file_path = None
        else:
            error_message_file_path = f"""Invalid input for file_path: {self.file_path}.
            Input must be a csv file."""

        return [error_message_coord_x, error_message_coord_y, error_message_file_path]

    def compute_distances(self) -> List:
        """Function that computes the distance"""
        try:
            coffe_shops_df = pd.read_csv(
                self.file_path, header=None, names=["Name", "X Coordinate", "Y Coordinate"]
            )
        except FileNotFoundError:
            return -1
        coffe_shops_df["distance"] = coffe_shops_df[
            ["Y Coordinate", "X Coordinate"]
        ].apply(
            lambda x: math.dist(
                [float(self.coord_x), float(self.coord_y)], [x["X Coordinate"], x["Y Coordinate"]]
            ),
            axis=1,
        )
        coffe_shops_df.sort_values(by=["distance"], inplace=True)
        coffe_shops_df.reset_index(drop=True, inplace=True)

        closest_coffee_shops = []
        for i in range(0, 3):
            closest_coffee_shops.append(
                str(coffe_shops_df.at[i, "Name"])
                + ","
                + str(round(coffe_shops_df.at[i, "distance"], 4))
            )

        return closest_coffee_shops
