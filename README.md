# Plex Remote Control
Plex Remote Control is a collection of scripts and configurations that make remote management of Plex Media Servers easier.

**Key features**
- Crash monitoring + auto restart: monitors if Plex Media Server app crashes and automatically restarts app
- SMS notification: Sends SMS to notify user of Plex Media Server app status changes (crashes, restarts, user termination)
- Start/Stop Control via SMS: Allows user to terminate or start Plex Media Server via SMS commands

# How to setup
Copy plex.agent.plist to your home directory's LaunchAgents folder:
```
cp /PATH/TO/plex.agent.plist ~/Library/LaunchAgents
```
Copy all other files into your home directory:
- restart\_plex.sh
- server\_down.py
- server\_manual\_shutdown.py
- server\_restart\_success.py
- server\_restart\_failure.py
Modify the code in the above files to point to the correct directories and phone numbers \(to receive / send SMS\)
Install Twilio helper library for Python:
```
pip3 install twilio
```
Edit your shell profiles by adding the following lines to .zshrc or .bashrc:
```
export TWILIO_ACCOUNT_SID=INSERT_ID_HERE
export TWILIO_API_KEY=INSERT_API_KEY_HERE
export TWILIO_API_SECRET=INSERT_API_SECRET_HERE
```
Load the launch agent:
```
Launchctl load ~/Libary/LaunchAgents/plex.agent.plist
```
The Plex Media Server app should automatically open. Congrats! You're all set.

# How to use
- To shut Plex Media Server app down via SMS, text "0" to your Twilio phone number. \(Note that this also disables the crash notification + auto-restart feature\)
- To start the app via SMS, text "1" to your Twilio phone number
