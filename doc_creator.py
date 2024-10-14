from docxtpl import DocxTemplate

def doc_creator(refarat_mavzusi,refarat_izohi):
    doc = DocxTemplate("my_word_template.docx")
    context = { 'refarad_mazusi' : f"{refarat_mavzusi}",
            "referat_izohi": f"{refarat_izohi}"}
    doc.render(context)
    doc.save("generated_doc.docx")
