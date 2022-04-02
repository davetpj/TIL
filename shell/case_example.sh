#!/bin/bash

case $1 in
  start)
    echo "Start"
    ;;
  stop)
    echo "Stop"
    ;;
  *)
    echo "Please input sub command"
esac
