import threading
import random
import xmlrpc.client

# Global variable
PROXY = xmlrpc.client.ServerProxy("http://localhost:5050")

MENU = {1: "Synchronous Addition", 2: "Asynchronous Addition", 3: "Synchronous Sort", 
            4: "Asynchronous Sort", 5: "Asynchronous result", 6: "Exit"}


# code to track thread status
threads = []


'''
 code block for performing asynchronus addition 
 and creating a 'Key' which refers to a result 
 '''
def asyncroAdd():
    no1 = int(input("Enter first number to calculate asynchronous addition:"))
    no2 = int(input("Enter second number to calculate asynchronous addition:"))
    threadId = "AddKey-" + str(random.randint(0,9))
    res = threading.Thread(target=PROXY.async_addition, args=(no1, no2, threadId,))
    threads.append(res)
    print(f"Asynchronous add id: {threadId}")
    res.start()
    res.join()

'''
code for synchronus sorting on 
entered array elements is performed 
here
'''
def syncroSort():
    array = [data for data in input("Enter array elements to be sorted: (Example: 5, 2, 7, 6) ").split()]
    res = PROXY.sync_array_sort(array)
    print(res)

'''
code for asynchronus sorting 
which accepts array elements, 
creating a 'Key'
which refers to a result of sorted array
'''
def asyncroSort():
    array = [data for data in input("Enter array elements to be sorted: (Example: 5, 2, 7, 6) ").split()]
    threadId = "SortKey-" + str(random.randint(0,9))
    res = threading.Thread(target=PROXY.async_array_sort, args=(array,  threadId,))
    threads.append(res)
    print(f"Asynchronous add id: {threadId}")
    res.start()
    res.join()

       
# main method
def main():
    # Menu running till user chooses to exit 
    while True:
        # displaying Menu
        for key in MENU.keys():
            print(key, MENU[key])
        option = " "
        try:
            selection = int(input("Enter your choice from above list: "))
            if selection > 6 and selection < 1:
                print('Invalid option. Please try again! ')
            
        except ValueError:
            print("Invalid option. Please try again! ")
        if selection == 1:
            # block of code to perform synchronus addition 
            ip1 = input("Enter First Number to calculate synchronous addition: ")
            ip2 = input("Enter Second Number to calculate synchronous addition: ")
            res = PROXY.sync_addition(ip1, ip2)
            print(res)
        elif selection == 2:
            asyncroAdd()
        elif selection == 3:
            syncroSort()
        elif selection == 4:
            asyncroSort()
        elif selection == 5:
            status = input("Enter id: ")
            print(PROXY.async_thread_res(status))
        elif selection == 6:
            print("Exiting client..")
            exit()
        
# Execution starts
if __name__ == "__main__":
    main()