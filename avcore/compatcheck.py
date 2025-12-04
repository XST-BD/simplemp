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

    ".flac" : ["flac"],
    ".m4a"  : ["aac", "alac"],
    ".mp3"  : ["mp3"],
    ".oga"  : ["vorbis", "opus", "flac", "speex"],
    ".ogg"  : ["vorbis", "opus", "flac", "speex"],
    ".opus" : ["opus"],
    ".wav"  : ["pcm_alaw", "pcm_mulaw", 
               "pcm_s8", 
               "pcm_s16le", "pcm_s24le", "pcm_s32le",
               "pcm_s16be", "pcm_s24be", "pcm_s32be"], 
    # wma format also supports wmapro and wmalossless codec. But not available by default for being proprietary
    ".wma"  : ["wmav1", "wmav2"],

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

    # Lossy
    "aac": [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000],
    "mp3": [32000, 48000],
    "opus": [8000, 48000],
    "vorbis": [32000, 48000],
    "speex": [8000, 32000],
    "wmav1": [8000, 11025, 16000, 22050, 32000, 44100],
    "wmav2": [8000, 11025, 16000, 22050, 32000, 44100, 48000],

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

codec_channels_dict = {

    # Lossy codecs

    "aac": [1, 2, 6, 8],
    "mp3": [1, 2],
    "opus": [1, 2, 6, 8],
    "vorbis": [1, 2, 6],
    "speex": [1],
    "wmav1": [1, 2],
    "wmav2": [1, 2, 6],

    # Lossless / PCM codecs

    "alac": [1, 2, 6, 8],
    "flac": [1, 2, 6, 8],
    "pcm_alaw": [1, 2],
    "pcm_mulaw": [1, 2],

    # PCM integer LE/BE: FFmpeg supports up to 8
    "pcm_s8": [1, 2, 6, 8],
    "pcm_s16le": [1, 2, 6, 8],
    "pcm_s24le": [1, 2, 6, 8],
    "pcm_s32le": [1, 2, 6, 8],
    "pcm_s16be": [1, 2, 6, 8],
    "pcm_s24be": [1, 2, 6, 8],
    "pcm_s32be": [1, 2, 6, 8],

    # PCM float: same
    "pcm_f32": [1, 2, 6, 8],
    "pcm_f64": [1, 2, 6, 8],
}


audio_sample_fmt_dict = {

    # Uncompressed PCM
    "pcm_u8": ["u8"],
    "pcm_s8": ["s8"],
    "pcm_s16le": ["s16", "s16p"],
    "pcm_s16be": ["s16", "s16p"],

    # FFmpeg does not expose native s24 sample_fmt
    "pcm_s24le": ["s32", "s32p"],  
    "pcm_s24be": ["s32", "s32p"],
    "pcm_s32le": ["s32", "s32p"],
    "pcm_s32be": ["s32", "s32p"],
    "pcm_f32le": ["flt", "fltp"],
    "pcm_f32be": ["flt", "fltp"],
    "pcm_f64le": ["dbl", "dblp"],
    "pcm_f64be": ["dbl", "dblp"],
    "pcm_alaw": ["s16", "s16p"],
    "pcm_mulaw": ["s16", "s16p"],

    # Lossless compressed codecs
    "flac": ["s16", "s16p", "s32", "s32p", "flt", "fltp"],
    "alac": ["s16", "s16p", "s32", "s32p", "flt", "fltp"],


    # Lossy codecs — sample_fmt fixed, reject others
    # They do *not* accept arbitrary formats
    "aac": ["fltp"],
    "mp3": ["s16p", "s16", "flt", "fltp"],
    "opus": ["fltp"],
    "vorbis": ["fltp"],
    "speex": ["flt", "fltp"],
    "wmav1": ["s16"],
    "wmav2": ["s16"],
}


video_sample_fmt_dict = {
    "av1": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    "h264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],
    "libx264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],
    "libopenh264": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le", "nv12"],

    "h265": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],
    "hevc": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],
    "libx265": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

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

preset_list = {"veryslow", "slower", "slow", "medium", "fast", "faster", "veryfast", "superfast", "ultrafast"}
profile_list = {"baseline", "high", "main"}
tune_list = {"animation", "fastdecode", "film", "grain", "stillimage", "zerolatency"}

# list of video codecs that support crf, preset, profile and tune
codec_cppt_support_list = {"h264", "libx264", "libopenh264", "h265", "libx265", "hevc"}
# list of video codecs that support crf, preset and profile but not tune
codec_cpp_support_list = {"av1", "vp9"}


media_type_ext_dict = {
    "audio": [
        ".3gp", ".aac", ".adts", ".aif", ".aifc", ".aiff", ".alac", ".amr", ".awb", 
        ".flac", 
        ".m4a", ".mp3", "mp4", 
        ".oga", ".ogg", ".opus", 
        ".wav", ".wma" 
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
    if ext in media_type_ext_dict["subtitle"]: mediatype = 1
    if ext in media_type_ext_dict["video"]: mediatype = 2

    if not checkCodecCompatibility(ext, video_codecname): 
        return False
    
    match mediatype: 
        # Audio
        case 0:
            if not checkBitrateCompatibility(audio_codecname, bitrate): return False
            if not checkSamplerateCompatibility(audio_codecname, samplerate): return False
            if not checkAudioSamplefmtCompatibility(audio_codecname, samplefmt): return False
    
        # Video
        case 2: 
            if not checkBitrateCompatibility(video_codecname, bitrate): return False
            if not checkVideoSamplefmtCompatibility(video_codecname, pixel_fmt): return False

    return True


# check video codec's compatibility with crf, preset, profile and tune
def checkCPPTcompat(codecname : str, crf : int, profile : str, preset : str, tune : str) ->  bool:

    if codecname not in codec_cppt_support_list and codecname not in codec_cpp_support_list: 
        print(f"SimpleMP: Codec: {codecname} doesn't support crf, preset, profile and tune")
        return False
    
    if crf not in range(0, 51):
        print(f"SimpleMP: crf outside practical range [0, 51]")
        return False 
    
    if profile not in profile_list: 
        print(f"SimpleMP: Profile: {profile} is unavailable to use or unavailable or non-exitentn\n"
              f"Available: {profile_list}")
        return False
    
    if preset not in preset_list: 
        print(f"SimpleMP: Preset: {preset} is unavailable to use or unavailable or non-exitent\n"
              f"Available: {preset_list}")
        return False

    if tune not in tune_list: 
        print(f"SimpleMP: Profile: {profile} is unavailable to use or unavailable or non-exitent\n"
              f"Available : {tune_list}")
        return False
    
    if tune in tune_list and codecname in codec_cpp_support_list:
        print(f"SimpleMP: Codec: {codecname} doesn't support tune")
        return False

    return True


def checkAudioVideoCompat():
    pass