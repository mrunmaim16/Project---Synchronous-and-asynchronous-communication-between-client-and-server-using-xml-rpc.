from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# Global variable
SERVER = SimpleXMLRPCServer(('localhost', 5050))
THREAD_CLIENT = {}

# code of Synchronus addition
def sync_addition(ip1, ip2):
    return int(ip1) + int(ip2)

# code of Asynchronus Addition
def async_addition(no1, no2, thread_id):
    result = no1 + no2
    THREAD_CLIENT.update({thread_id: result})
    return True

# Synchronus sorting of entered array
def sync_array_sort(client_array):
    client_array.sort()
    print(client_array)
    return client_array

# Asynchronus sorting of entered array
def async_array_sort(client_array, thread_id):
    client_array.sort()
    THREAD_CLIENT.update({thread_id: client_array})
    return True


# Storing thread result as dictionary in THREAD_CLIENT list
def async_thread_res(status):
    try:
        return THREAD_CLIENT[status]
    except KeyError:
        exception = "Entered ID is not present. Enter valid id!!"
        return exception

# Main block
def main():
    # Register function to call from code of client side 
    SERVER.register_function(sync_addition)
    SERVER.register_function(async_addition)
    SERVER.register_function(sync_array_sort)
    SERVER.register_function(async_array_sort)
    SERVER.register_function(async_thread_res)
    # server started
    SERVER.serve_forever()

# Execution point of entry
if __name__ == "__main__":
    try:
        print("SERVER Started..")
        main()
    except KeyboardInterrupt:
        print("Exiting Server")