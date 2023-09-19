# magento_test_automation


# Test Automation Framework

This repository contains a test automation framework for automating interactions with a web application using Selenium, Python, and PyTest.

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
   cd <repository-folder>```

2. Create a virtual environment (optional but recommended):

    `python -m venv venv source venv/bin/activate`

3. Install project dependencies:

    `pip install -r requirements.txt`

4. Set environment variables (if required) in a .env file in the project root (email example: test_email+storetest@gmail.com):

    `BASE_EMAIL=your-username`
    `BASE_PASSWORD=your-password`

## Running Tests

You can run the tests locally using the following command:
    `pytest tests/`
