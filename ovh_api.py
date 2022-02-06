import json
import ovh
import os

class OvhApi:
    serviceName = os.environ['OVH_SERVICE_NAME']
    billingAccount = os.environ['OVH_BILLING_ACCOUNT']
    CHECK_LAST_N_CALLS = int(os.environ['CHECK_LAST_N_CALLS'])

    def __init__(self):
        self.client = ovh.Client(
            endpoint=os.environ['OVH_ENDPOINT'],  # Endpoint of API OVH Europe (List of available endpoints)
            application_key=os.environ['OVH_APPLICATION_KEY'],  # Application Key
            application_secret=os.environ['OVH_APPLICATION_SECRET'],  # Application Secret
            consumer_key=os.environ['OVH_CONSUMER_KEY'],  # Consumer Key
        )
    
    def get_missed_calls(self):
        
        consumptionIds = self.client.get(f'/telephony/{self.billingAccount}/service/{self.serviceName}/voiceConsumption')
        
        calls = []
        for call in consumptionIds[:self.CHECK_LAST_N_CALLS]:
            result = self.client.get(f'/telephony/{self.billingAccount}/service/{self.serviceName}/voiceConsumption/' + str(call))
            calls.append(result)

        latestInteractions = []
        for call in reversed(calls):
            # If this is the latest call from the 'calling' person
            if not next((c for c in latestInteractions if call["calling"] in (c["calling"], c["called"])), False):
                latestInteractions.append(call)
        
        missedPhoneCalls = []
        for call in latestInteractions:
            if (call["wayType"] == "transfer" or call["hangupNature"] == "missed") and call["called"] == self.serviceName:
                missedPhoneCalls.append(call)
        
        return missedPhoneCalls
