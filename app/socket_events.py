from flask_socketio import emit, join_room, leave_room
from .db import messages_collection
from datetime import datetime

def register_socket_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')
        emit('message', {'msg': 'Connected to WebSocket!'})

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('join')
    def on_join(data):
        username = data['username']
        room = data['room']
        join_room(room)
        print(f"{username} joined room {room}")

        # Fetch last 20 messages from the room
        previous_messages = list(messages_collection.find({'room': room}).sort('timestamp', -1).limit(20))
        previous_messages.reverse()  # Oldest first

        # Format messages
        formatted = [
            {
                'username': msg['username'],
                'message': msg['message'],
                'timestamp': msg['timestamp'].isoformat()
            }
            for msg in previous_messages
        ]

        # Send only to the user who joined
        emit('message_history', formatted)

        # Let others in room know this user joined
        emit('message', {'msg': f'{username} has joined the room.'}, room=room)

    @socketio.on('leave')
    def on_leave(data):
        username = data['username']
        room = data['room']
        leave_room(room)
        emit('message', {'msg': f'{username} has left the room.'}, room=room)
        print(f'{username} left room {room}')

    @socketio.on('send_message')
    def handle_message(data):
        username = data['username']
        room = data['room']
        message = data['message']
        timestamp = datetime.utcnow()

        # Save message
        messages_collection.insert_one({
            'username': username,
            'room': room,
            'message': message,
            'timestamp': timestamp
        })

        emit('message', {
            'username': username,
            'message': message,
            'timestamp': timestamp.isoformat()
        }, room=room)
