# Library Management System API

This project is a Flask-based REST API for managing a library system. It supports CRUD operations for both books and members and includes features like pagination and token-based authentication.

## How to Run the Project

### Prerequisites
- Python 3.7 or higher
- Flask library

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python <script_name>.py
   ```

4. Access the API at:
   ```bash
   http://127.0.0.1:5000
   ```

5. Use an API client like Postman or curl to interact with the endpoints. Ensure you include the Authorization header:
   ```bash
   Authorization: Bearer secret-token
   ```

---

## API Endpoints

### Books
- `GET /books` - Retrieve a paginated list of books.
- `POST /books` - Add a new book.
- `GET /books/<book_id>` - Retrieve details of a specific book.
- `PUT /books/<book_id>` - Update details of a specific book.
- `DELETE /books/<book_id>` - Delete a specific book.

### Members
- `GET /members` - Retrieve a paginated list of members.
- `POST /members` - Add a new member.
- `GET /members/<member_id>` - Retrieve details of a specific member.
- `PUT /members/<member_id>` - Update details of a specific member.
- `DELETE /members/<member_id>` - Delete a specific member.

Pagination parameters (`page` and `per_page`) can be passed as query parameters in the `GET` endpoints.

---

## Design Choices
1. **In-memory Storage**: Data is stored in-memory for simplicity. This makes the API suitable for prototyping or educational purposes. For production, a persistent database like SQLite or PostgreSQL should be used.
2. **Token-based Authentication**: A simple token (`secret-token`) is used for securing the API endpoints.
3. **Pagination**: Pagination is implemented to prevent returning too many records at once, improving performance and usability.
4. **RESTful Design**: The API adheres to REST principles, with clear separation of resource types (Books and Members) and standard HTTP methods.

---

## Assumptions and Limitations
1. **Authentication**:
   - A single hardcoded token (`secret-token`) is used for simplicity. In production, a more robust authentication mechanism like OAuth2 should be implemented.

2. **Data Persistence**:
   - Data is lost when the application stops since it uses in-memory storage. To persist data, integrate a database.

3. **Validation**:
   - Minimal input validation is implemented. Adding more robust validation for fields like email format, ISBN, etc., is recommended.

4. **Scalability**:
   - The current implementation is not suitable for large-scale deployment due to in-memory storage and lack of advanced features like rate limiting.

---

For questions or contributions, feel free to reach out or create a pull request.

