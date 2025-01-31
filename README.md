# GiveTake - Skill Exchange Platform

GiveTake is a platform where developers can exchange their skills and services without monetary transactions, using an escrow system to ensure trust and reliability.

## Features

- **Skill-Based Exchange**: Exchange your development skills with other developers
- **Escrow System**: Built-in security system to ensure fair exchanges
- **Service Management**: Create, manage, and track service exchanges
- **User Profiles**: Showcase your skills and track your exchange history
- **Real-time Status Updates**: Monitor the progress of your exchanges

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/givetake.git
cd givetake
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
flask run
```

## Project Structure

```
givetake/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── static/            # Static files (CSS, JS)
│   ├── css/
│   └── js/
└── templates/         # HTML templates
    ├── base.html
    ├── index.html
    └── ...
```

## Usage

1. Register an account on the platform
2. Create a service listing with your skills
3. Browse available services
4. Request an exchange
5. Complete the exchange and release escrow

## Development

### Running Tests
```bash
pytest
```

### Code Style
Follow PEP 8 guidelines for Python code.

## Security Features

- Secure password hashing
- CSRF protection
- Session management
- Input validation
- XSS prevention
- Escrow system for exchanges

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Flask framework
- Bootstrap for UI
- SQLAlchemy for database management
- Contributors and community members
