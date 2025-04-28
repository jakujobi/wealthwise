# Messaging

This directory contains the code for WealthWise's real-time messaging feature.

## Overview
The `messaging` app enables users to have real-time conversations powered by Django Channels (WebSockets) with a fallback InMemory channel layer for local development.

## Setup
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Configure `.env`:
  ```bash
  REDIS_URL=redis://127.0.0.1:6379
  CELERY_BROKER_URL=redis://127.0.0.1:6379/0
  CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
  ```
- Start services:
  **Option A: Docker Compose**
  ```bash
  docker compose up --build
  docker compose down --remove-orphans
  ```
  **Option B: Individually**
  ```bash
  docker run -d --name redis -p 6379:6379 redis:latest
  python -m celery -A core worker -l info
  uvicorn core.asgi:application --reload --host 127.0.0.1 --port 8000
  ```

## Running the Server
Use one of the following:
```bash
# With Daphne
daphne -b 127.0.0.1 -p 8000 core.asgi:application

# Or with Uvicorn
uvicorn core.asgi:application --reload --host 127.0.0.1 --port 8000
```

Then visit `http://localhost:8000/messaging/` in your browser.

## Endpoints
- REST API under `/messaging/api/`
- WebSocket endpoint: `ws://<host>/ws/chat/{conversation_id}/`

## WebSocket Protocol
Clients should send JSON messages:
```json
{ "body": "Your message here" }
```
Server broadcasts each new message to all connected clients in that conversation group.

## Deleting Messages
To delete a message:
- **REST**: `DELETE /messaging/api/conversations/{conversation_id}/messages/{message_id}/`
- **WebSocket**: send `{ "delete_id": <message_id> }` on `/ws/chat/{conversation_id}/`

## Notifications
New message notifications (email/SMS/in-app) are dispatched via Celery tasks when messages are sent.

## Code Structure
- `consumers.py`: WebSocket consumer handling connect, receive, disconnect and group operations.
- `views.py`: REST viewsets for conversations and messages.
- `serializers.py`: DRF serializers for Conversation and Message models.
- `routing.py`: WebSocket URL routing to `ChatConsumer`.
- `templates/messaging/index.html`: Front-end UI and JavaScript for real-time messaging.

## Testing
Run `pytest` to execute unit tests for the messaging app.
