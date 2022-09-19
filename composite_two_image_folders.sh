#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


python $SCRIPT_DIR/composite_two_image_folders.py "$@"
