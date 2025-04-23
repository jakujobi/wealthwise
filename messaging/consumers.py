import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Conversation, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.group_name = f"chat_{self.conversation_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data.get('message')
        user = self.scope['user']
        # Save message to the database
        msg_obj = await self.create_message(self.conversation_id, user, message_text)
        payload = {
            'id': msg_obj.id,
            'sender': user.username,
            'body': msg_obj.body,
            'timestamp': msg_obj.timestamp.isoformat(),
        }
        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': payload,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    @database_sync_to_async
    def create_message(self, convo_id, user, body):
        conv = Conversation.objects.get(id=convo_id)
        msg = Message.objects.create(conversation=conv, sender=user, body=body)
        return msg
