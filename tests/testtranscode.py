import os 
import sys

external_dir = os.path.abspath('/home/pancake/Projects/simplemp/avcore/simplemp.py') 
sys.path.append(external_dir) 

from avcore import simplemp

simplemp.transcode(
    inputfilename="../dump/v2v/notafraid.mp4", outputfilename="../dump/v2v/notafraid.m4v",
    codec_audio="aac", codec_video="h264", 
    samplerate=48000, bitrate=128000, sample_fmt="fltp",
    bitrate_video=4000000, pixel_fmt="nv12", frame_rate=60, crf=24, preset="slow", profile="high", tune="zerolatency",
    width=1280, height=720,
    mute=False, debug=True, overwrite=False
)