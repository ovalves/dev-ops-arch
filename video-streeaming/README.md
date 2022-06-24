# Video Streaming

## Convertendo o vídeo para HLS
ffmpeg.exe -i streaming/BigBuckBunny/mp4/BigBuckBunny_512kb.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls outputlist.m3u8

