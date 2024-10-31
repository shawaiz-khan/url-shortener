# URL Shortener

A simple Python-based URL shortener that converts long URLs into short, easy-to-share links. This application generates unique short codes for URLs, allowing users to store and retrieve original links efficiently.

## Features

- **Unique Short Code Generation**: Automatically creates unique short codes for each long URL.
- **URL Mapping and Storage**: Maps short codes to long URLs and enables quick retrieval.
- **Reusable Short URLs**: Returns the same short code if a URL has already been shortened.
- **Original URL Retrieval**: Retrieves the original URL when provided with a short code.

## Requirements

- Python 3.x
- No external libraries required

## Getting Started

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shawaiz-khan/url-shortener.git
   ```
2. **Navigate into the project directory**:
   ```bash
   cd url-shortener
   ```

3. **Expected Output**:
   ```
   Short URL: http://short.url/abc123
   Retrieved URL: https://www.example.com/very/long/url
   ```

## Project Structure

- `url_shortener.py`: Contains the main logic for URL shortening.
- `README.md`: Project documentation.

## How It Works

1. **Shorten a URL**: Generates a random 6-character short code (letters and numbers) and maps it to the provided long URL.
2. **Retrieve URL**: Looks up the long URL based on the provided short code.

## Future Enhancements

- **Database Integration**: Use a database to store URL mappings for persistence.
- **Custom Short Codes**: Allow users to set custom codes for their URLs.
- **URL Expiration**: Add expiration dates for short URLs, if desired.

## License

This project is licensed under the MIT License. See `LICENSE` for details.