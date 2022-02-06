import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackApi:
    def __init__(self):
        self.client = WebClient(token=os.environ['SLACK_OAUTH_TOKEN'])

    def send_slack_msg(self, msg, in_channel='#notifications'):
        try:
            response = self.client.chat_postMessage(channel=in_channel, text=msg)
            assert response["message"]["text"] == msg
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")