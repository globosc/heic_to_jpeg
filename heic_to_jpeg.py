from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()

def convert_heic_files_in_folder(folder_path, output_folder):
    try:
        folder_path = Path(folder_path)
        output_folder = Path(output_folder)

        if not output_folder.exists():
            output_folder.mkdir(parents=True)

        total_files = 0
        converted_files = 0

        for input_heic in folder_path.rglob('*.heic'):
            total_files += 1
            output_jpeg = output_folder / (input_heic.stem + '.jpg')

            image = Image.open(input_heic)
            image.save(output_jpeg, "JPEG", quality=95)

            converted_files += 1
            print(f'Convertido {input_heic} a {output_jpeg}')

            # Calcula y muestra el porcentaje de avance
            progress = (converted_files / total_files) * 100
            print(f'Progreso: {progress:.2f}%\n')

        print(f'Se han convertido {converted_files} de {total_files} archivos correctamente.')

    except Exception as e:
        print(f'Se produjo un error al convertir los archivos: {e}')

if __name__ == "__main__":
    input_folder =  Path(r"D:\photos\cam")
    output_folder =  Path(r"D:\photos\cam_jpeg")

    convert_heic_files_in_folder(input_folder, output_folder)
