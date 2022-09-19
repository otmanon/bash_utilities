#!/bin/bash
ffmpeg -i $1 -filter_complex 'fps=24,scale=1080:-1:flags=lanczos,split [o1] [o2];[o1] palettegen
 [p]; [o2] fifo [o3];[o3] [p] paletteuse' $2
