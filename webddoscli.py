# -*- coding: utf-8 -*-
import random

from colorama import Fore, Style

#is is
def fakeip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


print(Fore.GREEN + "╔═════════╣ About ╠══════════╗" + Style.RESET_ALL)
print(Fore.GREEN + "║+-     WebDDOScli V1.0    -+║" + Style.RESET_ALL)
print(Fore.GREEN + "║+- Made Proudly in India, -+║" + Style.RESET_ALL)
print(Fore.GREEN + "║+-    By Prattay Sarkar   -+║" + Style.RESET_ALL)
print(Fore.GREEN + "╚════════════════════════════╝" + Style.RESET_ALL)
print(Fore.RED + "╔═════════════╣ WARNING! ╠═════════════╗" + Style.RESET_ALL)
print(Fore.RED + "║+-   This Application is Created,   -+║" + Style.RESET_ALL)
print(Fore.RED + "║+-      FOR EDUCATION PURPOSES!     -+║" + Style.RESET_ALL)
print(Fore.RED + "║+- Please, Don't MISUSE This Tool!  -+║" + Style.RESET_ALL)
print(Fore.RED + "╚══════════════════════════════════════╝\n" + Style.RESET_ALL)
print(Fore.BLUE + "|+- Trying To Connect To URL...")
