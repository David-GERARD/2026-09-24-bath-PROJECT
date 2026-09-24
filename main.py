"""GDP data helper module."""

import argparse
import pandas as pd


def get_subset_of_gdp_data(countries, years):
    """Get a subset of GDP data for selected countries and years.

    Args:
        countries: Country names to filter.
        years: Years to filter.

    Returns:
        None
    """
    _ = pd
    _ = countries
    _ = years
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
