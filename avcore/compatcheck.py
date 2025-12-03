import code
from random import sample

# don't remove . from keys. It's for explicitly describing extension name
codec_dict = {

    # Audio

    ".3gp"  : ["aac"],
    ".aac"  : ["aac"],
    ".adts" : ["aac"],
    ".aif"  : ["pcm_s8", "pcm_s16le", "pcm_s32le", "pcm_s16be", "pcm_s24be", "pcm_s32be"],

    # aifc also supports alac coded but needs AIFF-C muxer. Which is unavailable in pyav
    ".aifc" : ["pcm_s8", "pcm_s16le", "pcm_s16be", "pcm_s24be", "pcm_s32be"],

    ".aiff" : ["pcm_s8", "pcm_s16le", "pcm_s16be", "pcm_s24be", "pcm_s32be"],

    # these 2 needs separate libs installed
    # ".amr"  : ["amr_nb", "amr_wb"],
    # ".awb"  : ["amr_wb"],

    # caf file don't work well outside mac
    # ".caf"  : ["alac"], 

    ".flac" : ["flac"],
    ".m4a"  : ["aac", "alac"],
    ".mp3"  : ["mp3"],
    # ".mp4"  : ["aac", "aac (fdk)"],
    ".oga"  : ["vorbis", "opus", "flac", "speex"],
    ".ogg"  : ["vorbis", "opus", "flac", "speex"],
    ".opus" : ["opus"],
    ".wav"  : ["pcm_alaw", "pcm_mulaw", 
               "pcm_s8", 
               "pcm_s16le", "pcm_s24le", "pcm_s32le",
               "pcm_s16be", "pcm_s24be", "pcm_s32be"], 

    # wma format also supports wmapro and wmalossless codec. But not available by default for being proprietary
    ".wma"  : ["wmav1", "wmav2"],

    # Images

    ".bmp"  : ["bmp"],
    ".gif"  : ["gif"],
    ".ico"  : ["ico"],
    ".jpg"  : ["mjpeg"],    # FFmpeg encoder name for JPEG
    ".jpeg" : ["mjpeg"],
    ".png"  : ["png"],
    ".pbm"  : ["pbm"],
    ".pgm"  : ["pgm"],
    ".pnm"  : ["pnm"],
    ".ppm"  : ["ppm"],
    ".svg"  : [],           # FFmpeg can read, not encode
    ".tif"  : ["tiff"],
    ".tiff" : ["tiff"],
    ".webp" : ["webp"],


    # Subtitles

    ".ass"  : ["ass"],
    ".dfxp" : ["ttml"],
    ".idx"  : ["vobsub"],     # VobSub (DVD bitmap) .idx+.sub pair
    ".scc"  : ["scc"],        # Scenarist Closed Caption
    ".srt"  : ["subrip"],
    ".ssa"  : ["ssa"],
    ".stl"  : ["ebu_stl"],    # EBU STL broadcast subs
    ".sub"  : ["microdvd"],   # text-based MicroDVD subtitles
    ".sup"  : ["pgssub"],     # Blu-ray PGS bitmap subtitles
    ".ttml" : ["ttml"],
    ".vtt"  : ["webvtt"],

    # Video

    # ".3gp"  : ["h264", "mpeg4"],
    ".asf"  : ["wmv1", "wmv2"],
    ".avi"  : ["mpeg4", "h264", "hevc"],
    ".flv"  : ["flv", "h264"],
    ".m4v"  : ["h264", "mpeg4"],
    ".mov"  : ["h264", "hevc", "mpeg4"],
    ".mp4"  : ["h264", "hevc", "mpeg4", "libx264", "libx265", "libopenh264", "av1"],
    ".mpg"  : ["mpeg1video", "mpeg2video"],
    ".mpeg" : ["mpeg1video", "mpeg2video"],
    ".mkv"  : ["h264", "hevc", "mpeg4", "vp8", "vp9", "av1"],
    ".ts"   : ["h264", "hevc", "mpeg2video"],
    ".webm" : ["vp8", "vp9", "av1"],    # only [opus, vorbis] audio codec supported | Extremely slow if wrong settings used
    ".wmv"  : ["wmv1"],
}

bitrate_range_dict = {

    # Compressed audio codecs
    "aac": [64000, 320000],
    "aac (fdk)": [64000, 320000],
    "amr_nb": [4750, 12200],       # AMR Narrowband
    "amr_wb": [6600, 23850],       # AMR Wideband
    "mp3": [64000, 320000],
    "opus": [500, 256000],          # 0.5 kbps → 256 kbps
    "vorbis": [16000, 500000],     # Ogg Vorbis
    "speex": [2000, 44100],        # Narrowband / wideband

    # wma supports some more bitrates but channel specific
    "wmav1": [32000, 32000], 
    "wmav2": [32000, 32000], 

    "wmapro": [12000, 384000], 
    "wmalossless": [12000, 384000], # technically lossless can vary

    # Lossless / PCM codecs → bitrate irrelevant
    "alac": None,
    "flac": None,
    "pcm_alaw": None,
    "pcm_mulaw": None,
    "s16": None,
    "s24": None,
    "s32": None,
    "flt": None,
    "dbl": None,
    "s16p": None,
    "s24p": None,
    "s32p": None,
    "fltp": None,
    "dblp": None,
    "u8": None
}

