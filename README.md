# NeuroZip

NeuroZip is a Django-based application designed for efficient image compression. Currently under active development, it leverages Docker for containerization, PostgreSQL for database management, and Redis for caching to ensure scalability and performance.

## Expected Features
 - **Image Compression:** 
Upload images to receive compressed versions with reduced file sizes while maintaining quality.

 - **User Authentication:**
Secure user accounts to manage and track compression tasks.

 - **Asynchronous Processing**:
Utilizes Celery for background processing of compression tasks.

 - **Scalable Architecture:**
Designed with microservices in mind, facilitating easy scaling and maintenance.​

 - **More...**

## Technologies (to be used)
 - **Django:** A high -level Python web framework that encourages rapid development and clean, pragmatic design.​

 - **PostgreSQL:** A powerful, open-source relational database system.​

 - **Redis:** An in-memory data structure store, used as a database, cache, and message broker.​

 - **Celery:** An asynchronous task queue/job queue based on distributed message passing.​

 - **Docker:** A platform for developing, shipping, and running applications in containers.

 - **More...**

## Getting Started

To set up the project locally using Docker:

Clone the repository:

```sh
    git clone https://github.com/Saiyam-Sandhir-Jain/neurozip.git
```

Navigate to the project directory:

```sh
    cd neurozip
```

Create a .env file in the project root with the following environment variables:

```
    # PostgreSQL Configuration
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    # Redis Configuration
    REDIS_HOST=cache
    REDIS_PORT=6379

    # Django Settings
    DEBUG=False
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=your_domain.com,localhost,127.0.0.1
````

**Note:** Ensure that the POSTGRES_HOST and REDIS_HOST values match the service names defined in your docker-compose.yml file.​

Build and start the Docker containers:

```sh
    docker-compose up --build
```

This command builds the necessary Docker images and starts the containers as defined in the docker-compose.yml file.

Apply database migrations:

```sh
    docker-compose exec web python manage.py migrate
```

Create a superuser account (optional, for accessing the Django admin interface):

```sh
    docker-compose exec web python manage.py createsuperuser
```

Access the application:

    The web application will be running at http://localhost:8000/.​

    The Django admin interface can be accessed at http://localhost:8000/admin/.

## Contributing

At this stage, contributions are restricted to team members only. If you are a team member, please ensure you have the necessary permissions to access and contribute to the repository. For more information on managing team access and permissions, refer to GitHub's documentation on [Managing team access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository).​

## License

This project is licensed under the MIT License.​

Note: Details and features are subject to change as development progresses.​
