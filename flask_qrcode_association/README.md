# Flask QRCode Association

This project is a web application built with Flask that allows users to register members and generate QR codes for them. The application includes user authentication and member management features.

## Features

- User registration and login
- Member registration with QR code generation
- Member profile display

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-qrcode-association.git
   cd flask-qrcode-association
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. Run the application:
   ```
   flask run
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Register a new user account.
2. Log in with your credentials.
3. Register new members and generate QR codes for them.
4. View member profiles with their QR codes.

## License

This project is licensed under the MIT License.
