import webbrowser
import time

Url = input("Enter URL: ")
Duration = int(input("Enter Duration: "))
Times = int(input("How many times would you like to view?"))

for x in range(Times):
    webbrowser.open(Url)
    time.sleep(Duration)