# Audio tunings to add

# ----------- General ------------

# Option             | Meaning                                        |
# ------------------ | ---------------------------------------------- |
# `-acodec` / `-c:a` | Select audio codec                             |
# `-ar`              | Output sample rate                             |
# `-ac`              | Number of channels                             |
# `-aframes`         | Limit number of output audio frames            |
# `-sample_fmt`      | Audio sample format (s16, s32, flt, dbl, etc.) |
# `-an`              | Disable audio                                  |
# `-map a`           | Map audio streams                              |

# ----------- Encoder Tuning Options (codec-dependent) ------------

# Option               | Meaning                                     |
# -------------------- | ------------------------------------------- |
# `-b:a`               | Constant bit rate                           |
# `-q:a` / `-qscale:a` | VBR quality                                 |
# `-compression_level` | Tune encoder aggressiveness                 |
# `-cutoff`            | Lowpass cutoff for encoders that support it |
# `-frame_duration`    | AAC frame duration                          |
# `-profile:a`         | AAC/Opus codec profiles                     |

# ----------- Codec specific ------------

# Option                                      | Meaning                 |
# ------------------------------------------- | ----------------------- |
# `-profile:a aac_low`, `aac_he`, `aac_he_v2` | AAC profiles            |
# `-aac_coder`                                | Coder algorithm         |
# `-aac_ms`                                   | Enable mid/side coding  |
# `-aac_is`                                   | Enable intensity stereo |
# `-ne`                                       | Native encoder          |
# `-global_quality`                           | VBR mode                |

# ----------- Others ------------

# Option      | Meaning                                     |
# ----------- | ------------------------------------------- |
# `-af`       | Simple audio filters (not full filtergraph) |
# `-shortest` | Stop encoding when shortest stream ends     |
# `-async`    | Audio stretching (legacy)                   |


# ----------- Filtergraphs ------------

# (Resampling / Reformatting)
# ------------ | ----------------------------------------- |
# `aresample`  | High-quality resampling                   |
# `aformat`    | Force sample format, rate, channel layout |
# `channelmap` | Re-map channels                           |
# `pan`        | Custom channel mixing                     |
# `amerge`     | Merge audio streams                       |
# `amix`       | Mix multiple inputs                       |
# `asetrate`   | Change playback rate (without resampling) |


# (Volume / Dynamics)
# ------------- | ------------------------------- |
# `volume`      | Adjust gain                     |
# `dynaudnorm`  | Dynamic audio normalization     |
# `compand`     | Compressor/expander             |
# `alimiter`    | Brickwall limiter               |
# `agate`       | Noise gate                      |
# `acompressor` | Compressor                      |
# `aexpander`   | Expander                        |
# `aloudnorm`   | EBU R128 loudness normalization |

# (Equalization / Frequency)
# ------------------------- | ------------------------ |
# `equalizer`               | Parametric EQ            |
# `anequalizer`             | Graphic EQ               |
# `firequalizer`            | FFT-based EQ             |
# `highpass`                | HPF                      |
# `lowpass`                 | LPF                      |
# `bandpass` / `bandreject` | Band filters             |
# `afir`                    | Convolution filter       |
# `ladspa`                  | Plugin rack              |
# `bs2b`                    | Bauer stereo-to-binaural |


# (Pitch / Speed / Time)
# ------------ | ------------------------------------ |
# `atempo`     | Speed change w/out pitch shift       |
# `asetrate`   | Rate change with pitch               |
# `rubberband` | Pitch/time stretching (external lib) |
# `asyncts`    | Audio stretching                     |

# (Noise Reduction / Enhancement)
# ----------- | -------------------------- |
# `anlmdn`    | Non-local means denoiser   |
# `arnndn`    | RNNoise AI-based denoising |
# `afftdn`    | FFT-based noise reduction  |
# `aphaser`   | Phaser effect              |
# `asubboost` | Bass enhancement           |
# `adeclick`  | Remove clicks              |
# `adeclip`   | Restore clipped peaks      |

# (Spatial / Ambisonics)
# ------------ | ------------------ |
# `surround`   | Surround-to-stereo |
# `aspatial`   | Spatial audio      |
# `ambisonic*` | Ambisonics filters |

# (Effects / Synth / Modulation)
# ------------------------------- | ----------------- |
# `aecho`                         | Echo              |
# `adelay`                        | Delay per channel |
# `chorus`                        | Chorus            |
# `flanger`                       | Flanger           |
# `tremolo`                       | Tremolo           |
# `vibrato`                       | Vibrato           |
# `aphaser`                       | Phaser            |
# `sine`, `anoisesrc`, `aevalsrc` | Audio generators  |

# (Measurement / Analysis)
# ------------------------------- | --------------------------- |
# `astats`                        | Measure RMS, peak, crest    |
# `spectrumsynth`, `showspectrum` | Spectral analysis           |
# `aphasemeter`                   | Phase/mono/stereo coherence |
# `ametadata`                     | Inspect metadata            |


import code
from email.policy import default
import os
from random import sample

import av
import av.container
import av.datasets

import compatcheck

def smpMediaProcessor(
        inputfilename="",
        outputfilename="", 
        bitrate = None,
        codec="",
        samplerate = None,
        frames="",
        channels="",
        sample_fmt="",
        mute=False,
        mapstream=False,

        # debug
        debug=False,
):
    
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
    
    # check file extenstion compatibility with settings

    ext = os.path.splitext(outputfilename)[1].lower()

    # ========== DEBUG ==========   

    if debug: 
        print(
            "Information about input file:\n"
            f"Bitrate:      {input.bit_rate}\n"
            f"Container:    {input.format.name}\n"
            f"Duration:     {input.duration} ms\n"
        )

        if input.streams.audio:
            print("Audio stream: exists")

        if input.streams.video:
            print("Video stream: exists")

    # ========== DEBUG ===========  

    if not compatcheck.checkMediaCompatibility(ext, codec, bitrate, samplerate):
        return

    
smpMediaProcessor("/home/pancake/Projects/simplemp/dump/testaudio.wav", 
                  "some.mp3", debug=True)