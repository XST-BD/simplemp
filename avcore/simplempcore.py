from fractions import Fraction
from numbers import Rational
from random import sample
from struct import pack
import av
import av.codec
import av.datasets
from av.audio.stream import AudioStream
from av.audio.resampler import AudioResampler

from av.video.stream import VideoStream
from av.video.reformatter import VideoReformatter

from typing import cast

# input = av.open(av.datasets.curated("/home/pancake/Music/palpal.mp3"))
# output = av.open("/home/pancake/Projects/simplemp/dump/testaudio.wav", "w") 

# stream_map = {}

# for istream in input.streams:

#     if istream.type != "audio":
#         continue

#     ostream = output.add_stream_from_template(istream)
#     stream_map[istream.index] = ostream


# for packet in input.demux():
    
#     # skip flushing packets that demuxer generates
#     if packet.dts is None:
#         continue

#     packet.stream = stream_map[packet.stream.index]
#     output.mux(packet)

# input.close()
# output.close()


def smpcore(
        inputfilename : str,
        outputfilename : str,
        audio_codecname : str,
        video_codecname : str,
        bitrate : int, 
        sample_rate : int, 
        sample_fmt : str,
        frame_rate: int,
        channels : int,
        width : int, 
        height : int,
):
    
   