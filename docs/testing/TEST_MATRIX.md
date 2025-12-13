# Test Matrix
## Overview
This document summarizes the compatibility and feature testing performed on the simpleav library.
## Legend
✔️ Pass  
❌ Fail  
⚠️ Partial  
— Not tested
 
## Audio Tests
| Extension  | Codec     | Sample Format |  API  | Status |
|------------|-----------|---------------|-------|--------|
| .3gp       | aac       | u8            |   Y   |   ✔️   |
| .3gp       | aac       | s16           |   Y   |   ✔️   |
| .3gp       | aac       | s16p          |   Y   |   ✔️   |
| .3gp       | aac       | s32           |   Y   |   ✔️   |
| .3gp       | aac       | s32p          |   Y   |   ✔️   |
| .3gp       | aac       | flt           |   Y   |   ✔️   |
| .3gp       | aac       | fltp          |   Y   |   ✔️   |
| .3gp       | aac       | dbl           |   Y   |   ✔️   |
| .3gp       | aac       | dblp          |   Y   |   ✔️   |
| .aac       | aac       | u8            |   Y   |   ✔️   |
| .aac       | aac       | s16           |   Y   |   ✔️   |
| .aac       | aac       | s16p          |   Y   |   ✔️   |
| .aac       | aac       | s32           |   Y   |   ✔️   |
| .aac       | aac       | s32p          |   Y   |   ✔️   |
| .aac       | aac       | flt           |   Y   |   ✔️   |
| .aac       | aac       | fltp          |   Y   |   ✔️   |
| .aac       | aac       | dbl           |   Y   |   ✔️   |
| .aac       | aac       | dblp          |   Y   |   ✔️   |
| .adts      | aac       | u8            |   Y   |   ✔️   |
| .adts      | aac       | s16           |   Y   |   ✔️   |
| .adts      | aac       | s16p          |   Y   |   ✔️   |
| .adts      | aac       | s32           |   Y   |   ✔️   |
| .adts      | aac       | s32p          |   Y   |   ✔️   |
| .adts      | aac       | flt           |   Y   |   ✔️   |
| .adts      | aac       | fltp          |   Y   |   ✔️   |
| .adts      | aac       | dbl           |   Y   |   ✔️   |
| .adts      | aac       | dblp          |   Y   |   ✔️   |
| .aif       | pcm_s8    | u8            |   Y   |   ✔️   |
| .aif       | pcm_s8    | dblp          |   N   |   ❌   |
| .aif       | pcm_s16le | s16           |   Y   |   ✔️   |
| .aif       | pcm_s16le | s16p          |   N   |   ❌   |
| .aif       | pcm_s16be | s16           |   Y   |   ✔️   |
| .aif       | pcm_s16be | s16p          |   N   |   ❌   |
| .aif       | pcm_s24be | s32           |   Y   |   ✔️   |
| .aif       | pcm_s24be | s32p          |   Y   |   ✔️   |
| .aif       | pcm_s32le | s32           |   N   |   ❌   |
| .aif       | pcm_s32le | s32p          |   N   |   ❌   |
| .aif       | pcm_s32be | s32           |   Y   |   ✔️   |
| .aif       | pcm_s32be | s32p          |   Y   |   ✔️   |
| .aifc      | pcm_s8    | u8            |   Y   |   ✔️   |
| .aifc      | pcm_s16le | s16           |   Y   |   ✔️   |
| .aifc      | pcm_s16le | s16p          |   N   |   ❌   |
| .aifc      | pcm_s16be | s16           |   Y   |   ✔️   |
| .aifc      | pcm_s16be | s16p          |   N   |   ❌   |
| .aifc      | pcm_s24be | s32           |   Y   |   ✔️   |
| .aifc      | pcm_s24be | s32p          |   Y   |   ✔️   |
| .aifc      | pcm_s32be | s32           |   Y   |   ✔️   |
| .aifc      | pcm_s32be | s32p          |   Y   |   ✔️   |
| .aiff      | pcm_s8    | u8            |   Y   |   ✔️   |
| .aiff      | pcm_s16le | s16           |   Y   |   ✔️   |
| .aiff      | pcm_s16le | s16p          |   N   |   ❌   |
| .aiff      | pcm_s16be | s16           |   Y   |   ✔️   |
| .aiff      | pcm_s16be | s16p          |   N   |   ❌   |
| .aiff      | pcm_s24be | s32           |   Y   |   ✔️   |
| .aiff      | pcm_s24be | s32p          |   Y   |   ✔️   |
| .aiff      | pcm_s32be | s32           |   Y   |   ✔️   |
| .aiff      | pcm_s32be | s32p          |   Y   |   ✔️   |
| .flac      | flac      | s16           |   Y   |   ✔️   |
| .flac      | flac      | s16p          |   N   |   ❌   |
| .flac      | flac      | s32           |   Y   |   ✔️   |
| .flac      | flac      | s32p          |   N   |   ❌   |
| .flac      | flac      | flt           |   N   |   ❌   |
| .flac      | flac      | fltp          |   N   |   ❌   |
| .m4a       | aac       | fltp          |   Y   |   ✔️   | 
| .m4a       | alac      | s16           |   Y   |   ✔️   |
| .m4a       | alac      | s16p          |   Y   |   ✔️   |
| .m4a       | alac      | s32           |   Y   |   ✔️   |
| .m4a       | alac      | s32p          |   Y   |   ✔️   |
| .m4a       | alac      | flt           |   Y   |   ✔️   |
| .m4a       | alac      | fltp          |   Y   |   ✔️   |
| .mp3       | mp3       | s16           |   Y   |   ✔️   |
| .mp3       | mp3       | s16p          |   Y   |   ✔️   |
| .mp3       | mp3       | flt           |   Y   |   ✔️   |
| .mp3       | mp3       | fltp          |   Y   |   ✔️   |
| .oga       | vorbis    | fltp          |   Y   |   ✔️   |
| .oga       | opus      | flt           |   Y   |   ✔️   |
| .oga       | opus      | fltp          |   N   |   ❌   |
| .oga       | speex     | flt           |   Y   |   ✔️   |
| .oga       | speex     | fltp          |   Y   |   ✔️   |
| .oga       | flac      | s16           |   Y   |   ✔️   |
| .oga       | flac      | s16p          |   N   |   ❌   |
| .oga       | flac      | s32           |   Y   |   ✔️   |
| .oga       | flac      | s32p          |   N   |   ❌   |
| .ogg       | vorbis    | fltp          |   Y   |   ✔️   |
| .ogg       | opus      | flt           |   Y   |   ✔️   |
| .ogg       | speex     | flt           |   Y   |   ✔️   |
| .ogg       | speex     | fltp          |   Y   |   ✔️   |
| .ogg       | flac      | s16           |   Y   |   ✔️   |
| .ogg       | flac      | s32           |   Y   |   ✔️   |
| .ogg       | flac      | flt           |   Y   |   ✔️   |
| .opus      | opus      | flt           |   Y   |   ✔️   |
| .opus      | opus      | fltp          |   N   |   ❌   |
| .wav       | pcm_alaw  | s16           |   Y   |   ✔️   |
| .wav       | pcm_alaw  | s16p          |   Y   |   ✔️   |
| .wav       | pcm_mulaw | s16           |   Y   |   ✔️   |
| .wav       | pcm_mulaw | s16p          |   Y   |   ✔️   |
| .wav       | pcm_s8    | u8            |   N   |   ❌   |
| .wav       | pcm_s16le | s16           |   Y   |   ✔️   |
| .wav       | pcm_s16be | s16           |   Y   |   ✔️   |
| .wav       | pcm_s24le | s32           |   Y   |   ✔️   |
| .wav       | pcm_s24le | s32p          |   Y   |   ✔️   |
| .wav       | pcm_s32le | s32           |   Y   |   ✔️   |
| .wav       | pcm_s32le | s32p          |   Y   |   ✔️   |
| .wma       | wmav1     | s16           |   Y   |   ✔️   |
| .wma       | wmav2     | s16           |   Y   |   ✔️   |


