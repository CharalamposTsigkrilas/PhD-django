from docx import Document
from django.conf import settings
import os
from docxtpl import DocxTemplate
from docxcompose.composer import Composer


def convert_to_docx(template, output_file, d):
    doc = DocxTemplate(template)
    doc.render(d)
    doc.save(output_file)

def convert_multiple_to_docx(template, output_file, dd):
    for i, gc in enumerate(dd):
        doc = DocxTemplate( template )
        doc.render(gc)
        doc.save(output_file)

        if i==0:
            master = Document(output_file)
            composer = Composer(master)
        else:
            doc = Document(output_file)
            composer.append(doc)    
    composer.save(output_file)

def abs_tmp_filename(target_filename):
    tmp_media = settings.MEDIA_TMP_EXPORT  
    abs_filename = os.path.join(tmp_media, target_filename) 
    return abs_filename
