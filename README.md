# KelasOtomesyen Selenium

## About

This is the repository for the final project of KelasOtomesyen's Web Automation course with Selenium. It also uses Pytest for batch testing and Allure Report for reporting purposes.

## Requirements
- Python 3.10+ for `match` statement compatibility
- Allure Report (install [here](https://allurereport.org/docs/install/))

## Modules used

- `selenium`: Used for web testing
- `pytest`: Used for batch testing
- `pytest-html`: Allows `pytest` to generate reports in html files
- `python-dotenv`: Allows python to use `.env` files
- `allure-pytest`: Integrates Allure Report to `pytest`. Requires the host machine to install Allure Report first.

## How to Use

### Setup
1. Install the requirements specified in [the "Requirements" section](#requirements)
2. Clone this repository
3. Create a virtual environment (`python -m venv /path/to/new/virtual/environment`), learn more [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
    - Note: You should create the virtual environment (run `python -m venv [venv-name]`) in the repository folder with the virtual environment name (`venv-name`) starting with `venv`
4. Activate the virtual environment (See [this page](https://docs.python.org/3/library/venv.html#how-venvs-work) to determine the activation command, which varies on the terminal's platform and shell)
5. Install the requirements (`pip install -r requirements.txt`) into the virtual environment

### Usage
1. Run `pytest` to run all tests.
2. Run `allure serve allure-results` to serve the Allure report.
     - Note: You can host the report locally (example: `allure serve allure-results --host 127.0.0.1`)
