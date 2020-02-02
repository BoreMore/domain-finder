from termcolor import colored
import json
import time
import requests
import sys

# godaddy api key
headers = {
    'Authorization': '',
}


def appraise(input, output):
    counter = 0
    connection_timeout = 0

    appraisal = open(output, 'a')
    # some domains get passed due to connection errors, so they get stored in this file
    passed = open('passed.txt', 'a')

    # reads input file
    with open(input) as file:
        for line in file:
            # pauses for 48 seconds due to API limit after appraising 20 names
            if counter % 20 == 0 and counter != 0:
                time.sleep(48)
            try:
                # uses API to get domain value
                response = requests.get('https://api.godaddy.com/v1/appraisal/' + line.rstrip('\n'), headers=headers)
                response = response.json()
                try:
                    # prints domain in green if value is over 1000 and writes to file
                    if not(response['govalue'] < 1000):
                        print(colored(response['domain'] + ", " + str(response['govalue']), 'green'))
                        appraisal.write('\n' + response['domain'] + ", " + str(response['govalue']))
                    # prints domain in red if value is under 1000 and writes to file
                    else:
                        print(colored(response['domain'] + ", " + str(response['govalue']), 'red'))
                        appraisal.write('\n' + response['domain'] + ", " + str(response['govalue']))
                    counter += 1
                    connection_timeout = 0
                except:
                    # if API limit is reached, write to passed file and retry after specified seconds
                    if response['code'] == 'TOO_MANY_REQUESTS':
                        print(response)
                        passed.write(line)
                        time.sleep(response['retryAfterSec'])
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
                    passed.write(line)
                    time.sleep(1)


    appraisal.close()
    passed.close()

# takes args for input (file with list of domains to appraise) and output (file to write appraisal values to)
if __name__ == "__main__":
    input = sys.argv[1]
    output = sys.argv[2]
    appraise(input, output)