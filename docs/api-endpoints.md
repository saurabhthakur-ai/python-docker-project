# API Endpoints

This document describes the authentication and user management endpoints available in the `feature/api-development` branch.

---

## Base URL

```
/api/v1
```

---

## Authentication

### POST /auth/register

Register a new user account.

#### Request Body

```json
{
  "name": "John Doe",
  "age": 30,
  "address": "123 Main Street, City, Country",
  "phone_no": "+1234567890",
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

#### Response

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "User registered successfully"
}
```

#### Status Codes

| Status | Description |
|--------|-------------|
| 201    | User created successfully. |
| 400    | Invalid request data or user already exists. |
| 422    | Validation error. |

---

### POST /auth/login

Authenticate a user and receive an access token.

#### Request Body

```json
{
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

#### Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Status Codes

| Status | Description |
|--------|-------------|
| 200    | Login successful. |
| 401    | Invalid credentials. |
| 422    | Validation error. |

---

### POST /auth/logout

Logout the currently authenticated user.

#### Headers

```http
Authorization: Bearer <access_token>
```

#### Response

```json
{
  "message": "Successfully logged out"
}
```

#### Status Codes

| Status | Description |
|--------|-------------|
| 200    | Logout successful. |
| 401    | Missing or invalid token. |

---

## Users

### GET /users/me

Retrieve the currently authenticated user's information.

#### Headers

```http
Authorization: Bearer <access_token>
```

#### Response

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "address": "123 Main Street, City, Country",
  "phone_no": "+1234567890",
  "email": "john.doe@example.com"
}
```

#### Status Codes

| Status | Description |
|--------|-------------|
| 200    | User information retrieved successfully. |
| 401    | Missing or invalid token. |
| 404    | User not found. |

---

## Notes

- All authenticated endpoints require a valid Bearer token in the `Authorization` header.
- Passwords must be stored securely using a hashing algorithm such as bcrypt.
- Tokens should have an expiration time and be refreshed or reissued as needed.
