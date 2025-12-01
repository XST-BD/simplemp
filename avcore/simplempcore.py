from random import sample
import av
import av.codec
import av.datasets
from av.audio.stream import AudioStream
from av.audio.resampler import AudioResampler

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
        codecname : str,
        bitrate : int, 
        sample_rate : int, 
        sample_fmt : str
):
    
    input = av.open(inputfilename)
    output = av.open(outputfilename, mode="w")

    istreams = input.streams.audio[0] 

    ostream = cast(AudioStream, output.add_stream(codec_name=codecname, rate=sample_rate))
    ostream.bit_rate = bitrate
    ostream.layout = "mono"

    if sample_rate is not None and sample_rate != "": 
        ostream.sample_rate = sample_rate

   # Create a resampler to convert input to something the encoder accepts
    resampler = AudioResampler(
        format="fltp",         # safe default for AAC
        layout="mono",         # match ostream.layout
        rate=ostream.rate      # match ostream rate
    )

    for frames in input.decode(istreams):
        # TODO: Apply filters here
        frames = resampler.resample(frames) 

        for frame in frames:
            for packet in ostream.encode(frame):
                output.mux(packet)

    # flush encoder
    for packet in ostream.encode(None):
        output.mux(packet)

    input.close()
    output.close()

    