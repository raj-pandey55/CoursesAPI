# Django Courses API

This project is a backend application developed in Django to provide REST APIs for managing courses and their instances. It is designed as part of an internship assignment at IIT Bombay's Application Software Centre. The application allows users to perform CRUD operations on courses and their delivery instances using RESTful endpoints.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The Django Courses API provides a set of RESTful APIs for managing course data, including creating, retrieving, updating, and deleting courses and course instances. The application is developed using Django and Django REST Framework, with SQLite as the default database.

## Features

- **CRUD operations** for managing courses and course instances
- **RESTful API design** for easy integration with front-end applications
- **JWT-based authentication** for secure API access
- **Swagger API documentation** for easy reference and testing
- **Dockerized deployment** for seamless setup and deployment

## Technologies Used

- **Django**: Python web framework for backend development
- **Django REST Framework**: Toolkit for building Web APIs
- **SQLite**: Lightweight, file-based database for data storage
- **Docker**: Containerization for deployment
- **Swagger**: For API documentation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/raj-pandey55/CoursesAPI.git
   cd CoursesAPI
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Apply migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

The following API endpoints are available:

| Endpoint                              | Method | Description                                            |
|---------------------------------------|--------|--------------------------------------------------------|
| `/api/courses/`                       | POST   | Create a new course                                    |
| `/api/courses/`                       | GET    | Get a list of all courses                              |
| `/api/courses/<id>/`                  | GET    | Get detailed information about a specific course       |
| `/api/courses/<id>/`                  | DELETE | Delete a specific course                               |
| `/api/instances/`                     | POST   | Create a new instance of a course delivery             |
| `/api/instances/<year>/<semester>/`   | GET    | List courses delivered in a specific year and semester |
| `/api/instances/<year>/<semester>/<id>/` | GET | Get details of a specific course instance              |
| `/api/instances/<year>/<semester>/<id>/` | DELETE | Delete a specific course instance                     |

## Docker Setup

1. Build the Docker image:

   ```bash
   docker build -t your-dockerhub-username/courses-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 your-dockerhub-username/courses-api
   ```

3. To use Docker Compose:

   - Ensure you have `docker-compose.yml` configured as per the repository.
   - Run Docker Compose:

   ```bash
   docker-compose up
   ```

- Use any REST client (e.g., Postman) to interact with the API endpoints.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [your-email@example.com](mailto:rajpandey552002@gmail.com).
