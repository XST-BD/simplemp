from random import sample

codec_dict = {

    # Audio

    ".3gp"  : ["aac", "aac (fdk)"],
    ".aac"  : ["aac", "aac (fdk)"],
    ".adts" : ["aac", "aac (fdk)"],
    ".aif"  : ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
    ".aifc" : ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
    ".aiff" : ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
    ".alac" : ["alac"],
    ".amr"  : ["amr_nb", "amr_wb"],
    ".awb"  : ["amr_wb"],
    ".flac" : ["flac"],
    ".m4a"  : ["aac", "aac (fdk)"],
    ".mp3"  : ["mp3"],
    ".mp4"  : ["aac", "aac (fdk)"],
    ".oga"  : ["vorbis", "opus", "flac", "speex"],
    ".ogg"  : ["vorbis", "opus", "flac", "speex"],
    ".opus" : ["opus"],
    ".wav"  : ["pcm_alaw", "pcm_mulaw", 
               "pcm_s16le", "pcm_s24le", "pcm_s32le", "pcm_f32le", "pcm_f64le", 
               "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be", 
               "pcm_u8"], 
    ".wma"  : ["wmav1", "wmav2", "wmapro", "wmalossless"],

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
    ".svg"  : [],   # FFmpeg can read, not encode
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

    ".3gp"  : ["h264", "mpeg4"],
    ".asf"  : ["wmv1", "wmv2", "wmv3"],
    ".avi"  : ["mpeg4", "h264", "hevc"],
    ".flv"  : ["flv", "h264"],
    ".m4v"  : ["h264", "mpeg4"],
    ".mov"  : ["h264", "hevc", "prores", "mpeg4"],
    ".mp4"  : ["h264", "hevc", "mpeg4", "libx264", "libx265", "libopenh264", "av1"],
    ".mpg"  : ["mpeg1video", "mpeg2video"],
    ".mpeg" : ["mpeg1video", "mpeg2video"],
    ".mkv"  : ["h264", "hevc", "mpeg4", "vp8", "vp9", "av1"],
    ".ts"   : ["h264", "hevc", "mpeg2video"],
    ".webm" : ["vp8", "vp9", "av1"],
    ".wmv"  : ["wmv1", "wmv2", "wmv3"],
}

bitrate_range_dict = {

    # Compressed audio codecs
    "aac": [64000, 320000],
    "aac (fdk)": [64000, 320000],
    "amr_nb": [4750, 12200],       # AMR Narrowband
    "amr_wb": [6600, 23850],       # AMR Wideband
    "mp3": [64000, 320000],
    "opus": [6000, 510000],        # 6 kbps → 510 kbps
    "vorbis": [16000, 500000],     # Ogg Vorbis
    "speex": [2000, 44100],        # Narrowband / wideband
    "wmav1": [12000, 384000], 
    "wmav2": [12000, 384000], 
    "wmapro": [12000, 384000], 
    "wmalossless": [12000, 384000], # technically lossless can vary

    # Lossless / PCM codecs → bitrate irrelevant
    "alac": None,
    "flac": None,
    "pcm_alaw": None,
    "pcm_mulaw": None,
    "pcm_s16le": None,
    "pcm_s24le": None,
    "pcm_s32le": None,
    "pcm_f32le": None,
    "pcm_f64le": None,
    "pcm_s16be": None,
    "pcm_s24be": None,
    "pcm_s32be": None,
    "pcm_f32be": None,
    "pcm_f64be": None,
    "pcm_u8": None
}

samplerate_range_dict = {

    # AAC
    "aac": [32000, 48000],
    "aac (fdk)": [32000, 48000],

    # MP3
    "mp3": [32000, 48000],

    # Opus
    "opus": [8000, 48000],

    # Ogg codecs
    "vorbis": [32000, 48000],
    "speex": [8000, 48000],

    # AMR
    "amr_nb": [8000, 8000],      # fixed 8kHz
    "amr_wb": [16000, 16000],    # fixed 16kHz

    # WMA
    "wmav1": [8000, 48000],
    "wmav2": [8000, 48000],
    "wmapro": [8000, 48000],
    "wmalossless": [8000, 48000],

    # Lossless / PCM
    "alac": [8000, 192000],
    "flac": [8000, 192000],
    "pcm_alaw": [8000, 192000],
    "pcm_mulaw": [8000, 192000],
    "pcm_s16le": [8000, 192000],
    "pcm_s24le": [8000, 192000],
    "pcm_s32le": [8000, 192000],
    "pcm_f32le": [8000, 192000],
    "pcm_f64le": [8000, 192000],
    "pcm_s16be": [8000, 192000],
    "pcm_s24be": [8000, 192000],
    "pcm_s32be": [8000, 192000],
    "pcm_f32be": [8000, 192000],
    "pcm_f64be": [8000, 192000],
    "pcm_u8": [8000, 192000]
}