Notes: 
aac not supported with .webm
alac not supported with .webm
hevc not supported with .avi
opus not supported with .avi, .m4v
speex not supported with .m4v, .webm
vorbis not supported with .flv, .webm

flac not supported with .m4v, .webm

# Video Tests 1
(video format compatibility tests against video codecs and pixel formats)

| Extension  | Codec     | Pixel Format  |  API  | Status |
|------------|-----------|---------------|-------|--------|
| .asf       | wmv1      | yuv420p       |   Y   |   ✔️   |
| .asf       | wmv2      | yuv420p       |   Y   |   ✔️   |
| .avi       | mpeg4     | yuv420p       |   Y   |   ✔️   |
| .avi       | h264      | yuv420p       |   Y   |   ✔️   |
| .avi       | h264      | yuv422p       |   N   |   ❌   |
| .avi       | h264      | yuv444p       |   N   |   ❌   |
| .avi       | h264      | yuv420p10le   |   N   |   ❌   |
| .avi       | h264      | yuv422p10le   |   N   |   ❌   |
| .avi       | h264      | yuv422p10le   |   N   |   ❌   |
| .avi       | h264      | nv12          |   Y   |   ✔️   |
| .flv       | flv       | yuv420p       |   Y   |   ⚠️   |
| .flv       | h264      | yuv420p       |   Y   |   ⚠️   |
| .flv       | h264      | nv12          |   Y   |   ⚠️   |
| .m4v       | mpeg4     | yuv420p       |   Y   |   ✔️   |
| .m4v       | h264      | yuv420p       |   Y   |   ✔️   |
| .m4v       | h264      | nv12          |   Y   |   ✔️   |
| .mov       | mpeg4     | yuv420p       |   Y   |   ✔️   |
| .mov       | h264      | yuv420p       |   Y   |   ✔️   |
| .mov       | h264      | nv12          |   Y   |   ✔️   |
| .mov       | hevc      | yuv420p       |   Y   |   ✔️   |
| .mov       | hevc      | yuv422p       |   Y   |   ✔️   |
| .mov       | hevc      | yuv444p       |   Y   |   ✔️   |
| .mov       | hevc      | yuv420p10le   |   Y   |   ✔️   |
| .mov       | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .mov       | hevc      | yuv444p10le   |   Y   |   ✔️   |
| .mp4       | h264      | yuv420p       |   Y   |   ✔️   |
| .mp4       | h264      | nv12          |   Y   |   ✔️   |
| .mp4       | hevc      | yuv420p       |   Y   |   ✔️   |
| .mp4       | hevc      | yuv422p       |   Y   |   ✔️   |
| .mp4       | hevc      | yuv444p       |   Y   |   ✔️   |
| .mp4       | hevc      | yuv420p10le   |   Y   |   ✔️   |
| .mp4       | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .mp4       | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .mp4       | mpeg4     | yuv420p       |   Y   |   ✔️   |
| .mpg       | mpeg1video| yuv420p       |   Y   |   ✔️   |
| .mpg       | mpeg2video| yuv420p       |   Y   |   ✔️   |
| .mpeg      | mpeg1video| yuv420p       |   Y   |   ✔️   |
| .mpeg      | mpeg2video| yuv420p       |   Y   |   ✔️   |
| .mkv       | av1       | yuv420p       |   N   |   ❌   |
| .mkv       | av1       | yuv422p       |   N   |   ❌   |
| .mkv       | av1       | yuv444p       |   N   |   ❌   |
| .mkv       | av1       | yuv420p10le   |   N   |   ❌   |
| .mkv       | av1       | yuv422p10le   |   N   |   ❌   |
| .mkv       | av1       | yuv444p10le   |   N   |   ❌   |
| .mkv       | h264      | yuv420p       |   Y   |   ✔️   |
| .mkv       | h264      | nv12          |   Y   |   ✔️   |
| .mkv       | hevc      | yuv420p       |   Y   |   ✔️   |
| .mkv       | hevc      | yuv422p       |   Y   |   ✔️   |
| .mkv       | hevc      | yuv444p       |   Y   |   ✔️   |
| .mkv       | hevc      | yuv420p10le   |   Y   |   ✔️   |
| .mkv       | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .mkv       | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .mkv       | mpeg4     | yuv420p       |   Y   |   ⚠️   |
| .mkv       | vp8       | yuv420p       |   N   |   ⚠️   |
| .mkv       | vp8       | yuv422p       |   N   |   ❌   |
| .mkv       | vp8       | yuv444p       |   N   |   ❌   |
| .mkv       | vp9       | yuv420p       |   N   |   ❌   |
| .mkv       | vp9       | yuv422p       |   N   |   ❌   |
| .mkv       | vp9       | yuv444p       |   N   |   ❌   |
| .mkv       | vp9       | yuv420p10le   |   N   |   ❌   |
| .mkv       | vp9       | yuv422p10le   |   N   |   ❌   |
| .mkv       | vp9       | yuv444p10le   |   N   |   ❌   |
| .ts        | mpeg2video| yuv420p       |   Y   |   ⚠️   |
| .ts        | h264      | yuv420p       |   Y   |   ✔️   |
| .ts        | h264      | nv12          |   Y   |   ✔️   |
| .ts        | hevc      | yuv420p       |   Y   |   ✔️   |
| .ts        | hevc      | yuv422p       |   Y   |   ✔️   |
| .ts        | hevc      | yuv444p       |   Y   |   ✔️   |
| .ts        | hevc      | yuv420p10le   |   Y   |   ✔️   |
| .ts        | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .ts        | hevc      | yuv422p10le   |   Y   |   ✔️   |
| .webm      | av1       | yuv420p       |   Y   |   ❌   |
| .webm      | av1       | yuv422p       |   Y   |   ❌   |
| .webm      | av1       | yuv444p       |   Y   |   ❌   |
| .webm      | av1       | yuv420p10le   |   Y   |   ❌   |
| .webm      | av1       | yuv422p10le   |   Y   |   ❌   |
| .webm      | av1       | yuv444p10le   |   Y   |   ❌   |
| .webm      | vp8       | yuv420p       |   Y   |   ⚠️   |
| .webm      | vp8       | yuv422p       |   Y   |   ⚠️   |
| .webm      | vp8       | yuv444p       |   Y   |   ⚠️   |
| .webm      | vp9       | yuv420p       |   Y   |   ⚠️   |
| .webm      | vp9       | yuv422p       |   Y   |   ⚠️   |
| .webm      | vp9       | yuv444p       |   Y   |   ⚠️   |
| .webm      | vp9       | yuv420p10le   |   Y   |   ⚠️   |
| .webm      | vp9       | yuv422p10le   |   Y   |   ⚠️   |
| .webm      | vp9       | yuv444p10le   |   Y   |   ⚠️   |
| .wmv       | wmv1      | yuv420p       |   Y   |   ✔️   | 

