Selenium Python Automation Framework
🎥 Demonstration Video

Watch the Project Demonstration Video

The demonstration video explains the project structure, framework components, Selenium execution, Login automation, Product Search for MacBook, and successful test execution.

📌 Project Overview

This project is a Selenium Python Automation Framework developed for automating an e-commerce web application using the TutorialsNinja Demo website.

The framework is designed using PyTest, Unittest, and Page Object Model (POM) along with reusable utilities, configuration management, external test data, logging, screenshots on failure, and HTML reporting.

Application Under Test

TutorialsNinja Demo:
https://tutorialsninja.com/demo/

🎯 Automation Scenarios

The framework automates the following scenarios:

1. User Login
Open the TutorialsNinja Demo application.
Navigate to My Account.
Select Login.
Read email and password from the configuration file.
Enter the credentials.
Click the Login button.
Verify that the My Account page is displayed.
2. Product Search
Read test data from the CSV file.
Log into the application.
Read the product name from the CSV file.
Search for the product.
Verify that the product results are displayed.

The current test data uses:

Product: MacBook