audio_sample_fmt_dict = {

    # Lossless PCM
    "pcm_u8": ["pcm_u8"],
    "pcm_s8": ["pcm_s8"],
    "pcm_s16le": ["pcm_s16le"],
    "pcm_s16be": ["pcm_s16be"],
    "pcm_s24le": ["pcm_s24le"],
    "pcm_s24be": ["pcm_s24be"],
    "pcm_s32le": ["pcm_s32le"],
    "pcm_s32be": ["pcm_s32be"],
    "pcm_f32le": ["pcm_f32le"],
    "pcm_f32be": ["pcm_f32be"],
    "pcm_f64le": ["pcm_f64le"],
    "pcm_f64be": ["pcm_f64be"],
    "pcm_alaw": ["pcm_alaw"],
    "pcm_mulaw": ["pcm_mulaw"],

    # Lossless compressed
    "flac": ["pcm_s16le", "pcm_s24le", "pcm_s32le"],
    "alac": ["pcm_s16le", "pcm_s24le", "pcm_s32le", "pcm_f32le", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be"],

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
    # Common H.264 / H.265 codecs
    "h264": ["yuv420p", "yuv422p", "yuv444p", "nv12", "yuv420p10le", "yuv422p10le", "yuv444p10le"],
    "hevc": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    # VP8 / VP9
    "vp8": ["yuv420p", "yuv422p", "yuv444p"],
    "vp9": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    # AV1
    "av1": ["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"],

    # MPEG-2 / MPEG-4
    "mpeg2video": ["yuv420p", "yuv422p", "yuv444p"],
    "mpeg4": ["yuv420p", "yuv422p", "yuv444p"],

    # Lossless / uncompressed video
    "rawvideo": ["rgb24", "bgr24", "rgba", "bgra", "yuv420p", "yuv422p", "yuv444p", "gray", "yuv420p10le", "yuv422p10le"],

    # Others
    "prores": ["yuv422p", "yuv422p10le", "yuv444p10le"],
    "dnxhd": ["yuv422p", "yuv422p10le"],

    # Placeholder for other codecs, default to common 8-bit YUV
    "default": ["yuv420p", "yuv422p", "yuv444p", "rgb24"]
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
        ".3gp",
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
        print(f"SimpleMP: Unsupported codec for converstion to {ext}"
              f"Supported codecs are:"
              f"{codec_dict[ext]}")
        return False

    return True

def checkBitrateCompatibility(codecname, bitrate) -> bool:

    # irrelevant for lossless codecs
    if bitrate_range_dict.get(codecname) is None: 
        return True

    if bitrate < bitrate_range_dict[codecname][0] or bitrate > bitrate_range_dict[codecname][1]: 
        print(f"SimpleMP: Bitrate outside safe range for codec: {codecname}"
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


    if samplerate < samplerate_range_dict[codecname][0] or samplerate > samplerate_range_dict[codecname][1]: 
        print(f"SimpleMP: Sample rate outside safe range for codec: {codecname}"
              f"Safe range: [{samplerate_range_dict[codecname][0]},{samplerate_range_dict[codecname][1]}]")
        return False

    return True

def checkAudioSamplefmtCompatibility(codecname, sample_fmt) -> bool:

    # irrelevant for lossy codecs
    if audio_sample_fmt_dict.get(codecname) is None: 
        return True

    if sample_fmt not in audio_sample_fmt_dict[codecname]:
        print(f"SampleMP: Incompatible sample format for codec: {codecname}"
              "Supported sample formats: "
              f"{audio_sample_fmt_dict[codecname]}") 
        return False
    
    return True 

def checkVideoSamplefmtCompatibility(codecname, sample_fmt) -> bool:

    if sample_fmt not in video_sample_fmt_dict[codecname]:
        print(f"SampleMP: Incompatible sample format for codec: {codecname}"
              "Supported sample formats: "
              f"{video_sample_fmt_dict[codecname]}") 
        return False
    
    return True 

def checkMediaCompatibility(ext, codecname, samplerate, samplefmt, bitrate) -> bool: 


    mediatype = -1

    if ext in media_type_ext_dict["audio"]: mediatype = 0
    if ext in media_type_ext_dict["image"]: mediatype = 1
    if ext in media_type_ext_dict["subtitle"]: mediatype = 2
    if ext in media_type_ext_dict["video"]: mediatype = 3

    if not checkCodecCompatibility(ext, codecname): 
        return False
    
    match mediatype: 
        # Audio
        case 0:
            if not checkBitrateCompatibility(codecname, bitrate): return False
            if not checkSamplerateCompatibility(codecname, samplerate): return False
            if not checkAudioSamplefmtCompatibility(codecname, samplefmt): return False
        # Video
        case 3: 
            if not checkBitrateCompatibility(codecname, bitrate): return False
            if not checkVideoSamplefmtCompatibility(codecname, samplefmt): return False

    return True