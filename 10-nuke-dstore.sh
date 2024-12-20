#!/bin/bash
# macOS Finder likes to litter the file system with these
# Nuke them all from the current directory down..
find . -name ".DS_Store" -print -delete
