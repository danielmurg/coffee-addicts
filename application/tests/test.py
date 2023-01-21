from src.CoffeeAddicts import CoffeeAddicts

def test_distance_function():
    inputs = CoffeeAddicts(47.6,-122.4, r'C:\Users\danie\OneDrive\Desktop\Git-repos\coffee-addicts\coffee_shops_Coding_C.csv')
    outputs = ['Starbucks Seattle2,0.0645', 'Starbucks Seattle,0.0861', 'Starbucks SF,10.0793']

    assert inputs.compute_distances() == outputs

