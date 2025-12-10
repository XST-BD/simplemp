import os 
import sys

import pytest 

# external_dir = os.path.abspath('/home/pancake/Projects/simplemp/simplemp') 
# sys.path.append(external_dir) 

from simplemp.simplemp import transcode

transcode(
    inputfilename="../dump/testv0.0.3/next.mp3", outputfilename="../dump/testv0.0.3/next1.aifc",
    codec_audio="pcm_s32be", samplerate=48000, bitrate=128000, sample_fmt="s32p",
    # codec_video="vp9", bitrate_video=4000000, pixel_fmt="yuv422p", frame_rate=60, crf=24, preset="slow", profile="baseline", tune="zerolatency",
    # width=1280, height=720,
    mute=False, debug=True, overwrite=False
)