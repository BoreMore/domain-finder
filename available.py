#curl -X GET -H'Authorization: sso-key [API_KEY]:[API_SECRET]''https://api.godaddy.com/v1/domains/available?domain=example.guru'

from termcolor import colored
import json
import time
import requests
import sys

# godaddy api key
headers = {
    'Authorization': '',
}

def check(input, output):
    counter = 0
    connection_timeout = 0

    available = open(output, 'a')
    # some domains get passed due to connection errors, so they get stored in this file
    passed = open('passed.txt', 'a')

    # reads input file
    with open(input) as file:
        for line in file:
            # pauses for 30 seconds due to API limit after checking 120 names
            if counter % 120 == 0 and counter != 0:
                time.sleep(30)
            try:
                # uses API to get domain value
                response = requests.get('https://api.godaddy.com/v1/domains/available?domain=' + line.rstrip('\n') + '.com', headers=headers)
                response = response.json()
                try:
                    # prints domain in green if it is available or not definitively unavailable and writes to file
                    if not(response['available'] == False and response['definitive'] == True):
                        print(colored(response, 'green'))
                        available.write('\n' + response['domain'])
                    # prints domain in red if it is unavailable
                    else:
                        print(colored(response, 'red'))
                    counter += 1
                    connection_timeout = 0
                # waits 30 seconds if API limit is reached
                except:
                    print(response)
                    passed.write(line)
                    if response['code'] == 'TOO_MANY_REQUESTS':
                        time.sleep(30)
                    pass
            except requests.ConnectionError:
                # if internet disconnects, notify user and stop script
                if connection_timeout == 300:
                    raise Exception('Unable to get updates after {} tries to reconnect'.format(connection_timeout))
                    print("Stopped at keyword " + line)
                    exit()
                # if internet disconnects, try to reconnect
                else:
                    connection_timeout += 1
                    print("Connection error... trying to reconnect. Attempt: " + str(connection_timeout))
                    passed.write(line.replace(" ", ""))
                    time.sleep(1)

    available.close()
    passed.close()

# takes args for input (file with word list) and output (file to write available domain names to)
if __name__ == "__main__":
    #file to read
    input = sys.argv[1]
    #file to print to
    output = sys.argv[2]
    check(input, output)