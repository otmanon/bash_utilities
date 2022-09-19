#!/bin/bash
echo "Making video from images in directoy $1..."
ffmpeg.exe -i $1/%4d.png -q:v 3 -s 1920x1080 -vcodec mpeg4 -pix_fmt yuv420p $2.mp4
