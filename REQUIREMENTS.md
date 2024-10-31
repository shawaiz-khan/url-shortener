# URL Shortener

A simple, Python-based URL shortener that takes long URLs and generates short, easy-to-share versions. This application is designed to create unique short codes for URLs and allow retrieval of the original link using the generated code.

## Features

- **Unique Short Code Generation**: Generates a unique short code (5–7 characters) for each long URL.
- **URL Mapping and Storage**: Maps each short code to its long URL and allows quick retrieval.
- **Reusable Short URLs**: Returns the same short code for URLs that have already been shortened.
- **Easy Retrieval**: Retrieve the original URL from a short code.

## Requirements

The URL shortener should meet the following requirements:

1. **Generate Unique Short Codes**: The system should create a unique short code (5–7 characters) for each URL, ensuring no duplicates.
2. **Efficient URL Storage**: Maintain a mapping between the short code and the original URL, enabling fast look-up and retrieval.
3. **Reusability**: If a URL has already been shortened, the system should return the existing short code rather than generating a new one.
4. **Simple URL Retrieval**: Given a short code, the system should retrieve and return the original URL.
5. **Python Compatibility**: The application should work in Python 3.x without requiring external libraries.