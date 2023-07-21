from PyPDF2 import PdfReader, PdfWriter

def split_pdf(pdf_path, split_length):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        original_width = page.mediabox.width
        original_height = page.mediabox.height
        
        if original_height > split_length:
            num_splits = int(original_height / split_length) + 1
            start_y = original_height
            end_y = original_height - split_length

            for i in range(num_splits):
                new_page = writer.add_blank_page(width=original_width, height=split_length)

                # Copy content from the original page to the new page
                new_page.merge_page(page)

                # Crop the new page
                new_page.mediabox.lower_left = (0, 0)
                new_page.mediabox.upper_right = (original_width, split_length)

                start_y = end_y
                end_y -= split_length
                if end_y < 0:
                    end_y = 0

        else:
            writer.add_page(page)

    with open(pdf_path, "wb") as output_file:
        writer.write(output_file)