# WealthWise
Project for SE 306

Server starts on
- http://localhost:8000/ (local ASGI)
- http://localhost:8001/ (via Docker Compose)

## Real-Time Messaging
WealthWise now includes a real-time messaging feature powered by Django Channels and WebSockets.

### Prerequisites
- Redis (for production or full concurrency; for local dev you can also use the InMemoryChannelLayer).

### Running
```bash
# Start Redis via Docker
docker run -d --name redis -p 6379:6379 redis:latest

# Start ASGI server with Daphne
daphne -b 127.0.0.1 -p 8000 core.asgi:application

# Or with Uvicorn
uvicorn core.asgi:application --reload --host 127.0.0.1 --port 8000
```

You can also spin up **all services** (Postgres, Redis, ASGI, Celery) via Docker Compose:
```bash
docker compose up --build
docker compose down --remove-orphans
```
Then visit `http://localhost:8001/messaging/`.

See `messaging/README.md` or `docs/real-time-messaging.md` for more details.