from random import sample


def isAACcompatible(ext, codecname, bitrate, samplerate) -> bool:

    if codecname not in ["aac", "aac (fdk)"]:
        print(f"SimpleMP: Unsupported codec for converstion to {ext} | Only aac and aac(fdk) codec is allowed")
        return False
    
    if not (64000 <= bitrate <= 320000):
        print("SimpleMP: Bitrate is outside safe range for {ext} | Safe range [64k, 320k]")
        return False
    
    match samplerate:
        case "low": samplerate = 32000
        case "medium": samplerate = 44100
        case "high": samplerate = 48000
        case _:
            if samplerate != 32000 and samplerate != 44100 and samplerate != 48000:
                print(f"SimpleMP: Unsafe sample rate for converstion to {ext}\n"  
                      "Safe sample rates are: 32khz, 44.1khz, 48khz")
                return False

    return True

def isAIFFCompatible() -> bool: 

    return True

def isALACCompatible(codecname, samplerate, sample_fmt) -> bool:

    if codecname != "alac":
        print("SimpleMP: Unsupported codec for converstion to .alac | Only alac codec is allowed")
        return False 
    
    match samplerate:
        case "low": samplerate = 32000
        case "medium": samplerate = 44100
        case "high": samplerate = 48000
        case _:
            if not (8000 <= samplerate <= 192000):
                print("SimpleMP: Unsafe sample rate range for .alac | Safe range [8k, 192k]")
                return False
            
    if sample_fmt not in [
        "pcm_s16le",  "pcm_s24le", "pcm_s32le",
        "pcm_s16be",  "pcm_s24be", "pcm_s32be", 
        "pcm_f32le", "pcm_f32be", 
        "pcm_f64le", "pcm_f64be"]:
        print("SimpleMP: Unsafe bit depth range for .alac | 16 bit to 32 bit is safer")
        return False   

    return True

def isAMRCompatible() -> bool:

    return True

def isFLACCompatible() -> bool: 

    return True

def isOggCompatible(codecname, samplerate) -> bool:

    if codecname not in ["vorbis", "opus", "flac", "speex"]:
        print("SimpleMP: Unsupported codec for converstion to .ogg"
              "Only following codecs are allowed:\n"
              "vorbis, opus, flac, speex")
        return False 
    
    match samplerate:
        case "low": samplerate = 32000
        case "medium": samplerate = 44100
        case "high": samplerate = 48000
        case _:
            if samplerate != 32000 and samplerate != 44100 and samplerate != 48000:
                print("SimpleMP: Unsafe sample rate for converstion to .ogg\n"  
                      "Safe sample rates are: 32khz, 44.1khz, 48khz")
                return False


    return True

def isOpusCompatible(codecname, samplerate, bitrate) -> bool: 

    # Codec check
    if codecname != "opus":
        print("SimpleMP: Unsupported codec for conversion to .opus | Only 'opus' codec is allowed")
        return False

    # Sample rate validation
    if not (8000 <= samplerate <= 48000):
        print("SimpleMP: Unsafe sample rate for .opus | Safe range [8kHz, 48kHz]")
        return False

    # Optional bitrate validation
    if bitrate is not None:
        if not (6000 <= bitrate <= 510000):
            print("SimpleMP: Unsafe bitrate for .opus | Safe range [6kbps, 510kbps]")
            return False

    return True

def isWMACompatible() -> bool:

    return True

def isAWBCompatible() -> bool: 

    return True

def isMP3Compatible(codecname, bitrate, samplerate) -> bool:

    if codecname != "mp3":
        print("SimpleMP: Unsupported codec for converstion to .mp3 | Only mp3 codec is allowed")
        return False 
    
    match samplerate:
        case "low": samplerate = 32000
        case "medium": samplerate = 44100
        case "high": samplerate = 48000
        case _:
            if samplerate != 32000 and samplerate != 44100 and samplerate != 48000:
                print("SimpleMP: Unsupported sample rate for converstion to .mp3\n"  
                      "Only allowed sample rates are: 32khz, 44.1khz, 48khz")
                return False
            
    match bitrate: 
        case "very low": bitrate = 64000
        case "low": bitrate = 96000
        case "medium": bitrate = 128000
        case "high": bitrate = 192000
        case "very high": bitrate = 256000
        case "extreme": bitrate = 320000
        case _:
            if not (64000 <= bitrate <= 320000):
                print("SimpleMP: Bitrate is outside safe range for .mp3 | Safe range [64k, 320k]")
                return False

    return True    

def isWAVCompatible(codecname, samplerate) -> bool:

    if codecname not in [
        "pcm_alaw",
        "pcm_mulaw",
        "pcm_s16le", 
        "pcm_s24le", 
        "pcm_s32le",
        "pcm_f32le", 
        "pcm_f64le",
        "pcm_s16be", 
        "pcm_s24be", 
        "pcm_s32be",
        "pcm_f32be", 
        "pcm_f64be",
        "pcm_u8"] :
        print("SimpleMP: Unsupported codec for converstion to .wav\n" 
              " Only following codecs are allowed:\n"
              "pcm_alaw, pcm_mulaw, pcm_s16le,  pcm_s24le, pcm_s32le, pcm_f32le, pcm_f64le, pcm_s16be, pcm_s24be, pcm_s32be, pcm_f32be, pcm_f64be, pcm_u8")
        return False 
    
    if not (8000 <= samplerate <= 192000):
        print("SimpleMP: Sample rate is outside safe range for .wav | Safe range [8k, 192k]")
        return False

    return True