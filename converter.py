from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx.all import resize

def create_gif(video_file, gif_file, start_time, end_time, gif_duration, gif_width, text=None):
    # Load the video and select the desired segment
    clip = VideoFileClip(video_file).subclip(start_time, end_time)

    # If text is specified, add it to the GIF
    if text:
        txt_clip = TextClip(text, fontsize=24, color='white')
        txt_clip = txt_clip.set_duration(gif_duration).set_pos('center', 'bottom')
        clip = CompositeVideoClip([clip, txt_clip])

    # Resize and save the GIF
    clip = resize(clip, width=gif_width)
    clip.write_gif(gif_file, fps=15)

# Replace with the path to your video file and the name of the GIF file
video_file = "/path/to/your/videofile.mp4"
gif_file = "/path to/your/file.gif"

# Replace with the start and end times in seconds
start_time = 10
end_time = 20

# GIF duration, GIF width and text
gif_duration = 10
gif_width = 500
text = "Your text is here"

create_gif(video_file, gif_file, start_time, end_time, gif_duration, gif_width, text)
