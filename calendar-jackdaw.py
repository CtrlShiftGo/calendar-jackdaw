#!/usr/bin/env python

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

class CalendarParser:
    """Calendar parsing class"""

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def __init__(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)
        return

    def get_tag(tag_file_name, calendar_event):
        tags = open(str(tag_file_name), 'r')
        # Parse tags
        for lines in tags:
            # Check for subtags

            if line[0] == " ":
                # Line is a tag subset
                previous_line = line

    def get_calendar(self, calendar_name):
        calendar_list = self.service.calendarList().list().execute()
        for calendar in calendar_list['items']:
            if(calendar_name in calendar['summary']):
                return calendar['id']
        return None

    def get_events(self, calendar_name):
        eventResults = self.service.events().list(
            calendarId=self.get_calendar(calendar_name), maxResults=100,
            singleEvents=True, orderBy='startTime').execute()
        return eventResults.get('items', [])

    def conv_time(self, time_str):
        date = datetime.datetime.strptime(time_str, "%Y-%M-%d")
        return date.isoformat("T") + "-08:00"

if __name__ == '__main__':
    if(len(os.sys.argv) < 2 or len(os.sys.argv) > 3):
        print
        # print("Incorrect Usage")
        # print("Usage Example")
    parser = CalendarParser()
    print(parser.get_calendar("1. Health and Fitness"))
