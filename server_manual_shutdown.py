# Imports
import os
import subprocess
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])

def sms():
    number = request.form['From']
    message_body = request.form['Body']

    # Create a response object that we can send back to user
    resp = MessagingResponse()

    def shutdown():
        # Shutdown plex server via bash commands
        shutdown_success = 0
        # Unload the plist that keeps PMS alive
        shutdown_success = subprocess.call(["launchctl", "unload", "Library/Launn
chAgents/plex.agent.plist"])
        # Shutdown plex server via bash commands
        shutdown_success = 0
        # Unload the plist that keeps PMS alive
        shutdown_success = subprocess.call(["launchctl", "unload", "Library/LaunchAgents/plex.agent.plist"])
        # Exits PMS
        pgrep = subprocess.Popen(("pgrep", "-x", "Plex Media Server"), stdout=subprocess.PIPE)
        shutdown_success = subprocess.call(["xargs", "kill"], stdin=pgrep.stdout)
        return shutdown_success

    def restart():
        # Restart plex server via bash commands
        restart_success = 0
        restart_success = subprocess.call(["open", "/Applications/Plex Media Server.app"])
        restart_success = subprocess.call(["launchctl", "load", "Library/LaunchAgents/plex.agent.plist"])
        return restart_success

    # List of responses to user input
    def getReply(message):
        answer = ""
        if "0" in message:
            shutdown_status = shutdown()
            if shutdown_status == 0:
                answer = "Plex Media Server successfully shut down. REPLY 1 to restart server. Have a nice day."
            else:
                answer = "For some reason, we're unable to shut down Plex Media Server. Please access via terminal."
        elif "1" in message:
            restart_status = restart()
            if restart_status == 0:
                answer = "Plex Media Server successfully restarted. REPLY 0 to shut down server. Have a pleasant day."
            else:
                answer = "For some reason, we're unable to restart Plex Media Server. Please access via terminal."
        else:
            answer = "Welcome to the Plex Media Server SMS Control Panel <3 <3\n REPLY 0 to shut down server.\n REPLY 1 to start server.\n No other inputs accepted."
        return answer

    # Obtain the correct response based on what the user sent us
    respText = getReply(message_body)

    # Text our response back to the user
    resp.message(respText)
    return str(resp)

if __name__ == '__main__':
    app.run()
