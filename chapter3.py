from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

# Memuat file video
video = VideoFileClip('Video/Nothings.mp4')

# Menyimpan file video
video.write_videofile('output_video/result.mp4')

short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('output_video/short_result.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('output_video/combined_result.mp4')
