
```
pipenv install
pipenv dev
```

## Why another Python Framework

This is exercise, I think one cannot reach sufficient level of understanding of a web application without dissecting
parts, analysing security, scalability, and performance issues.

In this framework, everything is implemented and in multiple ways and as flexibly as possible so that modifying the
settings gives you different setups. The only dependencies are:

- Uvicorn (ASGI Web Server)
- Psycopg2 (PostgreSQL driver)
- Redis
- Requests
- Starlette

I try to comment them well so that this can be used as
"textbook" by reading the documentation.

Following the guide, you can also implement some parts yourself or extend your favorite microframework!

The influence for the application structure are:
    - Django
    - Django REST Framework
    - FastAPI
    
"Good, fast, cheap. Choose two."
We would like to have _good_ and _cheap_.

## The Topics for the backend of Web Application

Separate framework projects will be created for frontend, database change management, and deployment.

- Architecture
    - JSON API formats
- Authentication
- Caching
- Data Isolation
    - SQL: Column-Level Security
    - SQL: Row-Level Security
    - SQL: Table-Level Security
- Logging
- Monitoring
- Routing
    - Architecture
    - Optimization 
- Storage Systems
    - Databases
        - Relational
        - NoSQL
        - Graph
- Testing
    - Unit testing
    - Integration testing
    - System testing
    - Acceptance testing
- Validation
    - URIs
    - Headers
    - Data
    - Permissions
    - Files
- Vulnerabilities
    - Resource exhaustion
    - Injections
    
