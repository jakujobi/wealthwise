import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Message, Conversation
from .tasks import send_notifications_for_message
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            user = self.scope["user"]
            is_participant = await self.check_user_participation(user, self.conversation_id)
            if not is_participant:
                await self.close()
            else:
                self.room_group_name = f'chat_{self.conversation_id}'
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )
                await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            # Handle message deletion request
            if 'delete_id' in data:
                message_id = data['delete_id']
                user = self.scope['user']
                success = await self.delete_message_db(message_id, user)
                if success:
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'delete_message',
                            'message_id': message_id
                        }
                    )
                return
            message_text = data.get('message')
            user = self.scope["user"]

            if not message_text:
                logger.warning(f"Received empty message from user {user.id} in convo {self.conversation_id}")
                return

            msg_obj = await self.create_message(self.conversation_id, user, message_text)
            # Schedule notifications to other participants
            send_notifications_for_message.delay(msg_obj.id)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'id': msg_obj.id,
                    'message': message_text,
                    'sender': user.username,
                    'timestamp': str(msg_obj.timestamp)
                }
            )
        except json.JSONDecodeError:
            logger.error(f"Failed to decode JSON from WebSocket message: {text_data}", exc_info=True)
            await self.send(text_data=json.dumps({'error': 'Invalid JSON format.'}))
        except Exception as e:
            logger.exception(f"Error processing message in ChatConsumer for convo {self.conversation_id}: {e}")
            await self.send(text_data=json.dumps({'error': 'An internal error occurred.'}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'id': event['id'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))

    async def delete_message(self, event):
        await self.send(text_data=json.dumps({
            'delete_id': event['message_id']
        }))

    @database_sync_to_async
    def create_message(self, conversation_id, user, message_text):
        try:
            conversation = Conversation.objects.get(id=conversation_id)
            msg = Message.objects.create(
                conversation=conversation,
                sender=user,
                body=message_text
            )
            return msg
        except Conversation.DoesNotExist:
            logger.error(f"Attempted to create message for non-existent conversation {conversation_id} by user {user.id}")
            return None
        except Exception as e:
            logger.exception(f"Database error creating message for convo {conversation_id} by user {user.id}: {e}")
            return None

    @database_sync_to_async
    def check_user_participation(self, user, conversation_id):
        try:
            return Conversation.objects.filter(id=conversation_id, participants=user).exists()
        except Exception as e:
            logger.exception(f"Database error checking participation for user {user.id} in convo {conversation_id}: {e}")
            return False

    @database_sync_to_async
    def delete_message_db(self, message_id, user):
        try:
            conv_id = int(self.conversation_id)
            qs = Message.objects.filter(id=message_id, conversation_id=conv_id, sender=user)
            if not qs.exists():
                return False
            qs.delete()
            return True
        except Exception as e:
            logger.exception(f"Error deleting message {message_id} by user {user.id}: {e}")
            return False
