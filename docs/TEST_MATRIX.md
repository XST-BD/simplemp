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
