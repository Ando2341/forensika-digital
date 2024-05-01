from PyPDF2 import PdfReader
from datetime import datetime

def get_pdf_metadata(pdf_file):
    # Create a PdfReader object
    pdf_reader = PdfReader(pdf_file)

    # Get metadata
    metadata = {
        'Title': pdf_reader.metadata.get('/Title', "Tidak ada judul"),
        'Author': pdf_reader.metadata.get('/Author', "Tidak ada informasi penulis"),
        'Subject': pdf_reader.metadata.get('/Subject', "Tidak ada subjek"),
        'Creator': pdf_reader.metadata.get('/Creator', "Tidak ada pencipta"),
        'Producer': pdf_reader.metadata.get('/Producer', "Tidak ada produsen"),
        'Publisher': pdf_reader.metadata.get('/Publisher', "Tidak ada publisher"),
        'Creation Date': pdf_reader.metadata.get('/CreationDate', "Tidak ada informasi tanggal pembuatan"),
        'Modification Date': pdf_reader.metadata.get('/ModDate', "Tidak ada informasi tanggal modifikasi"),
        'Keywords': pdf_reader.metadata.get('/Keywords', "Tidak ada kata kunci")
    }

    return metadata

pdf_file_path = 'JAIIT_0502_0004+online.pdf'
metadata = get_pdf_metadata(pdf_file_path)
print("Metadata Dokumen PDF:")
for key, value in metadata.items():
    print(f"{key}: {value if value else 'TIDAK ADA METADATA'}")
