# User-Owned Notes API - Django REST API with JWT Authentication
<img width="1012" height="661" alt="Screenshot 2025-08-11 184737" src="https://github.com/user-attachments/assets/9305c8a5-6752-447a-9cd4-74695041fce5" />


A Django REST API for managing personal notes with full CRUD functionality and JWT authentication.

## Features

- `Note` model with fields: `title`, `content`, `created_at`  
- Multi-user support: each note belongs to a specific user (`owner`)  
- Full CRUD operations via a ViewSet (list, retrieve, create, update, delete)  
- JWT Authentication with SimpleJWT
  - Signup endpoint for user registration
  - Login endpoint to obtain access & refresh tokens
- API access restricted to authenticated users (`IsAuthenticated`)
- Users can only see and manage their own notes
- Tested in Postman:
  - Requests without token → 401 Unauthorized
  - Requests with token → Successful CRUD operations

