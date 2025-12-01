FROM python:3.11-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential pkg-config wget yasm nasm git \
    libmp3lame-dev libopus-dev libflac-dev \
    && rm -rf /var/lib/apt/lists/*

# Build FDK-AAC
RUN git clone https://github.com/mstorsjo/fdk-aac.git /tmp/fdk-aac && \
    cd /tmp/fdk-aac && ./autogen.sh && ./configure --prefix=/usr --disable-static && \
    make -j$(nproc) && make install && rm -rf /tmp/fdk-aac

# Build FFmpeg with fdk-aac
RUN git clone https://git.ffmpeg.org/ffmpeg.git /tmp/ffmpeg && \
    cd /tmp/ffmpeg && \
    ./configure \
        --enable-gpl \
        --enable-nonfree \
        --enable-libfdk-aac \
        --enable-libmp3lame \
        --enable-libopus \
        --enable-libflac \
        --prefix=/usr && \
    make -j$(nproc) && make install && rm -rf /tmp/ffmpeg

# Install PyAV (will detect ffmpeg libs inside container)
RUN pip install av
