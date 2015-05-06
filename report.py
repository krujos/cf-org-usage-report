#!/usr/bin/env python
#Script runs as whoever is logged into the CF API. 
from subprocess import check_output
import json 

orgs = json.loads(check_output(['cf', 'curl', '/v2/organizations']).decode('utf8'))
appcount = 0
appinstancecount = 0
for org in orgs['resources']:
    name = org['entity']['name']
    guid = org['metadata']['guid']
    quota_url = org['entity']['quota_definition_url']
    quota = json.loads(check_output(['cf', 'curl', quota_url]).decode('utf8'))
    quota_memory_limit = quota['entity']['memory_limit']
    used = json.loads(check_output(['cf', 'curl', '/v2/organizations/' + guid + '/memory_usage']).decode('utf8'))['memory_usage_in_mb']
    print "Org " + name + " is using " + str(used) + "MB of " + str(quota_memory_limit) + "MB."
    spaces_url = org['entity']['spaces_url']
    spaces = json.loads(check_output(['cf', 'curl', spaces_url]).decode('utf8'))
    for space in spaces['resources']:
        apps_url = space['entity']['apps_url']
        consumed = 0
        apps = json.loads(check_output(['cf', 'curl', apps_url]).decode('utf8'))
        for app in apps['resources']:
            instances = app['entity']['instances']
            memory = app['entity']['memory']
            consumed += (instances * memory)
            appcount = appcount + 1
            appinstancecount = appinstancecount + instances
        print "\tSpace " + space['entity']['name'] + " is using " + str(consumed) + "MB memory (" + str(100 * consumed / quota_memory_limit) + "%) of org quota"
print "You are running " + str(appcount) + " apps in all orgs, with a total of " + str(appinstancecount) + " instances"

                    


