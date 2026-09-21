"""Practice entrypoint for GDP subset exercises."""

import pandas as pd


def get_subset_of_gdp_data(countries, years):
    """Return a subset of GDP data for selected countries and years.

    Args:
        countries: Country names to include.
        years: Year values to include.

    Returns:
        None while the exercise implementation is pending.
    """
    _ = pd
    _ = countries
    _ = years
    return None


if __name__ == "__main__":
    get_subset_of_gdp_data(["France", "Italy"], [1962, 1967])
