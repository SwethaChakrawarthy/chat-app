from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    print(app.url_map)  # ✅ Helps us debug routes
    socketio.run(app, debug=True, host='0.0.0.0', port=5050)

