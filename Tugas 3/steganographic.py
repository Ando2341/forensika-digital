from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import base64

def create_steganographic_pdf(pdf_file, output_pdf, logo_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        writer = PdfWriter()

        # Set new metadata
        new_metadata = {
            '/Title': 'Prototipe Sistem Monitoring Suhu, Ketinggian Air, dan Kontrol Otomatis pada Budidaya Ikan dalam Ember Berbasis IoT',
            '/Author': 'Abdul Yazid1, Weny Indah Kusumawati, Ridha Febriliana',
            '/Subject': 'Jurnal',
            '/Creator': 'Human',
            '/Producer': 'LPPM Telkom University Surabaya',
            '/Keywords': 'Internet of Things, Kontroling, Monitoring'
        }

        # Retrieve old metadata
        old_metadata = pdf_reader.metadata

        # Combine old and new metadata
        all_metadata = {**old_metadata, **new_metadata}

        # Hide old and new metadata
        for metadata_key, metadata_value in all_metadata.items():
            encoded_value = base64.b64encode(metadata_value.encode()).decode().replace('O', 'S')
            writer.add_metadata({metadata_key: encoded_value})

        # Add a new page at the beginning to hide the logo
        c = canvas.Canvas("output/logo_page1.pdf", pagesize=letter)
        c.setFillColorRGB(1, 1, 1)  # Set text color to white
        logo_data = base64.b64encode(open(logo_file, 'rb').read()).decode().replace('O', 'S')
        c.drawString(100, 100, logo_data)  # Add logo data as hidden text
        c.save()
        with open("output/logo_page1.pdf", 'rb') as logo_page_file:
            logo_page_reader = PdfReader(logo_page_file)
            logo_page = logo_page_reader.pages[0]
            writer.add_page(logo_page)

        # Add original pages
        for page in pdf_reader.pages:
            writer.add_page(page)

        # Add a new page at the end to hide metadata
        metadata_data = '\n'.join([f"{key}: {value}" for key, value in all_metadata.items()])
        metadata_data_encoded = base64.b64encode(metadata_data.encode()).decode().replace('O', 'S')

        # Add a new page with hidden metadata
        c = canvas.Canvas("output/metadata_page1.pdf", pagesize=letter)
        c.setFillColorRGB(1, 1, 1)  # Set text color to white
        c.drawString(100, 100, metadata_data_encoded)
        c.save()
        with open("output/metadata_page1.pdf", 'rb') as metadata_file:
            metadata_reader = PdfReader(metadata_file)
            metadata_page = metadata_reader.pages[0]
            writer.add_page(metadata_page)

        # Save the modified PDF
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf = "JAIIT_0502_0004+online.pdf"
output_pdf = "output/encoded_jurna1.pdf"
logo_file = "logo.png"
create_steganographic_pdf(input_pdf, output_pdf, logo_file)
