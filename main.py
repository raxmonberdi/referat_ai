from ai_sorov import gpt_sorov
from doc_creator import doc_creator

refarat_mavzusi = "Alisher Navoiy hayoti va ijodi"
refarat_izoh = gpt_sorov(refarat_mavzusi)
#print(refarat_izoh)
doc_creator(refarat_mavzusi, refarat_izoh)