from PIL import Image
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='mastes images from <foreground_dir>, onto pngs from background dir ending at <frame_end> and palces the output at <output_dir>')
parser.add_argument('--foreground_dir', default='C:/Users/otman/OneDrive/Desktop/fastCD/fastComplementaryDynamicsCpp/results/reduction_vs_coarse/glob_tree_cage/cage_screenshots/',
                    help='input directory full of animation frames, these will all be the foreground')
parser.add_argument('--background_dir', default='C:/Users/otman/OneDrive/Desktop/fastCD/fastComplementaryDynamicsCpp/results/reduction_vs_coarse/glob_tree_cage/screenshots/',
                    help='input director full of animation frames, these will all be the background')
parser.add_argument('--frame_end', default=10,
                    help='which frame should we end at')
parser.add_argument('--output_dir', default='./output/', help='where to print output')
parser.add_argument('--zfill', default=4, help='frames are numbered from 0 to n. how many chars do these frames use for their numbering system')
args = parser.parse_args()
parser.print_help()


if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
#foreground.show()
for i in range(0, int(args.frame_end)):
    fore_path = args.foreground_dir + "/" + str(i).zfill(4) + ".png";
    back_path = args.background_dir + "/" + str(i).zfill(4) + ".png";
    out_path = args.output_dir + "/" + str(i).zfill(4) + ".png";

    print("Overlaying " + fore_path + " onto " + back_path + " and saving in " + out_path )
    foreground = Image.open( args.foreground_dir + "/" + str(i).zfill(4) + ".png")
    background = Image.open(args.background_dir + "/" + str(i).zfill(4) + ".png")

    alpha_channel = background.getchannel('A')

    background.paste(foreground, (0, 0), foreground)

    background.save(args.output_dir + "/" + str(i).zfill(4) + ".png")
