
import os 

def convert_srt_to_txt(directory):
    if not os.path.isdir(directory):
        print(f"The directory {directory} dos not exist.")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith(".srt"):
            txt_filename = filename[:-4] + ".txt"
            srt_path = os.path.join(directory, filename)
            txt_path = os.path.join(directory, txt_filename)

            with open(srt_path, 'r', encoding='utf-8') as srt_file:
                srt_content = srt_file.read()

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(srt_content)

            os.remove(srt_path) # delete srt files

            print(f"Converted {filename} to {txt_filename}.")


directory_path = '/Users/perihill/Desktop/UL_2___Clustering_subtitles'
convert_srt_to_txt(directory_path)
