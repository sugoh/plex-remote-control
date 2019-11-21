# Source shell configurations
source ~/.zshrc

if ! pgrep -x Plex\ Media\ Server
  then
    # Start PMS
    open /Applications/Plex\ Media\ Server.app
    # Upon success or failure, send SMS notification to user
    if [ $? -eq 0 ]
      then
        python3 /Users/YOUR_USER/server_restart_success.py
    else
      python3 /Users/YOUR_USER/server_restart_failure.py
    fi
fi
