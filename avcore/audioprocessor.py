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
    codec: str = "",                # codec to use for conversion
    overwrite: bool = False,        # whether to overwrite existing files
    debug: bool = False,            # print debug info
    threads: int = 0,               # ffmpeg threads, 0 = auto

    # --------------------
    # Audio only
    samplerate: int = 44100,        # sample rate in Hz (defasult : 44.1khz)
    sample_fmt: str = "",           # e.g., pcm_s16le, pcm_f32le
    channels: int = 2,              # number of audio channels  (default : stereo)
    volume: float = 1.0,            # volume adjustment (linear)
    audio_filter: str = "",         # e.g., "highpass=f=300"
    normalize: bool = False,        # normalize audio
    start_time: float = 0.0,        # start time (seek)
    duration: float = 0.0,          # duration to process
    bitrate: int = 192000,          # audio bitrate for compressed formats (defasult : 192kbps)

    # --------------------
    # Video only
    width: int = 800,               # output width
    height: int = 600,              # output height
    frame_rate: float = 30.00,      # fps (default : 30fps)                        
    pixel_format: str = "",         # yuv420p, rgb24, etc.
    video_filter: str = "",         # e.g., "crop=640:360"
    rotate: int = 0,                # rotation in degrees
    bitrate_video: int = 192000,    # video bitrate
    gop_size: int = 0,              # keyframe interval
    preset: str = "",               # encoder preset (fast, slow, etc.)
    crf: int = 0,                   # constant rate factor for quality-based encoding

    # --------------------
    # Audio & Video
    map_streams: str = "",          # e.g., "0:a,0:v" for specific streams
    mute: bool = False,             # remove audio track
    loop: int = 0,                  # loop input N times
    start_time_global: float = 0.0, # global start time for trimming
    duration_global: float = 0.0,   # global duration for trimming

    # --------------------
    # Image only
    format_out: str = "",           # e.g., png, jpg, bmp
    compression_level: int = 6,     # for PNG, WebP, etc.
    quality: int = 85,              # JPEG / WebP quality 0-100
    resize: Optional[Tuple[int,int]] = None,         
                                    # (width, height)
    rotate_image: int = 0,          # image rotation
    flip: str = "",                 # horizontal / vertical / both
    color_space: str = "",          # e.g., rgb24, gray
    dithering: bool = False,        # for palette reduction

    # --------------------
    # Subtitle only
    subtitle_codec: str = "",           # e.g., srt, ass, mov_text
    subtitle_encoding: str = "utf-8",   # character encoding
    subtitle_filter: str = "",          # e.g., "scale=1.5:1.5"
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
        print("SimpleMP: Output file doesn't exist")
        return

    input = av.open(str(inputfilename))
    
    # ==== debug
    debuglog.debuglog(input, debug)

    # ==== check file extenstion and codec compatibility with settings
    ext = os.path.splitext(outputfilename)[1].lower()
    if not compatcheck.checkMediaCompatibility(ext, codec, samplerate, sample_fmt, bitrate):
        return
    
    simplempcore.smpcore(inputfilename, outputfilename, codec, bitrate, samplerate, sample_fmt)



smpMediaProcessor("../dump/testaudio.flac", 
                  "../dump/some.mp3",
                  codec="mp3", 
                  bitrate=68000, 
                  samplerate=48000, 
                  sample_fmt="",
                  debug=False)