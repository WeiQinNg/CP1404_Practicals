"""
CP1404/CP5632 Practical 5
Wimbledon
Program to store Wimbledon champions data in a dictionary
Estimate: 25 minutes
Actual: 60 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Read data file and display Wimbledon champions details."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def get_records(filename):
    """Get records from input file in list of lists form."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    print(records)


main()
