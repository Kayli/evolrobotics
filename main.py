import os
import re

def vtt_to_txt(vtt_folder, output_txt_file):
    with open(output_txt_file, 'w', encoding='utf-8') as output_file:
        for filename in sorted(os.listdir(vtt_folder)):
            if filename.endswith(".vtt"):
                file_path = os.path.join(vtt_folder, filename)
                
                # Write the filename (lecture name) as a heading
                lecture_title = filename.replace(".vtt", "")  # Remove the .vtt extension
                output_file.write(f"\n\n--- {lecture_title} ---\n\n")  # Add separator and title
                
                with open(file_path, 'r', encoding='utf-8') as vtt_file:
                    lines = vtt_file.readlines()
                    seen_lines = set()  # To avoid duplicate lines
                    for line in lines:
                        # Remove timestamps and any other tags
                        cleaned_line = re.sub(r'<[^>]*>', '', line).strip()  # Remove <c> and other tags
                        cleaned_line = re.sub(r'\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}', '', cleaned_line).strip()  # Remove timestamps
                        
                        # Only write lines that are not empty and not duplicates
                        if cleaned_line and cleaned_line not in seen_lines:
                            output_file.write(cleaned_line + '\n')
                            seen_lines.add(cleaned_line)  # Mark this line as seen

    print(f"Text file '{output_txt_file}' has been created.")

# Current working directory
vtt_folder = '.'  # Current folder

# Output .txt file name
output_txt_file = 'cleaned_output_plain.txt'

vtt_to_txt(vtt_folder, output_txt_file)
