from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Motion Blurs Frames from <input_dir>, starting at frame <frame_start> and ' +
                                             'grabbing the <range> frames behind it. The resulting blurred image is outputted in <output>.png')
parser.add_argument('--input_dir', default='C:/Users/otman/OneDrive/Desktop/fastCD/fastComplementaryDynamicsCpp/results/reduction_vs_coarse/glob_tree_cage/screenshots',
                    help='input director full of animation frames')
parser.add_argument('--frame_start', default=10,
                    help='which frame should we start out at')
parser.add_argument('--range', default=10, help='how many frames back do we want to motion blur this frame wiht')
parser.add_argument('--output', default='./result.png', help='where to print output')
parser.add_argument('--max_blur_alpha', default=64, help='the alpha value of the first frame behind the previous frame')
parser.add_argument('--zfill', default=4, help='frames are numbered from 0 to n. how many chars do these frames use for their numbering system')
args = parser.parse_args()
parser.print_help()

frame_number = args.frame_start;
input_dir = args.input_dir;


foreground = Image.open( args.input_dir + "/" + str(frame_number).zfill(4) + ".png")
#foreground.show()
for i in range(0, int(args.range)):
    background = Image.open(args.input_dir + "/" + str(int(frame_number) - i).zfill(4) + ".png")

    alpha_channel = background.getchannel('A')
    new_alpha_channel = alpha_channel.point(lambda ind: int(args.max_blur_alpha)  - (int(args.max_blur_alpha)/int(args.range)) *i if ind>254 else 0)
 #   new_alpha_channel = alpha_channel.put_alpha(lambda ind: 128 - (128 / (args.range)) * i if ind > 0 else 0)
   # orig_alpha = alpha_channel.point(lambda ind: 255)
    background.putalpha(new_alpha_channel)
   # background.show()
    foreground = Image.alpha_composite(background, foreground)

foreground.save(args.output)
