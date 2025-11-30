import av

def debuglog(input, debug : bool):
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