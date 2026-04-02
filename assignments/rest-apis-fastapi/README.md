# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework in Python, learning how to define routes, handle HTTP methods, work with request and response models, and test your API using the built-in interactive documentation.

## 📝 Tasks

### 🛠️ Create a FastAPI Application with CRUD Endpoints

#### Description
Set up a FastAPI application that manages a collection of items (e.g., a simple to-do list or book catalog). Implement the four core HTTP methods — GET, POST, PUT, and DELETE — to allow clients to create, read, update, and delete items.

#### Requirements
Completed program should:

- Define a data model using Pydantic's `BaseModel` with at least three fields (e.g., `id`, `title`, `description`)
- Implement a `GET /items` endpoint that returns the full list of items
- Implement a `GET /items/{item_id}` endpoint that returns a single item by its ID, returning a 404 error if not found
- Implement a `POST /items` endpoint that accepts a JSON body and adds a new item to the list
- Implement a `DELETE /items/{item_id}` endpoint that removes an item by ID

### 🛠️ Add Input Validation and Error Handling

#### Description
Extend your API to validate incoming data and return meaningful error responses when something goes wrong.

#### Requirements
Completed program should:

- Use Pydantic field constraints to validate input (e.g., `title` must be a non-empty string, `description` has a maximum length of 200 characters)
- Return a `422 Unprocessable Entity` response automatically when validation fails (FastAPI handles this with Pydantic)
- Return a `404 Not Found` response with a descriptive message when an item ID does not exist
- Implement a `PUT /items/{item_id}` endpoint that updates an existing item and returns the updated item, or 404 if not found
