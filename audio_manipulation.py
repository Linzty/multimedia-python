from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export(output_path + 'clipped_result.mp3', format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Penggabungan dengan validasi durasi
        combined_audio = audio + clipped_audio
        combined_audio.export(output_path + 'combined_result.mp3', format='mp3')
        print("✅ Penggabungan berhasil")

        # Operasi Konversi Format
        audio.export(output_path + 'result.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -10:
            louder_audio = audio - 10  # Meningkatkan volume sebesar 10dB
            louder_audio.export(output_path + 'louder_result.mp3', format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            raise ValueError("Volume audio sudah terlalu tinggi")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('audio/See You Again Bardcore.mp3', 'output_task2/')
