# Airport Data Analysis CLI

A Python command-line tool for analyzing airport departure data from CSV files. The script loads a selected airport and year dataset, calculates flight statistics, prints the results, saves them to a text file, and displays a histogram of departures by hour for a chosen airline.

## Features

- Validates airport code and year input from the user
- Loads airport departure data from CSV files
- Calculates key statistics such as:
  - total flights
  - runway 1 departures
  - flights over 500 miles
  - British Airways departures
  - departures in rain
  - average flights per hour
  - delayed departures
  - most common destinations
- Saves results to `results.txt`
- Displays a histogram of hourly departures for a selected airline

## Files

- `code.py` - main Python script
- `graphics.py` - graphics library used for the histogram window
- `CDG2021.csv` - sample airport data file
- `LHR2025.csv` - sample airport data file
- `results.txt` - output file where summaries are appended

## Requirements

- Python 3
- The CSV file must be named using the airport code and year format, for example:
  - `CDG2021.csv`
  - `LHR2025.csv`

## How to Run

1. Open a terminal in the project folder.
2. Run the main script:

```bash
python code.py
```

3. Enter a valid three-letter airport code.
4. Enter a valid year between 2000 and 2025.
5. Choose an airline code when prompted to generate the histogram.

## Output

The program prints a summary of the selected airport data to the console and appends the same results to `results.txt`.

## Notes

- The histogram only plots flights from 00:00 to 11:59.
- If the matching CSV file is not found, the program asks for a new selection.
- Existing content in `results.txt` is preserved because new runs are appended to the file.
