# QuoteNest API

A simple open-source REST API built with Flask that serves inspirational quotes.

## Features
- Get all quotes
- Get a random quote
- Get quotes by author
- Add new quotes (POST request)

## Endpoints
- `GET /quotes`
- `GET /quotes/random`
- `GET /quotes/<author>`
- `POST /quotes`

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`

## Example POST Request

```
POST /quotes
{
  "quote": "Life is what happens when you're busy making other plans.",
  "author": "John Lennon"
}
```

---

Feel free to fork this project and contribute!
