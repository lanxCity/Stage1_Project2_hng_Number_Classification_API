# Number Classification API

This is a Django-based API that classifies numbers based on their mathematical properties and provides a fun fact about them using the Numbers API.

## Features

- Checks if a number is prime.
- Determines if a number is an Armstrong number.
- Determines if a number is a perfect number.
- Calculates the sum of digits.
- Fetches a fun fact about the number.
- Returns responses in JSON format.

## API Endpoint

**Base URL:** `http://<your-domain>/api/classify-number/`

### Request Format

**Method:** `GET`
**Query Parameter:** `number` (integer)

**Example Request:**

```sh
GET http://127.0.0.1:8000/api/classify-number/?number=371
```

### Success Response (200 OK)

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

```json
{
  "number": "alphabet",
  "error": "Number parameter is required."
}
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the server:
   ```sh
   python manage.py runserver
   ```

## Deployment

- The API must be publicly accessible.
- Enable CORS to allow cross-origin requests.
- Deploy using platforms like **Heroku, Render, or DigitalOcean**.

## Technologies Used

- Django & Django REST Framework
- Requests (for fetching fun facts)
- Python 3.x

## Contributing

Feel free to fork the repository and submit a pull request with improvements.

## License

This project is open-source and available under the MIT License.