# Video tests 2 
(video format compatibility tests against audio codecs)

| Extension  | Codec          |  API  | Status |
|------------|----------------|-------|--------|
| .asf       | aac            |       |        |
| .asf       | alac           |       |        |
| .asf       | flac           |       |        |
| .asf       | mp3            |       |        |
| .asf       | opus           |       |        |
| .asf       | pcm_alaw       |       |        |
| .asf       | pcm_mulaw      |       |        |
| .asf       | pcm_s8         |       |        |
| .asf       | pcm_s16le      |       |        |
| .asf       | pcm_s16be      |       |        |
| .asf       | pcm_s24le      |       |        |
| .asf       | pcm_s24be      |       |        |
| .asf       | pcm_s32le      |       |        |
| .asf       | pcm_s32be      |       |        |
| .asf       | speex          |       |        |
| .asf       | vorbis         |       |        |
| .asf       | wmav1          |       |        |
| .asf       | wmav2          |       |        |
| .avi       | aac            |       |        |
| .avi       | alac           |       |        |
| .avi       | flac           |       |        |
| .avi       | mp3            |       |        |
| .avi       | opus           |       |        |
| .avi       | pcm_alaw       |       |        |
| .avi       | pcm_mulaw      |       |        |
| .avi       | pcm_s8         |       |        |
| .avi       | pcm_s16le      |       |        |
| .avi       | pcm_s16be      |       |        |
| .avi       | pcm_s24le      |       |        |
| .avi       | pcm_s24be      |       |        |
| .avi       | pcm_s32le      |       |        |
| .avi       | pcm_s32be      |       |        |
| .avi       | speex          |       |        |
| .avi       | vorbis         |       |        |
| .avi       | wmav1          |       |        |
| .avi       | wmav2          |       |        |
| .flv       | aac            |       |        |
| .flv       | alac           |       |        |
| .flv       | flac           |       |        |
| .flv       | mp3            |       |        |
| .flv       | opus           |       |        |
| .flv       | pcm_alaw       |       |        |
| .flv       | pcm_mulaw      |       |        |
| .flv       | pcm_s8         |       |        |
| .flv       | pcm_s16le      |       |        |
| .flv       | pcm_s16be      |       |        |
| .flv       | pcm_s24le      |       |        |
| .flv       | pcm_s24be      |       |        |
| .flv       | pcm_s32le      |       |        |
| .flv       | pcm_s32be      |       |        |
| .flv       | speex          |       |        |
| .flv       | vorbis         |       |        |
| .flv       | wmav1          |       |        |
| .flv       | wmav2          |       |        |
| .m4v       | aac            |       |        |
| .m4v       | alac           |       |        |
| .m4v       | flac           |       |        |
| .m4v       | mp3            |       |        |
| .m4v       | opus           |       |        |
| .m4v       | pcm_alaw       |       |        |
| .m4v       | pcm_mulaw      |       |        |
| .m4v       | pcm_s8         |       |        |
| .m4v       | pcm_s16le      |       |        |
| .m4v       | pcm_s16be      |       |        |
| .m4v       | pcm_s24le      |       |        |
| .m4v       | pcm_s24be      |       |        |
| .m4v       | pcm_s32le      |       |        |
| .m4v       | pcm_s32be      |       |        |
| .m4v       | speex          |       |        |
| .m4v       | vorbis         |       |        |
| .m4v       | wmav1          |       |        |
| .m4v       | wmav2          |       |        |
| .mov       | aac            |       |        |
| .mov       | alac           |       |        |
| .mov       | flac           |       |        |
| .mov       | mp3            |       |        |
| .mov       | opus           |       |        |
| .mov       | pcm_alaw       |       |        |
| .mov       | pcm_mulaw      |       |        |
| .mov       | pcm_s8         |       |        |
| .mov       | pcm_s16le      |       |        |
| .mov       | pcm_s16be      |       |        |
| .mov       | pcm_s24le      |       |        |
| .mov       | pcm_s24be      |       |        |
| .mov       | pcm_s32le      |       |        |
| .mov       | pcm_s32be      |       |        |
| .mov       | speex          |       |        |
| .mov       | vorbis         |       |        |
| .mov       | wmav1          |       |        |
| .mov       | wmav2          |       |        |
| .mp4       | aac            |       |        |
| .mp4       | alac           |       |        |
| .mp4       | flac           |       |        |
| .mp4       | mp3            |       |        |
| .mp4       | opus           |       |        |
| .mp4       | pcm_alaw       |       |        |
| .mp4       | pcm_mulaw      |       |        |
| .mp4       | pcm_s8         |       |        |
| .mp4       | pcm_s16le      |       |        |
| .mp4       | pcm_s16be      |       |        |
| .mp4       | pcm_s24le      |       |        |
| .mp4       | pcm_s24be      |       |        |
| .mp4       | pcm_s32le      |       |        |
| .mp4       | pcm_s32be      |       |        |
| .mp4       | speex          |       |        |
| .mp4       | vorbis         |       |        |
| .mp4       | wmav1          |       |        |
| .mp4       | wmav2          |       |        |
| .mpg       | aac            |       |        |
| .mpg       | alac           |       |        |
| .mpg       | flac           |       |        |
| .mpg       | mp3            |       |        |
| .mpg       | opus           |       |        |
| .mpg       | pcm_alaw       |       |        |
| .mpg       | pcm_mulaw      |       |        |
| .mpg       | pcm_s8         |       |        |
| .mpg       | pcm_s16le      |       |        |
| .mpg       | pcm_s16be      |       |        |
| .mpg       | pcm_s24le      |       |        |
| .mpg       | pcm_s24be      |       |        |
| .mpg       | pcm_s32le      |       |        |
| .mpg       | pcm_s32be      |       |        |
| .mpg       | speex          |       |        |
| .mpg       | vorbis         |       |        |
| .mpg       | wmav1          |       |        |
| .mpg       | wmav2          |       |        |
| .mpeg      | aac            |       |        |
| .mpeg      | alac           |       |        |
| .mpeg      | flac           |       |        |
| .mpeg      | mp3            |       |        |
| .mpeg      | opus           |       |        |
| .mpeg      | pcm_alaw       |       |        |
| .mpeg      | pcm_mulaw      |       |        |
| .mpeg      | pcm_s8         |       |        |
| .mpeg      | pcm_s16le      |       |        |
| .mpeg      | pcm_s16be      |       |        |
| .mpeg      | pcm_s24le      |       |        |
| .mpeg      | pcm_s24be      |       |        |
| .mpeg      | pcm_s32le      |       |        |
| .mpeg      | pcm_s32be      |       |        |
| .mpeg      | speex          |       |        |
| .mpeg      | vorbis         |       |        |
| .mpeg      | wmav1          |       |        |
| .mpeg      | wmav2          |       |        |
| .mkv       | aac            |       |        |
| .mkv       | alac           |       |        |
| .mkv       | flac           |       |        |
| .mkv       | mp3            |       |        |
| .mkv       | opus           |       |        |
| .mkv       | pcm_alaw       |       |        |
| .mkv       | pcm_mulaw      |       |        |
| .mkv       | pcm_s8         |       |        |
| .mkv       | pcm_s16le      |       |        |
| .mkv       | pcm_s16be      |       |        |
| .mkv       | pcm_s24le      |       |        |
| .mkv       | pcm_s24be      |       |        |
| .mkv       | pcm_s32le      |       |        |
| .mkv       | pcm_s32be      |       |        |
| .mkv       | speex          |       |        |
| .mkv       | vorbis         |       |        |
| .mkv       | wmav1          |       |        |
| .mkv       | wmav2          |       |        |
| .ts        | aac            |       |        |
| .ts        | alac           |       |        |
| .ts        | flac           |       |        |
| .ts        | mp3            |       |        |
| .ts        | opus           |       |        |
| .ts        | pcm_alaw       |       |        |
| .ts        | pcm_mulaw      |       |        |
| .ts        | pcm_s8         |       |        |
| .ts        | pcm_s16le      |       |        |
| .ts        | pcm_s16be      |       |        |
| .ts        | pcm_s24le      |       |        |
| .ts        | pcm_s24be      |       |        |
| .ts        | pcm_s32le      |       |        |
| .ts        | pcm_s32be      |       |        |
| .ts        | speex          |       |        |
| .ts        | vorbis         |       |        |
| .ts        | wmav1          |       |        |
| .ts        | wmav2          |       |        |
| .webm      | aac            |       |        |
| .webm      | alac           |       |        |
| .webm      | flac           |       |        |
| .webm      | mp3            |       |        |
| .webm      | opus           |       |        |
| .webm      | pcm_alaw       |       |        |
| .webm      | pcm_mulaw      |       |        |
| .webm      | pcm_s8         |       |        |
| .webm      | pcm_s16le      |       |        |
| .webm      | pcm_s16be      |       |        |
| .webm      | pcm_s24le      |       |        |
| .webm      | pcm_s24be      |       |        |
| .webm      | pcm_s32le      |       |        |
| .webm      | pcm_s32be      |       |        |
| .webm      | speex          |       |        |
| .webm      | vorbis         |       |        |
| .webm      | wmav1          |       |        |
| .webm      | wmav2          |       |        |
| .wmv       | aac            |       |        |
| .wmv       | alac           |       |        |
| .wmv       | flac           |       |        |
| .wmv       | mp3            |       |        |
| .wmv       | opus           |       |        |
| .wmv       | pcm_alaw       |       |        |
| .wmv       | pcm_mulaw      |       |        |
| .wmv       | pcm_s8         |       |        |
| .wmv       | pcm_s16le      |       |        |
| .wmv       | pcm_s16be      |       |        |
| .wmv       | pcm_s24le      |       |        |
| .wmv       | pcm_s24be      |       |        |
| .wmv       | pcm_s32le      |       |        |
| .wmv       | pcm_s32be      |       |        |
| .wmv       | speex          |       |        |
| .wmv       | vorbis         |       |        |
| .wmv       | wmav1          |       |        |
| .wmv       | wmav2          |       |        |


