import av
import av.datasets

input = av.open(av.datasets.curated("/home/pancake/Music/palpal.mp3"))
output = av.open("/home/pancake/Projects/simplemp/dump/testaudio.wav", "w") 

stream_map = {}

for istream in input.streams:

    if istream.type != "audio":
        continue

    ostream = output.add_stream_from_template(istream)
    stream_map[istream.index] = ostream


for packet in input.demux():
    
    # skip flushing packets that demuxer generates
    if packet.dts is None:
        continue

    packet.stream = stream_map[packet.stream.index]
    output.mux(packet)

input.close()
output.close()