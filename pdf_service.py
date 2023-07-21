from PyPDF2 import PdfReader, PdfWriter
import math
def split_pdf(pdf_path, split_length):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for idx,page in enumerate(reader.pages):
        original_width = page.mediabox.width
        original_height = page.mediabox.height
        
        if original_height > split_length:
            num_splits = max(int(original_height / split_length),2)+1
            print(num_splits)
            start_y = original_height
            end_y = original_height - split_length

            for i in range(num_splits):
                print(start_y,end_y)

                new_page = PdfReader(pdf_path).pages[idx]
                new_page.mediabox.upper_left = (0, start_y)
                new_page.mediabox.lower_right = (original_width, end_y)
                
                start_y = end_y
                end_y -= split_length
                
                if end_y<0:
                    end_y=0
                
                writer.add_page(new_page)

        else:
            writer.add_page(page)

    with open(pdf_path, "wb") as output_file:
        writer.write(output_file)