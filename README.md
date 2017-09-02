# cron1min-pylogs101
One minute cron interval test with basic python logging application

# Project Purpose
On Linux OS make crontab execute file `cron1min.py` once every minute to test cron and learn basic python logging.

# Project Files
`appconf.py` - application configuration

`cron1min.py` - application code

`cron1min.log` - log file

`cron1min.txt` - text file for console redirect

`cron1min.dbg` - debug log file

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
* * * * * python /media/Users/UserName/ProjFolder/cron1min.py >> /media/Users/UserName/ProjFolder/cron1min.txt 2>&1
```
The task [1] setup shown above includes the absolute path to the project folder and redirects the console log output to the file `cron1min.txt` inside the project folder.

# Monitor Dynamic Output

Add/enable crontab task [1] as shown above then navigate to the project folder.

To monitor log file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.log
2017-09-02 16:00:01 INFO    Sat Cron fired
2017-09-02 16:01:01 INFO    Sat Cron fired 
```
To monitor text file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.txt
2017-09-02 16:00:01 INFO    Sat Cron fired
2017-09-02 16:01:01 INFO    Sat Cron fired 
```

To monitor debug log file (`Ctrl-C` to cancel):
```
~$ tail -f cron1min.dbg

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
#* * * * * python /media/Users/UserName/ProjFolder/cron1min.py >> /media/Users/UserName/ProjFolder/cron1min.txt 2>&1
```

# Clear Output Files

Disable crontab task [1] as shown above then navigate to the project folder.

Clear log file:
```
~$ > cron1min.log
```
Clear text file:
```
~$ > cron1min.txt
```

Clear debug log file:
```
~$ > cron1min.dbg
```
