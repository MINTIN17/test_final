import os
import threading
from Demo_web.application.Server_socket import utils
from Demo_web.application import app, socketio

# if __name__ == "__main__":
#     # socket_thread = threading.Thread(target=utils.start_socket_server)
#     # socket_thread.start()
#     socketio.run(app)
#     app.run(host='0.0.0.0', port=5000)
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    
if __name__ == '__main__':
    socket_path = os.environ.get("WERKZEUG_SERVER_UNIX_SOCKET")
    print(socket_path)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

