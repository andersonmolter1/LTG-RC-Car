Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jun  9 00:38:15 2021 from 192.168.1.11
pi@herolabcar:~ $ sudo systemctl status LTG.service
● LTG.service - My service
   Loaded: loaded (/etc/systemd/system/LTG.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2021-06-09 00:39:31 BST; 2min 26s ago
 Main PID: 472 (python3)
    Tasks: 4 (limit: 725)
   CGroup: /system.slice/LTG.service
           └─472 /usr/bin/python3 -u main.py

Jun 09 00:39:31 herolabcar systemd[1]: Started My service.
Jun 09 00:39:38 herolabcar python3[472]: Motor initialized.
Jun 09 00:39:38 herolabcar python3[472]: Motor enabled
Jun 09 00:39:39 herolabcar python3[472]: 60016
Jun 09 00:39:39 herolabcar python3[472]: 16006
pi@herolabcar:~ $ sudo poweroff
pi@herolabcar:~ $
Remote side unexpectedly closed network connection

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Session stopped
    - Press <return> to exit tab
    - Press R to restart session
    - Press S to save terminal output to file

