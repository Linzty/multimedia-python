from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        # Memuat gambar
        image = Image.open(input_path)
        print("✅ Gambar berhasil dimuat")

        # Operasi Cropping dengan validasi ukuran
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((2337, 1769, 6847, 3481))
            cropped_image.save(output_path + 'cropped_result.jpg')
            print("✅ Cropping berhasil")
        else:
            raise ValueError("Gambar terlalu kecil untuk di-crop ke ukuran 200x200")

        # Operasi Resizing dengan rasio aspek yang dipertahankan
        resized_image = cropped_image.resize((1024, 720), Image.Resampling.LANCZOS)
        resized_image.save(output_path + 'resized_result.jpg')
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image.save(output_path + 'filtered_result.jpg')
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(2.5)
        bright_image.save(output_path + 'bright_result.jpg')
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered_image, bright_image, alpha=0.5)
        combined_image.save(output_path + 'combined_result.jpg')
        print("✅ Penggabungan gambar berhasil")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_image('Gambar/sf90.jpg', 'output_task2/')
