#TODO: add Google-Style docsting here

import argparse
import pandas as pd


def get_subset_of_gdp_data(countries, years):
    #TODO: add Google-Style docsting here
    #TODO: load data, select countries, select years based on column name
    #TODO: what to do when country does not exist?
    #TODO: what to do when year not in data?
    return None


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--countries", nargs="+", required=True)
    parser.add_argument("--years", nargs="+", type=int, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    get_subset_of_gdp_data(args.countries, args.years)
