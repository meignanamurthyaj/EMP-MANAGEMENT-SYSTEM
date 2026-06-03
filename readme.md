# Employee Registration & Management System

A full-stack web application designed to handle the registration and management of employee records. Built with **FastAPI** for a high-performance backend, **SQLAlchemy** for database interactions, and a clean, responsive frontend using plain HTML, CSS, and JavaScript. 

## 🚀 Features

* **Complete CRUD Operations:** Users can create, read, update, and delete employee records via a seamless web interface.
* **RESTful API Architecture:** Backend endpoints clearly separated for data operations.
* **Data Validation:** Pydantic models automatically validate incoming JSON payloads, preventing duplicate Employee IDs and Emails.
* **Responsive User Interface:** Lightweight frontend powered by custom CSS and Vanilla JavaScript fetch requests.
* **Interactive API Documentation:** Auto-generated Swagger UI accessible via FastAPI.

---

## 🏛️ System Architecture

The following Mermaid diagram maps the exact data flow and functional architecture based on the project files. 

```mermaid
graph TD
    %% Define Node Styles
    classDef frontend fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef backend fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#0f172a;
    classDef database fill:#fef08a,stroke:#ca8a04,stroke-width:2px,color:#0f172a;

    %% Client Layer
    subgraph Client [Frontend UI Layer]
        UI[HTML Templates<br>index, create, update, search]:::frontend
        JS[Vanilla JS fetch API]:::frontend
        UI <-->|User Interaction| JS
    end

    %% Backend Layer
    subgraph API [FastAPI Backend Layer]
        Main[main.py<br>API Routes & Static Serving]:::backend
        Schemas[schemas.py<br>Pydantic Data Validation]:::backend
        CRUD[crud.py<br>Business Logic]:::backend
        Models[models.py<br>SQLAlchemy Tables]:::backend
        DBConn[database.py<br>MySQL Engine & Session]:::backend

        JS <-->|HTTP Requests| Main
        Main -->|Validates Input| Schemas
        Main -->|Routes Request| CRUD
        CRUD -->|Maps Data| Models
        CRUD -->|Executes Query| DBConn
    end

    %% Database Layer
    subgraph Storage [Database Layer]
        MySQL[(MySQL Database<br>employee_db)]:::database
    end

    %% Database Connection
    DBConn <-->|PyMySQL Driver| MySQL