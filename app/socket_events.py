from flask_socketio import emit

def register_socket_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')
        emit('message', {'msg': 'Connected to WebSocket!'})

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')
