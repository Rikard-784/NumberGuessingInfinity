import socket
 # Proceed with caution.
def start_client():
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server!")
        play_game(s)

