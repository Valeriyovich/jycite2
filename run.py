from app import app, manager, socketio


if __name__ == "__main__":
    socketio.run(app)
