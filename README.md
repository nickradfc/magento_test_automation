# magento_test_automation


# Test Automation Framework

This repository contains a test automation framework for automating interactions with a web application using Selenium, Python, and PyTest running on CHrome browser. Additional funcationality can be added for supporting different browser and differemt environments (outide of the scope of current project's state).

## Table of Contents

- [File System Structure](#file-system-structure)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)

## File System Structure

The project follows a Page Object Model (POM) design pattern and is organized as follows:

- `page_objects/`: Contains Page Object classes representing web pages.
- `page_helpers/`: Contains Page Helper classes with functions for interacting with web elements on pages.
- `fixtures/`: Contains fixture files for test data and setup.
- `utilities/`: Contains utility functions used across the project.
- `tests/`: Contains the test cases.

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)

## Local Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Create and activate virtual environment (optional but recommended):

    `python3 -m venv venv`
    `source venv/bin/activate`

3. Install project dependencies and upgrade webdriver:

    `pip3 install -r requirements.txt`
    `python3 -m pip install webdriver-manager --upgrade`

4. Set environment variables in a .env file in the project root (email example: test_email+storetest@gmail.com):

    `BASE_EMAIL=your-username`
    `BASE_PASSWORD=your-password`

## Running Tests

You can run the tests locally using the following command with standard PyTest HTML Report:
    `pytest --html=report.html`

You can run the tests locally using the following command without report:
    `pytest tests/`
