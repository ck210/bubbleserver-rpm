#!/bin/bash
#
#	/etc/rc.d/init.d/bubbleserver
#
# Starts the BubbleUPnPServer daemon
#
# chkconfig: 345 20 80
# description: BubbleUPnPServer
# processname: java BubbleUPnPServer.jar

### BEGIN INIT INFO
# Provides: BubbleUPnPServer
# Defalt-Start: 3 4 5
# Default-Stop: 0 2 1 6
# Description: BubbleUPnPServer
### END INIT INFO

. /etc/rc.d/init.d/functions

NAME=bubbleserver
DESC="Bubble Server Upnp Proxy"

if [ `id -u` -ne 0 ]; then
   echo "You need root privileges to run this script"
   exit 1
fi


# Define other required variables
PID_FILE=/var/run/$NAME.pid
USER=bubbleserver

DAEMON_PATH="/opt/bubbleserver"

DAEMON="java -Xss256k -Djava.awt.headless=true -Djava.net.preferIPv4Stack=true -Dfile.encoding=\"UTF-8\" -jar BubbleUPnPServerLauncher.jar"
DAEMON_OPTS=""

#
# Function that starts the daemon/service
#
do_start()
{

  if [ -z "$DAEMON" ]; then
    echo "not found - $DAEMON"
    exit 1
  fi

  if pidofproc -p "$PID_FILE" >/dev/null; then
    exit 0
  fi
  
  # to make sure ffmpeg is found and used if present in start directory
  export PATH=.:${PATH}

  cd $DAEMON_PATH
  echo -n "Starting $DESC: "
  runuser -s /bin/sh -c "exec $DAEMON $DAEMON_OPTS" ${USER} > /dev/null 2>&1 &

  RETVAL=$?
  local PID=$!
  # runuser forks rather than execing our process.
  usleep 500000
  JAVA_PID=$(ps axo ppid,pid | awk -v "ppid=$PID" '$1==ppid {print $2}')
  PID=${JAVA_PID:-$PID}
  echo $PID > $PID_FILE
  [ "$PID" = "$JAVA_PID" ] && success
}

#
# Function that stops the daemon/service
#
do_stop()
{
  echo -n "Stopping $DESC: "
  if [ -f $PID_FILE ]; then
    PID=`cat $PID_FILE`
    kill -9 $PID
    RETVAL=$?
    [ $RETVAL = 0 ] && rm -f ${PID_FILE} && success # $"Ok"
  else
      failure $"pidfile not found"
  fi
  echo
}

case "$1" in
  start)
    do_start
    ;;
  stop)
    do_stop
    ;;
  restart|reload)
    do_stop
    do_start
    ;;
  status)
    echo -n "$DESC"
    status -p $PID_FILE
    exit $?
    ;;
  *)
    echo "Usage: $SCRIPTNAME {start|stop|status|restart}" >&2
    exit 3
    ;;
esac

echo
exit 0