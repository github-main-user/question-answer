# Question-Answer API

A simple API service for creating questions and answers, built with Django and Django Rest Framework.

## Project Description

The service provides endpoints for managing questions and their corresponding answers. It is built following the requirements specified in the `task.md` file.

Key features:
- Create, list, retrieve, and delete questions.
- Create, retrieve, and delete answers for specific questions.
- Cascade deletion of answers when a question is deleted.
- API documentation using Swagger/ReDoc.

## Tech Stack

- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Testing:** Pytest
- **API Documentation:** drf-spectacular

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation and Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/github-main-user/question-answer.git
    cd question-answer
    ```

2.  **Create an environment file:**

    Create a `.env` file by copying the example file:
    ```bash
    cp .env.example .env
    ```

    Example `.env`:
    ```env
    # django settings
    SECRET_KEY=your-secret-key-here
    DEBUG=False
    ALLOWED_HOSTS=localhost,127.0.0.1

    # postgresql settings
    DB_NAME=qa_db
    DB_USER=qa_user
    DB_PASS=qa_pass
    DB_HOST=db
    DB_PORT=5432
    ```

3.  **Run the application:**

    Use Docker Compose to build and run the services:
    ```bash
    docker-compose up --build
    ```

    The application will be available at `http://localhost:8000`.

## API Endpoints

The API endpoints are available under the `/api/` prefix.

### API Documentation

- **Swagger UI:** `http://localhost:8000/api/docs/`
- **ReDoc:** `http://localhost:8000/api/redoc/`

### Questions

-   `GET /api/questions/`
    -   List all questions.
-   `POST /api/questions/`
    -   Create a new question.
    -   **Body:** `{ "text": "Your question text?" }`
-   `GET /api/questions/{id}/`
    -   Retrieve a question and all its answers.
-   `DELETE /api/questions/{id}/`
    -   Delete a question and all its associated answers.

### Answers

-   `POST /api/questions/{question_pk}/answers/`
    -   Add an answer to a question.
    -   **Body:** `{ "text": "Your answer text.", "user": "user-uuid-string" }`
-   `GET /api/answers/{id}/`
    -   Retrieve a specific answer.
-   `DELETE /api/answers/{id}/`
    -   Delete an answer.

## Running Tests

To run the tests, you can execute the `pytest` command inside the running `web` container.

```bash
docker compose exec web pytest
```
