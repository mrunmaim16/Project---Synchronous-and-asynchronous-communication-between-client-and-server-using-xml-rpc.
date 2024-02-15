from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

SERVER = SimpleXMLRPCServer(('localhost', 5050), logRequests = True)

# Client upload file to server
def server_download(file_binary, file_name):
    filepath = "./server/" + file_name
    with open(filepath, "wb") as file:
        file.write(file_binary.data)
    return True

# Delete file from server
def server_delete(file_name):
    filepath = "./server/" + file_name
    if os.path.exists(filepath):
        os.remove(filepath)
        result = "Removed " + file_name + " from the server"
        return result
    else:
        result = "File not exists in the server"
        return result

# Main function
def main():
    try:
        # Functions exceuted by client
        SERVER.register_function(server_download)
        SERVER.register_function(server_delete)
        print('Serving..')
        SERVER.serve_forever()
    except KeyboardInterrupt:
        print("Existing Server")

# Execution start
if __name__ == "__main__":
    main()