#Report on memory usage of Cloud Foundry Orgs

This is a sample script to report on the amount of memory used against the currently applied quota. It uses CF curl and the currently logged in user to access the [Cloud Controller rest API](http://apidocs.cloudfoundry.org/). This script is written against v196 but is expected to work against any release. Should you have a problem please open an issue.

##Usage

```
➜  org-quota-reporting git:(master) ./report.py                                                                                                                                                                                                                              
Org pivotalservices is using 5504 of 102400
Org krujos is using 768 of 10240
Org pcfp is using 1024 of 10240
```

## Known issues
If an org or space doesn't contain the fields we're asking for in the script it does not fail gracefully. 