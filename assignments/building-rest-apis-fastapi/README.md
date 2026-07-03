# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints, handling JSON data, and validating request bodies. This assignment will help students practice backend web development concepts and Python programming.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI app that exposes a simple home endpoint and returns JSON data. The app should run locally and respond to basic requests.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app.
- Create at least one GET endpoint that returns a JSON response.
- Start the app locally with Uvicorn.
- Add a simple root endpoint that returns a welcome message.

### 🛠️ Build CRUD Endpoints

#### Description
Expand the API to manage a collection of items such as books, tasks, or students. Each item should be created, read, updated, and deleted through REST endpoints.

#### Requirements
Completed program should:

- Define a Pydantic model for the item data.
- Create endpoints for creating and reading items.
- Add update and delete endpoints for existing items.
- Return clear JSON responses for success and error cases.
- Use in-memory storage for the assignment.
