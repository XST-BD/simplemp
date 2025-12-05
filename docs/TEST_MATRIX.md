# Test Matrix
## Overview
This document summarizes the compatibility and feature testing performed on the simpleav library.
## Legend
✔️ Pass  
❌ Fail  
⚠️ Partial  
— Not tested

## Audio Tests
| Extension  | Codec     | Sample Format | Status |
|------------|-----------|---------------|--------|
| .3gp       | aac       | u8            |   ❌   |
| .3gp       | aac       | s16           |   ❌   |
| .3gp       | aac       | s16p          |   ❌   |
| .3gp       | aac       | s32           |   ❌   |
| .3gp       | aac       | s32p          |   ❌   |
| .3gp       | aac       | flt           |   ❌   |
| .3gp       | aac       | fltp          |   ✔️   |
| .3gp       | aac       | dbl           |   ❌   |
| .3gp       | aac       | dblp          |   ❌   |
| .aac       | aac       | u8            |   ✔️   |
| .aac       | aac       | s16           |   ✔️   |
| .aac       | aac       | s16p          |   ✔️   |
| .aac       | aac       | s32           |   ✔️   |
| .aac       | aac       | s32p          |   ✔️   |
| .aac       | aac       | flt           |   ✔️   |
| .aac       | aac       | fltp          |   ✔️   |
| .aac       | aac       | dbl           |   ✔️   |
| .aac       | aac       | dblp          |   ✔️   |
| .adts      | aac       | u8            |   ❌   |
| .adts      | aac       | s16           |   ❌   |
| .adts      | aac       | s16p          |   ❌   |
| .adts      | aac       | s32           |   ❌   |
| .adts      | aac       | s32p          |   ❌   |
| .adts      | aac       | flt           |   ❌   |
| .adts      | aac       | fltp          |   ✔️   |
| .adts      | aac       | dbl           |   ❌   |
| .adts      | aac       | dblp          |   ❌   |
| .aif       | pcm_s8    | u8            |   ✔️   |
| .aif       | pcm_s8    | dblp          |   ❌   |
| .aif       | pcm_s16le | s16           |   ✔️   |
| .aif       | pcm_s16le | s16p          |   ❌   |
| .aif       | pcm_s16be | s16           |   ✔️   |
| .aif       | pcm_s16be | s16p          |   ❌   |
| .aif       | pcm_s24be | s32           |   ✔️   |
| .aif       | pcm_s24be | s32p          |   ❌   |
| .aif       | pcm_s32le | s32           |   ❌   |
| .aif       | pcm_s32le | s32p          |   ❌   |
| .aif       | pcm_s32be | s32           |   ✔️   |
| .aif       | pcm_s32be | s32p          |   ❌   |
| .aifc      | pcm_s8    | u8            |   ✔️   |
| .aifc      | pcm_s16le | s16           |   ✔️   |
| .aifc      | pcm_s16le | s16p          |   ❌   |
| .aifc      | pcm_s16be | s16           |   ✔️   |
| .aifc      | pcm_s16be | s16p          |   ❌   |
| .aifc      | pcm_s24be | s32           |   ✔️   |
| .aifc      | pcm_s24be | s32p          |   ❌   |
| .aifc      | pcm_s32be | s32           |   ✔️   |
| .aifc      | pcm_s32be | s32p          |   ❌   |
| .aiff      | pcm_s8    | u8            |   ✔️   |
| .aiff      | pcm_s16le | s16           |   ✔️   |
| .aiff      | pcm_s16le | s16p          |   ❌   |
| .aiff      | pcm_s16be | s16           |   ✔️   |
| .aiff      | pcm_s16be | s16p          |   ❌   |
| .aiff      | pcm_s24be | s32           |   ✔️   |
| .aiff      | pcm_s24be | s32p          |   ❌   |
| .aiff      | pcm_s32be | s32           |   ✔️   |
| .aiff      | pcm_s32be | s32p          |   ❌   |
| .flac      | flac      | s16           |   ✔️   |
| .flac      | flac      | s16p          |   ❌   |
| .flac      | flac      | s32           |   ✔️   |
| .flac      | flac      | s32p          |   ❌   |
| .flac      | flac      | flt           |   ❌   |
| .flac      | flac      | fltp          |   ❌   |
| .m4a       | aac       | fltp          |   ❌   | 
| .m4a       | alac      | s16           |   ❌   |
| .m4a       | alac      | s16p          |   ✔️   |
| .m4a       | alac      | s32           |   ❌   |
| .m4a       | alac      | s32p          |   ✔️   |
| .m4a       | alac      | flt           |   ❌   |
| .m4a       | alac      | fltp          |   ❌   |
| .mp3       | mp3       | s16           |   ✔️   |
| .mp3       | mp3       | s16p          |   ✔️   |
| .mp3       | mp3       | flt           |   ✔️   |
| .mp3       | mp3       | fltp          |   ✔️   |
| .oga       | vorbis    | fltp          |   ✔️   |
| .oga       | opus      | flt           |   ✔️   |
| .oga       | opus      | fltp          |   ❌   |
| .oga       | speex     | flt           |   ✔️   |
| .oga       | speex     | fltp          |   ✔️   |
| .oga       | flac      | s16           |   ✔️   |
| .oga       | flac      | s16p          |   ❌   |
| .oga       | flac      | s32           |   ✔️   |
| .oga       | flac      | s32p          |   ❌   |
| .ogg       | vorbis    | fltp          |   ✔️   |
| .ogg       | opus      | flt           |   ✔️   |
| .ogg       | speex     | flt           |   ✔️   |
| .ogg       | speex     | fltp          |   ✔️   |
| .ogg       | flac      | s16           |   ✔️   |
| .ogg       | flac      | s32           |   ✔️   |
| .ogg       | flac      | flt           |   ✔️   |
| .opus      | opus      | flt           |   ✔️   |
| .opus      | opus      | fltp          |   ❌   |
| .wav       | pcm_alaw  | s16           |   ✔️   |
| .wav       | pcm_alaw  | s16p          |   ✔️   |
| .wav       | pcm_mulaw | s16           |   ✔️   |
| .wav       | pcm_mulaw | s16p          |   ✔️   |
| .wav       | pcm_s8    | u8            |   ❌   |
| .wav       | pcm_s16le | s16           |   ✔️   |
| .wav       | pcm_s16be | s16           |   ✔️   |
| .wav       | pcm_s24le | s32           |   ✔️   |
| .wav       | pcm_s24le | s32p          |   ✔️   |
| .wav       | pcm_s32le | s32           |   ✔️   |
| .wav       | pcm_s32le | s32p          |   ✔️   |
| .wma       | wmav1     | s16           |   ✔️   |
| .wma       | wmav2     | s16           |   ✔️   |

