import fitz

with fitz.open("students.pdf") as pdf:
  for page in pdf:
    print(20*"====") # page separation
    print(page.get_text())

    page1= pdf[0].get_text()
    print(page1)
    