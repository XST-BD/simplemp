import os
from typeguard import typechecked

import av
import av.logging

from .validator import check_media_compat
from .simplempcore import smpcore

@typechecked
def transcode(
    # --------------------
    # General (all media types)
    input_file: str = "",
    output_file: str = "",
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
    crf: int = 24,                  # constant rate factor for quality-based encoding
    preset: str = "fast",           # encoder preset
    profile : str = "high", 
    tune : str = "zerolatency",
):
    """
    Unified media processor function for audio, video, image, and subtitles.
    
    Parameters grouped by media type and relevance.
    """
    if debug: 
        av.logging.set_level(av.logging.DEBUG)

    # ===== check file existence

    if not input_file or not os.path.exists(input_file): 
        print("SimpleMP: Input file doesn't exist")
        return

    # Output file unneccessary for overwrite
    if not output_file and overwrite == False: 
        print("SimpleMP: Output file not specified")
        return
     
    if not os.path.exists(output_file):
        print("SimpleMP: Output file doesn't exist. Creating it...")
        with open(output_file, 'w') as f:
            pass

    input = av.open(str(input_file))

    if overwrite: 
        outputfilename = input_file

    mediatype : int = 0
    # ==== check file extenstion and codec compatibility with settings
    ext = os.path.splitext(output_file)[1].lower()
    if not check_media_compat(
        ext, 
        audio_codecname=codec_audio, video_codecname=codec_video, 
        samplerate=samplerate, samplefmt=sample_fmt, pixel_fmt=pixel_fmt,
        bitrate=bitrate, bitrate_video=bitrate_video,
        mediatype=mediatype,
    ):
        return
    
    smpcore(
                input_file, output_file, mute=mute,

                # Audio
                audio_codecname=codec_audio, bitrate=bitrate, sample_fmt=sample_fmt, sample_rate=samplerate, 

                # Video
                video_codecname=codec_video, bitrate_vdo=bitrate_video, frame_rate=frame_rate, pixel_fmt=pixel_fmt,
                width=width, height=height, preset=preset, tune=tune, profile=profile, crf=crf,   
                mediatype=mediatype,     
            )
