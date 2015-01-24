#!/usr/bin/env python
#Script runs as whoever is logged into the CF API. 
from subprocess import check_output
import json 

orgs = json.loads(check_output(['cf', 'curl', '/v2/organizations']))

for org in orgs['resources']:
    name = org['entity']['name']
    guid = org['metadata']['guid']
    quota_url = org['entity']['quota_definition_url']
    quota = json.loads(check_output(['cf', 'curl', quota_url]))
    quota_memeory_limit = quota['entity']['memory_limit']
    used = json.loads(check_output(['cf', 'curl', '/v2/organizations/' + guid + '/memory_usage']))['memory_usage_in_mb']
    print "Org " + name + " is using " + str(used) + " of " + str(quota_memeory_limit)



