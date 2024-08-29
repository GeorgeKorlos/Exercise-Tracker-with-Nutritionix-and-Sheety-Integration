# Exercise Tracker with Nutritionix and Sheety Integration

This repository contains a Python script that automates the process of logging exercises and their corresponding calories burned using the Nutritionix API and storing the data in a Google Sheet via Sheety.

## Features

- **Exercise Data Retrieval**: Uses the Nutritionix API to analyze and retrieve details about exercises performed, including calories burned.
- **Google Sheets Logging**: Automatically logs exercise data (date, time, exercise name, duration, calories burned) into a Google Sheet using Sheety.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `python-dotenv`
- [Nutritionix API](https://www.nutritionix.com/business/api) credentials (App ID and API Key)
- [Sheety API](https://sheety.co/) for Google Sheets integration
- A `.env` file with necessary environment variables

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker
