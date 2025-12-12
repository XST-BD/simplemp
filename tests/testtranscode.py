import os 
import sys

import pytest 

# external_dir = os.path.abspath('/home/pancake/Projects/simplemp/simplemp') 
# sys.path.append(external_dir) 

from simplemp.simplemp import transcode

transcode(
    input_file="../dump/testv0.0.3/next.mp4", output_file="../dump/testv0.0.3/next1.asf",
    codec_audio="aac", samplerate=48000, bitrate=128000, sample_fmt="s32p",
    codec_video="vp9", bitrate_video=4000000, pixel_fmt="yuv422p", frame_rate=60, crf=24, preset="slow", profile="baseline", tune="zerolatency",
    width=1280, height=720,
    mute=False, debug=True, overwrite=False
)