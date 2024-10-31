# URL Shortener

A simple, Python-based URL shortener that takes long URLs and generates short, easy-to-share versions. This application is designed to create unique short codes for URLs and allow retrieval of the original link using the generated code.

## Features

- **Unique Short Code Generation**: Generates a unique short code (5–7 characters) for each long URL.
- **URL Mapping and Storage**: Maps each short code to its long URL and allows quick retrieval.
- **Reusable Short URLs**: Returns the same short code for URLs that have already been shortened.
- **Easy Retrieval**: Retrieve the original URL from a short code.

## Requirements

- Python 3.x
- No external libraries are needed

## How It Works

1. **Shortening a URL**: Generates a random short code and maps it to the long URL.
2. **Retrieving the URL**: Looks up the long URL based on the provided short code.

## Future Improvements

- **Database Integration**: Store mappings in a database for persistence.
- **Custom Short Codes**: Allow users to specify their own short codes.
- **Expiration Dates**: Add optional expiration dates for short URLs.