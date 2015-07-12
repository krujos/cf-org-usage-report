THIS REPOSITORY IS DEPRECATED
=============================

I've written a CLI plugin which acheives the same means. Please use it!
https://github.com/krujos/usagereport-plugin

#Report on memory usage of Cloud Foundry Orgs and Spaces.

This is a sample script to report on the amount of memory used against the currently applied quota. It uses CF curl and the currently logged in user to access the [Cloud Controller rest API](http://apidocs.cloudfoundry.org/). It assumes the CF cli is in your path.  This script is written against v204 but is expected to work against any release. Should you have a problem please open an issue.

##Usage

```
➜  org-quota-reporting git:(master) ./report.py                                                                                 
Org pcfp is using 5888MB of 102400MB.
	Space development is using 0MB memory (0%) of org quota
	Space docs-staging is using 1024MB memory (1%) of org quota
		 running 2 apps with 4 instances
...
Org testdrive is using 1344MB of 10240MB.
	Space development is using 1344MB memory (13%) of org quota
		 running 4 apps with 4 instances

You are running 23 apps in all orgs, with a total of 37 instances
➜  org-quota-reporting git:(master)
```
## Known issues
If an org or space doesn't contain the fields we're asking for in the script it does not fail gracefully. 