samplerate_range_dict = {

    # AAC
    "aac": [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000],
    "aac (fdk)": [32000, 48000],

    # MP3
    "mp3": [32000, 48000],

    # Opus
    "opus": [8000, 48000],

    # Ogg codecs
    "vorbis": [32000, 48000],
    "speex": [8000, 32000],

    # AMR
    "amr_nb": [8000, 8000],      # fixed 8kHz
    "amr_wb": [16000, 16000],    # fixed 16kHz

    # WMA
    "wmav1": [8000, 11025, 16000, 22050, 32000, 44100],
    "wmav2": [8000, 11025, 16000, 22050, 32000, 44100, 48000],
    # "wmapro": [8000, 48000],
    # "wmalossless": [8000, 48000],

    # Lossless / PCM
    "alac": [8000, 192000],
    "flac": [8000, 192000],
    "pcm_alaw": [8000, 192000],
    "pcm_mulaw": [8000, 192000],
    "pcm_s8": [8000, 192000],
    "pcm_s16le": [8000, 192000],
    "pcm_s24le": [8000, 192000],
    "pcm_s32le": [8000, 192000],
    "pcm_s16be": [8000, 192000],
    "pcm_s24be": [8000, 192000],
    "pcm_s32be": [8000, 192000],
    "pcm_f32": [8000, 192000],
    "pcm_f64": [8000, 192000],
}

audio_sample_fmt_dict = {

    # Lossless PCM
    "u8": ["u8"],
    "pcm_s8": ["pcm_s8"],
    "pcm_s16le": ["s16"],
    "s16p": ["s16p"],
    "s24": ["s24"],
    "s24p": ["s24p"],
    "s32": ["s32"],
    "s32p": ["s32p"],
    "flt": ["flt"],
    "fltp": ["fltp"],
    "dbl": ["dbl"],
    "dblp": ["dblp"],
    "pcm_alaw": ["pcm_alaw"],
    "pcm_mulaw": ["pcm_mulaw"],

    # Lossless compressed
    "flac": ["u8", "s16", "s16p", "s32", "s32p", "flt", "fltp", "dbl", "dblp"],
    "alac": ["u8", "s16", "s16p", "s32", "s32p", "flt", "fltp"],

    # Compressed formats (bit depth is internal / fixed)
    "aac": None,
    "aac (fdk)": None,
    "mp3": None,
    "opus": None,
    "vorbis": None,
    "speex": None,
    "amr_nb": None,
    "amr_wb": None,
    "wmav1": None,
    "wmav2": None,
    "wmapro": None,
    "wmalossless": None
}

video_sample_fmt_dict = {
    "av1": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    "h264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],
    "libx264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],
    "libopenh264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],

    "h265": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],
    "hevc": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],
    "libx265": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    # VP8 / VP9
    "vp8": ["yuv420p", "yuv422p", "yuv444p"],
    "vp9": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    "flv": ["yuv420p"],
    "mpeg1video": ["yuv420p"],
    "mpeg2video": ["yuv420p"],
    "mpeg4": ["yuv420p"],
    "wmv1" : ["yuv420p"],
    "wmv2" : ["yuv420p"],

    # Lossless / uncompressed video
    "rawvideo": ["rgb24", "bgr24", "rgba", "bgra", "yuv420p", "yuv422p", "yuv444p", "gray", "yuv420p10le", "yuv422p10le"],

    # Proprietary (Unavailable to use at API)
    "prores": ["yuv422p10le", "yuv444p10le"],
    "dnxhd": ["yuv422p", "yuv422p10le"],

    # Placeholder for other codecs, default to common 8-bit YUV
    "default": ["yuv420p", "yuv422p", "yuv444p", "rgb24"]
}

frame_rate_dict = {
    "mpeg4" : [24, 120],
    "wmv1" : [24, 30],
    "wmv2" : [24, 30],
}

media_type_ext_dict = {
    "audio": [
        ".3gp", ".aac", ".adts", ".aif", ".aifc", ".aiff", ".alac", ".amr", ".awb", 
        ".flac", 
        ".m4a", ".mp3", "mp4", 
        ".oga", ".ogg", ".opus", 
        ".wav", ".wma" 
    ],
    "image": [
        ".bmp", 
        ".gif", 
        ".ico", 
        ".jpg", ".jpeg", 
        ".png", ".pbm", ".pgm", ".pnm", ".ppm", 
        ".svg", 
        ".tif", ".tiff", 
        ".webp",
    ],
    "subtitle": [
        ".ass",
        ".dfxp",
        ".idx",
        ".scc", ".srt", ".ssa", ".stl", ".sub", ".sup",
        ".ttml",
        ".vtt",
    ],
    "video": [
        # ".3gp",
        ".asf", ".avi"
        ".flv",
        ".m4v" , ".mkv", ".mov", ".mp4", ".mpg", "mpeg",
        ".ts",
        ".webm", ".wmv",
    ],
}


