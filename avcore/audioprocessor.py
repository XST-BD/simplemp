import code
from email.policy import default
import os
from random import sample

from typing import Optional, Tuple

import av
import av.container
import av.datasets

import compatcheck
import debuglog

import simplempcore

def smpMediaProcessor(
    # --------------------
    # General (all media types)
    inputfilename: str = "",
    outputfilename: str = "",
    overwrite: bool = False,        # whether to overwrite existing files
    debug: bool = False,            # print debug info
    threads: int = 0,               # ffmpeg threads, 0 = auto
    mute: bool = False,             # remove audio track
    loop: int = 0,                  # loop input N times

    # --------------------
    # Audio only
    codec_audio: str = "",          # audio codec to use for conversion
    samplerate: int = 44100,        # sample rate in Hz (defasult : 44.1khz)
    sample_fmt: str = "",           # e.g., pcm_s16le, pcm_f32le
    bitrate: int = 192000,          # audio bitrate for compressed formats (defasult : 192kbps)

    # --------------------
    # Video only
    codec_video: str = "",          # video codec to use for conversion
    pixel_fmt: str = "",            # yuv420p, rgb24, etc.
    bitrate_video: int = 192000,    # video bitrate
    width: int = 800,               # output width
    height: int = 600,              # output height
    frame_rate: int = 30,           # fps (default : 30fps)                        
    crf: int = 0,                   # constant rate factor for quality-based encoding
    preset: str = "",               # encoder preset (fast, slow, etc.)
    profile : str = "", 
    tune : str = "",

    # --------------------
    # Subtitle only
    codec_subtitle: str = "",           # e.g., srt, ass, mov_text
    subtitle_encoding: str = "utf-8",   # character encoding
    embed_subtitles: bool = False,      # burn-in subtitles
    extract_subtitles: bool = False,    # extract subtitle stream only
):
    """
    Unified media processor function for audio, video, image, and subtitles.
    
    Parameters grouped by media type and relevance.
    """
    
    # ===== check file existence

    if not inputfilename or not os.path.exists(inputfilename): 
        print("SimpleMP: Input file doesn't exist")
        return

    if not outputfilename: 
        print("SimpleMP: Output file not specified")
        return
     
    if not os.path.exists(outputfilename):
        print("SimpleMP: Output file doesn't exist. Creating it...")
        with open(outputfilename, 'w') as f:
            pass

    input = av.open(str(inputfilename))
    
    # ==== debug
    debuglog.debuglog(input, debug)

    # ==== check file extenstion and codec compatibility with settings
    ext = os.path.splitext(outputfilename)[1].lower()
    if not compatcheck.checkMediaCompatibility(
        ext, 
        codec_audio, codec_video, 
        samplerate, sample_fmt, pixel_fmt,
        bitrate, bitrate_video
    ):
        return
    
    simplempcore.smpcore(
                inputfilename, outputfilename,

                # Audio
                audio_codecname=codec_audio, bitrate=bitrate, sample_fmt=sample_fmt, sample_rate=samplerate, 

                # Video
                video_codecname=codec_video, bitrate_vdo=bitrate_video, frame_rate=frame_rate, pixel_fmt=pixel_fmt,
                width=width, height=height, preset=preset, tune=tune, profile=profile, crf=crf,         
            )


smpMediaProcessor(
            inputfilename="../dump/a2a/testaudio.aac", 
            outputfilename="../dump/a2a/audio9.wav",

            # Audio
            codec_audio="pcm_s32le", bitrate=2000, sample_fmt="s32p", samplerate=8000,

            # Video
            # codec_video="h264", bitrate_video=4000000, pixel_fmt="yuv420p", frame_rate=24, width=1280, height=720,
            # crf=24, tune="zerolatency", profile="high", preset="fast",
            
            # General
            threads=4, mute=False, loop=1, debug=False,
        )