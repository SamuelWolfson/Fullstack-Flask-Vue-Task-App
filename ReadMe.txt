========================================================================
                      FLASK & VUE TASK MANAGER
========================================================================

A full-stack task management web application built with a Flask & 
PostgreSQL RESTful API backend and a Vue 3 (Composition API) frontend 
powered by Pinia for state management.

------------------------------------------------------------------------
FEATURES
------------------------------------------------------------------------
- User Authentication: Registration, login, and JWT-based protection.
- Password Recovery: Token-based email reset requests via Flask-Mailman.
- Task Management: Create, edit, toggle completed status, and delete tasks.
- Responsive UI: Categorized task view separating active and completed tasks.

------------------------------------------------------------------------
TECH STACK
------------------------------------------------------------------------
Backend:
- Python / Flask
- Flask-SQLAlchemy (PostgreSQL)
- PyJWT (JSON Web Tokens)
- Flask-Mailman (SMTP Email Integration)
- Flask-CORS

Frontend:
- Vue 3 (Composition API)
- Pinia (State Management)
- Axios (HTTP Client)
- Vite
- ESLint & Prettier

------------------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------------------
Fullstack-Flask-Vue-Task-Manager/
│
├── .vscode/
│   └── settings.json
├── backend/
│   ├── .env
│   ├── app.py
│   ├── pyproject.toml
│   └── requirements.txt
│
├── frontend/
│   ├── .vscode/
│   ├── public/
│   │   └── logo.svg
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── stores/
│   │   ├── App.vue
│   │   └── main.js
│   ├── .eslintrc.json
│   ├── .prettierignore
│   ├── .prettierrc
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
│
├── .gitignore
├── cSpell.json
└── ReadMe.txt

------------------------------------------------------------------------
GETTING STARTED: BACKEND SETUP
------------------------------------------------------------------------
1. Navigate to the backend directory:
   cd backend

2. Create and activate a virtual environment:
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

3. Install required packages:
   pip install -r requirements.txt

4. Ensure your `.env` file in the `backend/` directory is configured:
   DB_USER=postgres
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=flask_tasks
   SECRET_KEY=super-secret-dev-key
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_email_app_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com

5. Ensure PostgreSQL is running and the database specified in DB_NAME exists.

6. Run the Flask development server:
   python app.py

------------------------------------------------------------------------
GETTING STARTED: FRONTEND SETUP
------------------------------------------------------------------------
1. Navigate to the frontend directory:
   cd frontend

2. Install dependencies:
   npm install

3. Run the development server:
   npm run dev

4. Open your browser and navigate to:
   http://localhost:5173

------------------------------------------------------------------------
API ENDPOINTS
------------------------------------------------------------------------
Auth & Users:
- POST /users           - Register a new user
- POST /login           - Authenticate user and obtain JWT
- POST /forgot-password - Request a password reset link
- POST /reset-password  - Submit token and new password

Tasks (Requires Bearer Token Header):
- GET    /tasks         - Retrieve user tasks
- POST   /tasks         - Create a new task
- GET    /tasks/<id>    - Get specific task
- PATCH  /tasks/<id>    - Update task title or completed status
- DELETE /tasks/<id>    - Delete task
========================================================================