# Video Tests
| Extension  | Codec     | Pixel Format  | Status |
|------------|-----------|---------------|--------|
| .asf       | wmv1      | yuv420p       |        |
| .asf       | wmv2      | yuv420p       |        |
| .avi       | mpeg4     | yuv420p       |        |
| .avi       | h264      | yuv420p       |        |
| .avi       | h264      | yuv422p       |        |
| .avi       | h264      | yuv444p       |        |
| .avi       | h264      | yuv420p10le   |        |
| .avi       | h264      | yuv422p10le   |        |
| .avi       | h264      | yuv422p10le   |        |
| .avi       | h264      | nv12          |        |
| .avi       | hevc      | yuv420p       |        |
| .avi       | hevc      | yuv422p       |        |
| .avi       | hevc      | yuv444p       |        |
| .avi       | hevc      | yuv420p10le   |        |
| .avi       | hevc      | yuv422p10le   |        |
| .avi       | hevc      | yuv422p10le   |        |
| .flv       | flv       | yuv420p       |        |
| .flv       | h264      | yuv420p       |        |
| .flv       | h264      | yuv422p       |        |
| .flv       | h264      | yuv444p       |        |
| .flv       | h264      | yuv420p10le   |        |
| .flv       | h264      | yuv422p10le   |        |
| .flv       | h264      | yuv422p10le   |        |
| .flv       | h264      | nv12          |        |
| .m4v       | mpeg4     | yuv420p       |        |
| .m4v       | h264      | yuv420p       |        |
| .m4v       | h264      | yuv422p       |        |
| .m4v       | h264      | yuv444p       |        |
| .m4v       | h264      | yuv420p10le   |        |
| .m4v       | h264      | yuv422p10le   |        |
| .m4v       | h264      | yuv422p10le   |        |
| .m4v       | h264      | nv12          |        |
| .mov       | mpeg4     | yuv420p       |        |
| .mov       | h264      | yuv420p       |        |
| .mov       | h264      | yuv422p       |        |
| .mov       | h264      | yuv444p       |        |
| .mov       | h264      | yuv420p10le   |        |
| .mov       | h264      | yuv422p10le   |        |
| .mov       | h264      | yuv422p10le   |        |
| .mov       | h264      | nv12          |        |
| .mov       | hevc      | yuv420p       |        |
| .mov       | hevc      | yuv422p       |        |
| .mov       | hevc      | yuv444p       |        |
| .mov       | hevc      | yuv420p10le   |        |
| .mov       | hevc      | yuv422p10le   |        |
| .mov       | hevc      | yuv422p10le   |        |
| .mp4       | av1       | yuv420p       |        |
| .mp4       | av1       | yuv422p       |        |
| .mp4       | av1       | yuv444p       |        |
| .mp4       | av1       | yuv420p10le   |        |
| .mp4       | av1       | yuv422p10le   |        |
| .mp4       | av1       | yuv422p10le   |        |
| .mp4       | h264      | yuv420p       |        |
| .mp4       | h264      | yuv422p       |        |
| .mp4       | h264      | yuv444p       |        |
| .mp4       | h264      | yuv420p10le   |        |
| .mp4       | h264      | yuv422p10le   |        |
| .mp4       | h264      | yuv422p10le   |        |
| .mp4       | h264      | nv12          |        |
| .mp4       | hevc      | yuv420p       |        |
| .mp4       | hevc      | yuv422p       |        |
| .mp4       | hevc      | yuv444p       |        |
| .mp4       | hevc      | yuv420p10le   |        |
| .mp4       | hevc      | yuv422p10le   |        |
| .mp4       | hevc      | yuv422p10le   |        |
| .mp4       | mpeg4     | yuv420p       |        |
| .mpg       | mpeg1video| yuv420p       |        |
| .mpg       | mpeg2video| yuv420p       |        |
| .mpeg      | mpeg1video| yuv420p       |        |
| .mpeg      | mpeg2video| yuv420p       |        |
| .mkv       | av1       | yuv420p       |        |
| .mkv       | av1       | yuv422p       |        |
| .mkv       | av1       | yuv444p       |        |
| .mkv       | av1       | yuv420p10le   |        |
| .mkv       | av1       | yuv422p10le   |        |
| .mkv       | av1       | yuv444p10le   |        |
| .mkv       | h264      | yuv420p       |        |
| .mkv       | h264      | yuv422p       |        |
| .mkv       | h264      | yuv444p       |        |
| .mkv       | h264      | yuv420p10le   |        |
| .mkv       | h264      | yuv422p10le   |        |
| .mkv       | h264      | yuv422p10le   |        |
| .mkv       | h264      | nv12          |        |
| .mkv       | hevc      | yuv420p       |        |
| .mkv       | hevc      | yuv422p       |        |
| .mkv       | hevc      | yuv444p       |        |
| .mkv       | hevc      | yuv420p10le   |        |
| .mkv       | hevc      | yuv422p10le   |        |
| .mkv       | hevc      | yuv422p10le   |        |
| .mkv       | mpeg4     | yuv420p       |        |
| .mkv       | vp8       | yuv420p       |        |
| .mkv       | vp8       | yuv422p       |        |
| .mkv       | vp8       | yuv444p       |        |
| .mkv       | vp9       | yuv420p       |        |
| .mkv       | vp9       | yuv422p       |        |
| .mkv       | vp9       | yuv444p       |        |
| .mkv       | vp9       | yuv420p10le   |        |
| .mkv       | vp9       | yuv422p10le   |        |
| .mkv       | vp9       | yuv444p10le   |        |
| .ts        | mpeg2video| yuv420p       |        |
| .ts        | h264      | yuv420p       |        |
| .ts        | h264      | yuv422p       |        |
| .ts        | h264      | yuv444p       |        |
| .ts        | h264      | yuv420p10le   |        |
| .ts        | h264      | yuv422p10le   |        |
| .ts        | h264      | yuv422p10le   |        |
| .ts        | h264      | nv12          |        |
| .ts        | hevc      | yuv420p       |        |
| .ts        | hevc      | yuv422p       |        |
| .ts        | hevc      | yuv444p       |        |
| .ts        | hevc      | yuv420p10le   |        |
| .ts        | hevc      | yuv422p10le   |        |
| .ts        | hevc      | yuv422p10le   |        |
| .webm      | av1       | yuv420p       |        |
| .webm      | av1       | yuv422p       |        |
| .webm      | av1       | yuv444p       |        |
| .webm      | av1       | yuv420p10le   |        |
| .webm      | av1       | yuv422p10le   |        |
| .webm      | av1       | yuv444p10le   |        |
| .webm      | vp8       | yuv420p       |        |
| .webm      | vp8       | yuv422p       |        |
| .webm      | vp8       | yuv444p       |        |
| .webm      | vp9       | yuv420p       |        |
| .webm      | vp9       | yuv422p       |        |
| .webm      | vp9       | yuv444p       |        |
| .webm      | vp9       | yuv420p10le   |        |
| .webm      | vp9       | yuv422p10le   |        |
| .webm      | vp9       | yuv444p10le   |        |
| .wmv       | wmv1      | yuv420p       |        | 


