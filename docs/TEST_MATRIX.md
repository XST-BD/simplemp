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

# Video Tests
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


