"""
CP1404/CP5632 Practical 5
Wimbledon
Program to store Wimbledon champions data in a dictionary
Estimate: 25 minutes
Actual: 60 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """Get records from input file in list of lists form."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    print(records)


main()
