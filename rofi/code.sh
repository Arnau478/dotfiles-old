#!/usr/bin/env zsh

if [ -z "$@" ]
then
    ls
else
    alacritty &!
    exit 0
fi
