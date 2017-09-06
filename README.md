# cron1min-pylogs101
Cron task every minute with basic python logging

# Project Purpose
On Linux OS make crontab execute file `cron1min.py` once every minute to test cron and learn basic python logging.

# Project Files
`appconf.py` - application configuration

`cron1min.py` - application code

`cron1min.info` - empty log file

`cron1min.ctxt` - empty text file for console redirect

`cron1min.dbug` - empty debug log file

# Resources

Configuration file `appconf.py` derives from dikei/Dictconfig example https://gist.github.com/dikei/1500194 which shows how to configure basic logging by incorporating (or importing) a specified python dictionary; and also derives from this reference, https://stackoverflow.com/questions/21455515/install-filter-on-logging-level-in-python-using-dictconfig, which shows how to install a filter in the logging dictionary configuration.

Why Crontab Scripts Are Not Working?
https://askubuntu.com/questions/23009/why-crontab-scripts-are-not-working

Run a Crontab Job Using Anaconda Environment?
https://stackoverflow.com/questions/36365801/run-a-crontab-job-using-an-annaconda-env

# Project Folder

Save the project files in a project folder owned by the Linux User such as the following:
```
/media/Users/YourUserName/ProjFolder
```

# Crontab Task Add/Enable
Execute crontab:
```
user:~$ crontab -e 
```
Add enabled cron task [1] to crontab via default editor:
```
# [1] task below runs once every minute to test cron functionality and basic python logging
* * * * * python /media/Users/UserName/ProjFolder/cron1min.py >> /media/Users/UserName/ProjFolder/cron1min.ctxt 2>&1
```
The task [1] setup shown above includes the absolute path to the project folder and redirects the console log output to the file `cron1min.ctxt` inside the project folder.

Activate the debug file to show the python version executed by the crontab. 

You may need to add the python environment path in crontab as described in these resources: 

Why Crontab Scripts Are Not Working?
https://askubuntu.com/questions/23009/why-crontab-scripts-are-not-working

Run a Crontab Job Using Anaconda Environment?
https://stackoverflow.com/questions/36365801/run-a-crontab-job-using-an-annaconda-env

# Monitor Dynamic Output

Add/enable crontab task [1] as shown above then navigate to the project folder.

To monitor log file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.info
2017-09-02 16:00:01 INFO    Sat Cron fired
2017-09-02 16:01:01 INFO    Sat Cron fired 
```
To monitor text file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.ctxt
2017-09-02 16:00:01 INFO    Sat Cron fired
2017-09-02 16:01:01 INFO    Sat Cron fired 
```
To monitor debug log file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.dbug

```
The debug log is disabled by default in file `appconf.py` so its output will be blank. Remove the leading `#` sign in `appconf.py` to enable debug log output. Insert the leading `#` sign in `appconf.py` to disable debug log output. 

# Crontab Task Disable
Execute crontab:
```
user:~$ crontab -e 
```
To disable task [1] insert a leading `#` sign in second line as shown below:
```
# [1] task below runs once every minute to test cron functionality and basic python logging
#* * * * * python /media/Users/UserName/ProjFolder/cron1min.py >> /media/Users/UserName/ProjFolder/cron1min.ctxt 2>&1
```

# Clear Output Files

Disable crontab task [1] as shown above then navigate to the project folder.

Clear log file:
```
~$ > cron1min.info
```
Clear text file:
```
~$ > cron1min.ctxt
```

Clear debug log file:
```
~$ > cron1min.dbug
```
