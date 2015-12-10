import sys, atexit, os
import locator


def main():
     name = input("Enter in an IP address or domain name:")

     if name == "":
         print("Please enter in a IP or domain name.")
     else:
         print("searching...")
         locator.find(name)


if __name__ == '__main__':
    main()
