# Messaging

This directory contains the code for WealthWise's real-time messaging feature.

## Overview
The `messaging` app enables users to have real-time conversations powered by Django Channels (WebSockets) with a fallback InMemory channel layer for local development.

## Setup
1. Ensure you have the dependencies installed: `pip install -r requirements.txt`
2. Configure environment variables in `.env`:
   ```bash
   REDIS_URL=redis://127.0.0.1:6379
   ```
3. (Optional) Start Redis:
   ```bash
   docker run -d --name redis -p 6379:6379 redis:latest
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

## Code Structure
- `consumers.py`: WebSocket consumer handling connect, receive, disconnect and group operations.
- `views.py`: REST viewsets for conversations and messages.
- `serializers.py`: DRF serializers for Conversation and Message models.
- `routing.py`: WebSocket URL routing to `ChatConsumer`.
- `templates/messaging/index.html`: Front-end UI and JavaScript for real-time messaging.

## Testing
Run `pytest` to execute unit tests for the messaging app.