def checkCodecCompatibility(ext, codecname) -> bool:

    # 1: Check extension
    if ext not in codec_dict: 
        print(f"SimpleMP: Unknownn media file extension: {codecname}")
        return False

    # 2: Check codec existence
    all_codecs = {c for codecs in codec_dict.values() for c in codecs}
    if codecname not in all_codecs:
        print(f"SimpleMP: Unknown codec found: {codecname}")
        return False

    # 3: Check codec compatibility with file extension
    if codecname not in codec_dict[ext]: 
        print(f"SimpleMP: Unsupported codec for converstion to {ext}\n"
              f"Supported codecs are:\n"
              f"{codec_dict[ext]}")
        return False

    return True

def checkBitrateCompatibility(codecname, bitrate : int) -> bool:

    # irrelevant for lossless codecs
    if bitrate_range_dict.get(codecname) is None: 
        return True

    if bitrate < bitrate_range_dict[codecname][0] or bitrate > bitrate_range_dict[codecname][1]: 
        print(f"SimpleMP: Bitrate outside safe range for codec: {codecname}\n"
              f"Safe range: [{bitrate_range_dict[codecname][0]},{bitrate_range_dict[codecname][1]}]")
        return False

    return True

def checkSamplerateCompatibility(codecname, samplerate) -> bool:

    # fixed sample rate for amr_nb and amr_wb
    if codecname == "amr_nb": 
        if samplerate != 8000: 
            print(f"SimpleMP: Only 8khz sample rate allowed for codec: {codecname}")
            return False

    if codecname == "amr_wb": 
        if samplerate != 16000: 
            print(f"SimpleMP: Only 16khz sample rate allowed for codec: {codecname}")
            return False
        
    if codecname == "aac" or codecname == "wmav1" or codecname == "wmav2" or codecname == "mp3":
        if samplerate not in samplerate_range_dict[codecname]: 
            print(f"SimpleMP: {codecname} only supports following sample rates:\n"
                  f"{samplerate_range_dict[codecname]}")
            return False
        return True


    if samplerate < samplerate_range_dict[codecname][0] or samplerate > samplerate_range_dict[codecname][1]: 
        print(f"SimpleMP: Sample rate outside safe range for codec: {codecname}\n"
              f"Safe range: [{samplerate_range_dict[codecname][0]},{samplerate_range_dict[codecname][1]}]")
        return False

    return True

def checkAudioSamplefmtCompatibility(codecname : str, sample_fmt : str) -> bool:

    # if not set, default will be used
    if sample_fmt == "":
        return True

    # irrelevant for lossy codecs
    if audio_sample_fmt_dict.get(codecname) is None: 
        return True

    if sample_fmt not in audio_sample_fmt_dict[codecname]:
        print(f"SampleMP: Incompatible sample format: {sample_fmt} for codec: {codecname}\n"
              "Supported sample formats: \n"
              f"{audio_sample_fmt_dict[codecname]}") 
        return False
    
    return True 

def checkVideoSamplefmtCompatibility(codecname, pixel_fmt) -> bool:

    if pixel_fmt not in video_sample_fmt_dict[codecname]:
        print(f"SampleMP: Incompatible sample format for codec: {codecname}\n"
              "Supported sample formats: \n"
              f"{video_sample_fmt_dict[codecname]}") 
        return False
    
    return True 



def checkMediaCompatibility(ext, 
                            audio_codecname, video_codecname, 
                            samplerate, samplefmt : str, pixel_fmt : str,
                            bitrate : int, bitrate_video : int) -> bool: 

    mediatype = -1

    if ext in media_type_ext_dict["audio"]: mediatype = 0
    if ext in media_type_ext_dict["image"]: mediatype = 1
    if ext in media_type_ext_dict["subtitle"]: mediatype = 2
    if ext in media_type_ext_dict["video"]: mediatype = 3

    if not checkCodecCompatibility(ext, video_codecname): 
        return False
    
    match mediatype: 
        # Audio
        case 0:
            if not checkBitrateCompatibility(audio_codecname, bitrate): return False
            if not checkSamplerateCompatibility(audio_codecname, samplerate): return False
            if not checkAudioSamplefmtCompatibility(audio_codecname, samplefmt): return False
        # Video
        case 3: 
            if not checkBitrateCompatibility(video_codecname, bitrate): return False
            if not checkVideoSamplefmtCompatibility(video_codecname, pixel_fmt): return False

    return True


def checkAudioVideoCompat():
    pass