def isAACcompatible() -> bool:

    return True

def isAIFFCompatible() -> bool: 

    return True

def isALACCompatible() -> bool:

    return True

def isAMRCompatible() -> bool:

    return True

def isFLACCompatible() -> bool: 

    return True

def isOggCompatible() -> bool:

    return True

def isOpusCompatible() -> bool: 

    return True

def isWMACompatible() -> bool:

    return True

def isAWBCompatible() -> bool: 

    return True

def isMP3Compatible(codecname, bitrate, samplerate) -> bool:

    if codecname != "mp3":
        print("SimpleMP: Unsupported codec for converstion to mp3 | Only mp3 codec is allowed")
        return False 
    
    match samplerate:
        case "low": samplerate = 32000
        case "medium": samplerate = 44100
        case "high": samplerate = 48000
        case _:
            if samplerate != 32000 and samplerate != 44100 and samplerate != 48000:
                print("SimpleMP: Unsupported sample rate for converstion to mp3\n"  
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
            if bitrate not in range(64000, 320000):
                print("SimpleMP: Bitrate is outside safe range | Safe range [64k, 320k]")
                return False

    return True    

def isWAVCompatible() -> bool:

    return True