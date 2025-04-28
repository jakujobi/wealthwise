# Real-Time Messaging

This document describes the real-time messaging feature in WealthWise, powered by Django Channels and WebSockets. It covers setup, commands, and API/WebSocket endpoints.

## Prerequisites
- Redis server (for production concurrency). For local development, you can use the built-in InMemoryChannelLayer.
- Python dependencies installed: `pip install -r requirements.txt`
- Environment variables configured (.env):
  ```bash
  DEBUG=True
  SECRET_KEY=...
  DATABASE_URL=postgres://...@localhost:5432/wealthwise
  REDIS_URL=redis://127.0.0.1:6379
  ```

## Setup & Commands
```bash
# Start Redis via Docker (local dev)
docker run -d --name redis -p 6379:6379 redis:latest

# Start the ASGI server with Daphne
daphne -b 127.0.0.1 -p 8000 core.asgi:application

# Or with Uvicorn
uvicorn core.asgi:application --reload --host 127.0.0.1 --port 8000
```

## API Endpoints
- **List Conversations**: `GET /messaging/api/conversations/`
- **Create Conversation**: `POST /messaging/api/conversations/` (no body required)
- **List Messages in Conversation**: `GET /messaging/api/conversations/{conversation_id}/messages/`
- **Send Message via REST**: `POST /messaging/api/conversations/{conversation_id}/messages/` with JSON `{ "body": "..." }`

## WebSocket Endpoint
- **URL**: `ws://<host>/ws/chat/{conversation_id}/`
- **Protocol**: JSON messages with the shape:
  ```json
  { "body": "Hello, world!" }
  ```
- **Behavior**:
  1. Client connects to `/ws/chat/{id}/`.
  2. Server adds client to group `chat_{id}`.
  3. When a new message arrives, server broadcasts to the group.

## Front-End Integration
- The messaging center UI is available at `http://<host>/messaging/`.
- It uses WebSocket for real-time updates and falls back to in-memory channel layer if Redis is not running.

---
For more details, see `messaging/README.md` in the codebase.
