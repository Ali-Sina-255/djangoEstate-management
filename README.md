🏠 Django Estate Management System

A comprehensive real estate management platform built with Django, Docker, Celery, Next.js, and PostgreSQL. This system helps property managers, landlords, and tenants manage properties, leases, payments, and maintenance requests efficiently.
🚀 Tech Stack
Backend

    Django 5.0 - Python web framework

    Django REST Framework - RESTful API development

    PostgreSQL - Primary database

    Redis - Caching and message broker

    RabbitMQ - Message queue for Celery

    Celery - Async task processing

    Celery Beat - Scheduled tasks

    Flower - Celery monitoring

    JWT Authentication - Secure API authentication

    Swagger/OpenAPI - API documentation

Frontend

    Next.js  - React framework

    Redux Toolkit - State management

    Tailwind CSS - Styling

    TypeScript - Type safety

Infrastructure

    Docker & Docker Compose - Containerization

    Nginx - Reverse proxy

    GitHub Actions - CI/CD

✨ Features
Property Management

    ✅ Property listings with images and details

    ✅ Unit/room management

    ✅ Amenities tracking

    ✅ Document storage (leases, agreements)

    ✅ Interactive maps integration

Tenant Management

    ✅ Tenant profiles and history

    ✅ Lease agreement management

    ✅ Rent tracking and reminders

    ✅ Maintenance request system

    ✅ Communication portal

Financial Management

    ✅ Rent collection and tracking

    ✅ Invoice generation

    ✅ Expense tracking

    ✅ Payment reminders

    ✅ Financial reports

    ✅ Integration with payment gateways

Automation & Async Tasks

    ✅ Scheduled rent reminders (Celery Beat)

    ✅ Automatic late fee calculation

    ✅ Email/SMS notifications

    ✅ Report generation

    ✅ Data backup automation

    ✅ Web scraping for property listings

Web Scraping Integration

    ✅ Automatic property import from popular portals

    ✅ Market price analysis

    ✅ Competitor property tracking

    ✅ Scheduled scraping tasks

Analytics & Reporting

    ✅ Occupancy rates

    ✅ Revenue analytics

    ✅ Maintenance costs

    ✅ Tenant turnover rates

    ✅ Custom report builder

📋 Prerequisites

    Docker and Docker Compose

    Python 3.11+

    Node.js 18+

    Git

🚦 Getting Started
Clone the Repository
bash

git clone https://github.com/yourusername/djangoEstate-management.git
cd djangoEstate-management

cp .env.example .env
# Edit .env with your configuration

# Build and start all services
docker-compose up -d --build

# Run migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Collect static files
docker-compose exec backend python manage.py collectstatic --noinput

Access the Application

    Frontend: http://localhost:3000

    Backend API: http://localhost:8000/api/v1

    Django Admin: http://localhost:8000/api/v1/admin

    API Documentation: http://localhost:8000/api/v1/swagger

    Flower Monitoring: http://localhost:5555

    RabbitMQ Management: http://localhost:15672



🐳 Docker Services
Service	Port	Description
PostgreSQL	5432	Primary database
Redis	6379	Caching & broker
RabbitMQ	5672, 15672	Message queue
Django Backend	8000	REST API
Celery Worker	-	Async tasks
Celery Beat	-	Scheduled tasks
Flower	5555	Task monitoring
Next.js Frontend	3000	Web application
Nginx	80, 443	Reverse proxy

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements/dev.txt


🔧 Development Setup (Without Docker)

# Setup database
createdb djangoestate

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver


Frontend Setup
cd frontend
npm install
npm run dev

Celery Setup

# Terminal 1: Start Redis
redis-server

# Terminal 2: Start Celery Worker
celery -A config worker --loglevel=info

# Terminal 3: Start Celery Beat
celery -A config beat --loglevel=info

# Terminal 4: Start Flower
celery -A config flower --port=5555