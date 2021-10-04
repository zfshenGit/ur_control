#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/zfshen/ur5_ws_szf/src/universal_robot/ur_kinematics"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/zfshen/ur5_ws_szf/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/zfshen/ur5_ws_szf/install/lib/python2.7/dist-packages:/home/zfshen/ur5_ws_szf/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/zfshen/ur5_ws_szf/build" \
    "/usr/bin/python2" \
    "/home/zfshen/ur5_ws_szf/src/universal_robot/ur_kinematics/setup.py" \
     \
    build --build-base "/home/zfshen/ur5_ws_szf/build/universal_robot/ur_kinematics" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/zfshen/ur5_ws_szf/install" --install-scripts="/home/zfshen/ur5_ws_szf/install/bin"
