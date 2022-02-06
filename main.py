import tabulate

from ovh_api import OvhApi
from slack_api import SlackApi

class SlackOVhTelecomNotifier:
    def __init__(self):
        ovh = OvhApi()
        self.missed_calls = ovh.get_missed_calls()

    def pretty_print(self, calls_list):
        header =['Numéro', 'durée', 'raison', 'date']
        rows = [[x['calling'],x['duration'],'Sans réponse' if not x['wayType'] == 'transfer' else 'Transféré à la boite vocale',x['creationDatetime']] for x in calls_list]
        return tabulate.tabulate(rows, header,   tablefmt="simple")

    def send_notification(self):
        slack = SlackApi()
        tableau = self.pretty_print(self.missed_calls)
        print(tableau)
        msg = 'Liste des appels manquès, merci de rappeler les numéros suivants :  \n' + tableau
        slack.send_slack_msg(msg)

if __name__ == '__main__':
    notifier = SlackOVhTelecomNotifier()
    notifier.send_notification()
