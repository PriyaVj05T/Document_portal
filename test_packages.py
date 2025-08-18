import fitz
print(fitz.__file__)
print(fitz.__doc__)

doc = fitz.open(r"D:\\My_data\\Projects\\LLMOPS\\Document_portal\\data\\document_analysis\\NIPS-2017-attention-is-all-you-need-Paper.pdf")

print("Pages:", doc.page_count)


