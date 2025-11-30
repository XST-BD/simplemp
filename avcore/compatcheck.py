from random import sample
import audiocompat
import imagecompat
import subtcompat
import vdocompat

def checkMediaCompatibility(ext, codec, bitrate, samplerate, sample_fmt) -> bool:
    match ext:

        # AUDIO

        # ---- AAC family ----
        case ".aac":
            return audiocompat.isAACcompatible(ext, codec, bitrate, samplerate)

        case ".m4a":
            return audiocompat.isAACcompatible(ext, codec, bitrate, samplerate)

        case ".mp4":
            return audiocompat.isAACcompatible(ext, codec, bitrate, samplerate)

        case ".3gp":
            return audiocompat.isAACcompatible(ext, codec, bitrate, samplerate)

        case ".adts":
            return audiocompat.isAACcompatible(ext, codec, bitrate, samplerate)

        # ---- MP3 ----
        case ".mp3":
            return audiocompat.isMP3Compatible(codec, bitrate, samplerate)

        # ---- WAV / PCM ----
        case ".wav":
            return audiocompat.isWAVCompatible(codec, samplerate)

        case ".aiff" | ".aif":
            return audiocompat.isAIFFCompatible()

        # ---- Ogg / Vorbis / Opus ----
        case ".ogg":
            return audiocompat.isOggCompatible()

        case ".opus":
            return audiocompat.isOpusCompatible()

        # ---- FLAC ----
        case ".flac":
            return audiocompat.isFLACCompatible()

        # ---- WMA ----
        case ".wma":
            return audiocompat.isWMACompatible()

        # ---- AMR (narrowband & wideband) ----
        case ".amr":
            return audiocompat.isAMRCompatible()

        case ".awb":
            return audiocompat.isAWBCompatible()

        # ---- ALAC ----
        case ".alac":
            return audiocompat.isALACCompatible(codec, samplerate, sample_fmt)


        # IMAGE
        case ".jpg" | ".jpeg":
            return imagecompat.isJPEGcompatible()

        case ".png":
            return imagecompat.isPNGcompatible()

        case ".bmp":
            return imagecompat.isBMPcompatible()

        case ".gif":
            return imagecompat.isGIFcompatible()

        case ".tiff" | ".tif":
            return imagecompat.isTIFFcompatible()

        case ".webp":
            return imagecompat.isWEBPcompatible()

        case ".avif":
            return imagecompat.isAVIFcompatible()

        case ".heic" | ".heif":
            return imagecompat.isHEIFcompatible()

        case ".ppm" | ".pgm" | ".pbm" | ".pnm":
            return imagecompat.isPNMcompatible()

        case ".svg":
            return imagecompat.isSVGcompatible()

        case ".ico":
            return imagecompat.isICOcompatible()

        # SUBTITLE
        case ".srt":
            return subtcompat.isSRTcompatible()

        case ".ass" | ".ssa":
            return subtcompat.isASScompatible()

        case ".vtt":
            return subtcompat.isVTTcompatible()

        case ".sub":
            return subtcompat.isSUBcompatible()

        case ".idx":
            return subtcompat.isIDXcompatible()

        case ".ttml" | ".dfxp":
            return subtcompat.isTTMLcompatible()

        case ".smi" | ".sami":
            return subtcompat.isSMIcompatible()

        case ".lrc":
            return subtcompat.isLRCcompatible()

        case ".stl":
            return subtcompat.isSTLcompatible()

        case ".sbv":
            return subtcompat.isSBVcompatible()

        case ".json":
            return subtcompat.isJSONSubtitleCompatible()

        # VIDEO
        case ".mp4":
            return vdocompat.isMP4compatible()

        case ".mkv":
            return vdocompat.isMKVcompatible()

        case ".mov":
            return vdocompat.isMOVcompatible()

        case ".avi":
            return vdocompat.isAVIcompatible()

        case ".wmv":
            return vdocompat.isWMVcompatible()

        case ".flv":
            return vdocompat.isFLVcompatible()

        case ".webm":
            return vdocompat.isWEBMcompatible()

        case ".mpeg" | ".mpg":
            return vdocompat.isMPEGcompatible()

        case ".ts" | ".m2ts":
            return vdocompat.isTScompatible()

        case ".3gp":
            return vdocompat.is3GPcompatible()

        case ".ogv":
            return vdocompat.isOGVcompatible()

        case ".mpv":
            return vdocompat.isMPVcompatible()

        case ".f4v":
            return vdocompat.isF4Vcompatible()

        case ".rm" | ".rmvb":
            return vdocompat.isRMcompatible()

        case ".asf":
            return vdocompat.isASFcompatible()

        case ".divx":
            return vdocompat.isDIVXcompatible()


        # ---- Default fallback ----
        case _:
            print(f"SimpleMP: Unsupported or unknown output extension '{ext}'")
            return False