import moviepy as mp

cvt_video = mp.VideoFileClip("outro.mov")
ext_audio = cvt_video.audio
ext_audio.write_audiofile("reel_extracted_audio2.mp3")
print("Audio extraction complete.")