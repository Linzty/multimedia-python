from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('audio\See You Again Bardcore.mp3')

# Menyimpan file audio
audio.export('output_audio/result.mp3', format='mp3')

#Cutting file audio
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('output_audio/clipped_result.mp3', format='mp3')

#mixing file audio
combined_audio = audio + clipped_audio
combined_audio.export('output_audio/combined_result.mp3', format='mp3')

#konvert file audio
audio.export('output_audio/result.wav', format='wav')

