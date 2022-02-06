# OVH Telecom - Slack notifier

Sends a slack notification if you missed an OVH Voip call.

## Getting started
```
docker build -t medreda/slak_ovh_telecom_notifier .  
```
```
docker run --env-file ./.env  medreda/slak_ovh_notifier   
```
## Configuration needed

- CHECK_LAST_N_CALLS : Specifies the N last calls that should be checked (if missed or transferred to voicemail).
- OVH API Keys can be found [here](https://docs.ovh.com/fr/api/api-premiers-pas/#creer-les-cles-de-votre-application).
- The Slack OAuth token is to be configured pretty easily, [example](https://stackoverflow.com/a/44233400).

### Sample
``````

        Numéro    durée  raison                       date
--------------  -------  ---------------------------  -------------------------
 0033626XXXXXX        4  Transféré à la boite vocale  2022-02-06T09:45:16+01:00
   002125XXXXX        6  Transféré à la boite vocale  2022-02-01T19:42:44+01:00
``````
###.env content
``````
CHECK_LAST_N_CALLS=100

OVH_ENDPOINT=ovh-eu
OVH_APPLICATION_KEY=*********
OVH_APPLICATION_SECRET=***************************
OVH_CONSUMER_KEY=******************

OVH_SERVICE_NAME=003318******
OVH_BILLING_ACCOUNT=as6******-ovh-2

SLACK_OAUTH_TOKEN=xoxb-************************************
``````