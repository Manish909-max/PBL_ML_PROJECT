# AI Mock Interview Assistant

A Django-based mock interview platform designed to simulate realistic interview experiences with AI-powered questioning, transcription, and structured feedback.

## Features

- Interview topic selection for backend, frontend, data science, and DevOps tracks
- Django Modules: users, interviews, ai_interviewer, analysis, and feedback
- Real-time WebSocket channel for interviewer communication
- GraphQL endpoint for integration with ML services
- Basic interview and user models with admin support
- Template-based UI for interview home and detail pages

## Tech Stack

- Django 5.0
- Django REST Framework
- Django Channels
- Graphene-Django
- SQLite by default, PostgreSQL-ready configuration
- Bootstrap-ready responsive templates

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Open http://localhost:8000/

## Project Structure

- `ai_mock_interview/` - Django project settings and routing
- `users/` - candidate and user profile logic
- `interviews/` - interview and question models
- `ai_interviewer/` - AI question generation and WebSocket consumers
- `analysis/` - NLP and scoring logic
- `feedback/` - structured feedback and reporting
- `templates/` - UI templates

## Environment Variables

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

## Notes

This project is intentionally structured as a production-ready foundation for the mock interview assistant, with real integration points left ready for Whisper, LLM APIs, TTS, and analytics services.
