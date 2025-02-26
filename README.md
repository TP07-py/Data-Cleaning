# COVID-19 Data Cleaning and Validation

This project focuses on cleaning and validating a COVID-19 dataset using Python and Pandas. It checks for missing or incorrect data, ensuring consistency in country names, WHO regions, and numerical values.

## Features
- Cleans and standardizes country and WHO region names
- Identifies missing or incorrectly spelled entries
- Ensures numeric consistency for confirmed, deaths, recovered, and active cases
- Outputs a validation report listing data issues

## Requirements
Ensure you have Python installed along with the following dependencies:
- `pandas`

## How It Works
1. Reads the dataset `covid_19_set_2 (1).csv`.
2. Cleans country and WHO region names by trimming spaces and converting to lowercase.
3. Checks for:
   - Missing values in `Country/Region` and `WHO Region`
   - Incorrect spellings in country and WHO region names
   - Non-numeric entries in quantitative columns
   - Inconsistent `Active` case calculations (`Confirmed - Deaths - Recovered`)
4. Saves identified issues in `validation_results.csv` for review.

## File Structure
```
.
├── covid_19_set_2 (1).csv   # Raw COVID-19 dataset
├── datacleaning.py          # Script for data cleaning and validation
├── validation_results.csv   # Output file listing identified data issues
```

## Future Improvements
- Enhance error handling for data inconsistencies
- Implement visualization tools for better data assessment
- Automate correction of common data entry mistakes

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.
