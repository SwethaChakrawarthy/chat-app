from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)  # ✅ This is CRUCIAL
    
    print("✅ Blueprint registered!")


    from .socket_events import register_socket_events
    register_socket_events(socketio)

    socketio.init_app(app)
    return app
