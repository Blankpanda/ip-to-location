import sys, re, socket, json, codecs
import website

from urllib.request import urlopen

# save the user input
def set_user_input(inp):
    global user_input
    user_input = inp


def find(input):
    if is_ip_addr(input):
        #its a ip address
        if is_valid_ip_addr(input):
            set_user_input(input)
            query_api(input)
        else:
            print("IP is not public.")
    else:
        # its a hostname
        input = remove_protocol(input) # removes http:// or https:// from the strin
        if is_valid_host_name(input):
            set_user_input(input)
            input = convert_to_ip(input)
            query_api(input)

        else:
            print("Hostname is invalid.")



def is_ip_addr(input):
    octets = input.split(".")
    nc = int() # number count
    for octet in octets:
        if octet.isnumeric():
            nc += 1

    if len(octets) == 4 and nc == 4: # if string has 4 octets and all numbers
        return True
    else:
        return False

def is_valid_host_name(input):
    regex_pattern = r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
    if len(input) > 255: # maximum characters for a hostname
        return False
    else:
        hostname = re.search(regex_pattern, input)
        if hostname == None:
            return False
        else:
            return True


def is_valid_ip_addr(ip): # lmao should of used a regex
    octets = ip.split(".")
    b_second_octets = list(range(16,32))

    # the elements of the list need to be a string
    for i in range(0,len(b_second_octets)): b_second_octets[i] = str(b_second_octets[i])
    # class A,B,C, localhost, APIPA
    if octets[0] == "127":  return False
    if octets[0] == "10":  return False
    if octets[0] == "172" and octets[1:2][0] in b_second_octets:    return False
    if ".".join(octets[:2]) == "169.254":   return False
    if ".".join(octets[:2]) == "192.168":   return False

    return True

def remove_protocol(hostname):
    if hostname.startswith("http"):
        hostname  = hostname[7:]
    elif hostname.startswith("https"):
        hostname = hostname[8:]
    return hostname

def convert_to_ip(hostname):
    hostname = socket.gethostbyname(hostname)
    return hostname


def query_api(ip):
    url = 'http://ipinfo.io/' + ip + "/json"
    reader = codecs.getreader("utf-8")
    response = urlopen(url)
    json_data = json.load(reader(response))
    print("Done.  Building website.")
    website.build(json_data)
