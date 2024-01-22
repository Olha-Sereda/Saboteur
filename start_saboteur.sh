#!/bin/bash
PYTHON_EXEC="/usr/local/bin/python3.11"
APP_PATH="/home/epi/21_sereda/G_projekt/app.py"

start() {
    echo "Game Saboteur has been started..."
    nohup $PYTHON_EXEC $APP_PATH &
}

stop() {
    echo "Game Saboteur has been stopped..."
    pkill -f "$APP_PATH"
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0