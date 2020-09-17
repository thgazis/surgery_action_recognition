from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

def slice(video_path,slice_file):
    video_files = os.listdir(video_path)
    print(video_files)
    for video_file in video_files[:10]:
        video = os.path.join(video_path, video_file)
        clip = VideoFileClip(video)
        duration = clip.duration
        start_time = 0
        end_time = 3
        while end_time < duration:
            slice_video = os.path.join(slice_file, (str(start_time)+video_file[7:-4]))
            print(slice_video)
            ffmpeg_extract_subclip(video, start_time, end_time, targetname=slice_video)
            start_time = end_time
            end_time += 3
    
    return os.path.join(os.getcwd(), video_path), os.path.join(os.getcwd(), slice_file)