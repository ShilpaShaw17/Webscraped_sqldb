# Web Scraping and Database Integration

This project demonstrates how to scrape information from websites using Python, extract relevant metadata, and store it in a SQL database. The script utilizes libraries like `requests`, `BeautifulSoup`, and `pyodbc` for web scraping and database interaction.

## Features

- **Scraping Functions**:
  - Extracts meta tags (title, description).
  - Finds social media links.
  - Detects technology stack and payment gateways.
  - Determines website language and category.

- **Database Integration**:
  - Stores scraped data into a SQL Server database.

## Requirements

Ensure you have the following installed:
- Python 3.x
- Required Python libraries (`requests`, `beautifulsoup4`, `pyodbc`)
- ODBC Driver for SQL Server
- SQL Server Management Studio (SSMS) or equivalent tool for database management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/web-scraping.git
   cd web-scraping
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up ODBC Driver**:
   - Download and install the [ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

4. **Configure Database Connection**:
   - Open `config.py` and update the database configuration:
     ```python
     DB_SERVER = 'your_server_name'
     DB_DATABASE = 'WebScraping'
     DB_USERNAME = 'your_username'
     DB_PASSWORD = 'your_password'
     ```

## Usage

1. **Prepare Input**:
   - Create a CSV file (`websites.csv`) containing URLs under the `url` column.

2. **Run the Script**:
   - Execute the Python script to scrape website data and store it in a CSV file:
     ```bash
     python scrape_websites.py
     ```

3. **Verify Output**:
   - Check `scraped_data.csv` for the scraped website information.

## Example

```python
# Example with reading URLs from websites.csv and outputting to scraped_data.csv
csv_file = 'websites.csv'
output_file = 'scraped_data.csv'
main(csv_file, output_file)
```

## Notes

- Adjust `determine_category` and parsing logic in `scrape_websites.py` as per your requirements.
- Ensure proper handling of exceptions and errors during scraping.
- Modify SQL schema and queries in `database.py` for advanced database operations.


