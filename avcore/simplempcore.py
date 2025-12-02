from random import sample
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
        sample_fmt : str
):
    
    input = av.open(inputfilename)
    output = av.open(outputfilename, mode="w")

    istreamsa = input.streams.audio[0] 
    istreamsv = input.streams.video[0]

    ostreama = cast(AudioStream, output.add_stream(codec_name=audio_codecname, rate=sample_rate))
    ostreamv = cast(VideoStream, output.add_stream(codec_name=video_codecname, rate=sample_rate))

    # Create a resampler to convert input audio to something the encoder accepts
    ostreama.bit_rate = bitrate
    resampler = AudioResampler(
        format="fltp",         # safe default for AAC
        layout="mono",         # match ostream.layout
        rate=sample_rate
    )

    # Create a reformater to convert input video to something the encoder accepts
    reformater = VideoReformatter()

    # Audio encoder
    for frames in input.decode(istreamsa):
        # TODO: Apply filters here
        frames = resampler.resample(frames) 

        for frame in frames:
            for packet in ostreama.encode(frame):
                output.mux(packet)

    # flush Audio encoder
    for packet in ostreama.encode(None):
        output.mux(packet) 


    # Video encoder 
    for frames in input.decode(istreamsv): 
        # TODO: Apply filters here
        
        rescaled_frames = frames.reformat(width=640, height=360, format='yuv420p')
        for packet in ostreamv.encode(rescaled_frames):
            output.mux(packet)

    # flush Video encoder
    for packet in ostreamv.encode(None): 
        output.mux(packet)

    input.close()
    output.close()

    