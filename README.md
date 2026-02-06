# Notes Docker — Django + PostgreSQL (CI Learning Project)

This project is a small hands-on practice to learn:

- Docker (Dockerfile, images, containers)
- Docker Compose (multi-container setup)
- PostgreSQL as a database container
- Volumes for database persistence
- GitHub Actions (CI – automatic Docker build on push)



---

## 🧰 Tech Stack

- Django (Python)
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI)

---

## 📁 Project Structure

notes-docker/
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── config/
├── notes/
└── .github/workflows/docker-build.yml


---

## 🚀 Run the Project (Docker)

From the root folder:

`bash
docker compose up --build
Open in browser:

http://localhost:8000
Admin panel:

http://localhost:8000/admin
🗄️ Database (PostgreSQL)
The project uses a PostgreSQL container connected to Django.

Database configuration is passed via environment variables in docker-compose.yml.

💾 Volume Persistence
The database uses a Docker volume:

pgdata
This means:

docker compose down → containers removed, data stays

docker compose down -v → containers + database data deleted

👤 Create Admin User
Run:

docker exec -it notes-docker-backend-1 python manage.py createsuperuser
Then login at:

http://localhost:8000/admin
📝 Add Notes
Notes can be added from Django Admin:

Title

Content

Stored in PostgreSQL.

🔄 Migrations (if needed)
docker exec -it notes-docker-backend-1 python manage.py makemigrations
docker exec -it notes-docker-backend-1 python manage.py migrate
⚙️ CI — GitHub Actions
This project includes a simple CI pipeline.

On every push to main:

GitHub automatically builds the Docker image

Workflow file:

.github/workflows/docker-build.yml
You can see runs in:
GitHub → Actions tab.

🧪 What this project demonstrates
Containerized Django backend

Multi-container architecture

DB persistence with volumes

CI automation with GitHub Actions

🔮 Future Improvements (next learning steps)
Add Django REST API

Add React frontend

Add CD (auto push image to Docker Hub)

Deploy to real server


---

## Push it

In VS Code terminal:

``bash
git add README.md
git commit -m "Add project README"
git push
