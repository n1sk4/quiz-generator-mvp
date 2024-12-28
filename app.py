import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog, messagebox
import pymupdf
from openai import OpenAI

load_dotenv()

def parse_pdf(filepath):
  doc = pymupdf.open(filepath)
  text = ""
  for page in doc:
    text += page.get_text()
  return text

def generate_questions_llm(text, question_types):
  client = OpenAI(
    api_key = os.getenv("LLM_API_KEY"), # .env API Key
    organization = os.getenv("ORG_ID"), # .env Organization Key
    project = os.getenv("PROJECT_ID")   # .env Project ID
  )
  additional_info = ""
  if "abc" in question_types:
    additional_info += "\n* ABC (provide up to 4 different answers with one correct and other three wrong or misleading (separated by a), b), etc)\n"
  if "fill_in" in question_types:
    additional_info += "* FILL IN (questions provide a sentance with a word missing (replaced with '_'), ideally a name or a date/year)\n"
  if "essay" in question_types:
    additional_info += "* ESSAY (leave an empty space after the question)\n"

  prompt = f'''Do not additionally explain, but only generate questions that have answear type: 
{additional_info}
  
please format the question to have a ONLY a number and then the question text, DO NOT, i repeat do not write answear type anywhere in the question, 
followed by the answears if applicable from the text: {text[:1000]}.'''

  completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  
  return completion.choices[0].message.content.strip().split("\n")

def save_questions_to_pdf(questions, output_path):
  doc = pymupdf.open()
  page = doc.new_page()
  text = "\n\n".join(questions)
  page.insert_text((72, 72), text, fontsize=12)
  doc.save(output_path)

def save_questions_to_word(questions, output_path):
  from docx import Document
  doc = Document()
  for q in questions:
    doc.add_paragraph(q)
  doc.save(output_path)

def create_test():
  file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
  if not file_path:
    return

  text = parse_pdf(file_path)
  selected_question_types = [qt for qt, var in question_type_vars.items() if var.get()]

  if not selected_question_types:
    messagebox.showerror("Error", "Please select at least one question type.")
    return

  try:
    questions = generate_questions_llm(text, selected_question_types)
  except Exception as e:
    messagebox.showerror("Error", f"Failed to generate questions: {e}")
    return

  save_format = save_format_var.get()
  output_path = filedialog.asksaveasfilename(defaultextension=f".{save_format}",
                         filetypes=[(f"{save_format.upper()} files", f"*.{save_format}")])
  if not output_path:
    return

  if save_format == "pdf":
    save_questions_to_pdf(questions, output_path)
  elif save_format == "docx":
    save_questions_to_word(questions, output_path)

  messagebox.showinfo("Success", "Test questions saved successfully!")

if __name__ == "__main__":
  root = tk.Tk()
  root.title("Test Question Generator")

  frame = tk.Frame(root)
  frame.pack(pady=20, padx=20)

  tk.Label(frame, text="Select Question Types:").grid(row=0, column=0, sticky="w")
  question_type_vars = {
  "abc"     : tk.BooleanVar(value=False),
  "fill_in" : tk.BooleanVar(value=False),
  "essay"   : tk.BooleanVar(value=False)
  }

  for i, (qt, var) in enumerate(question_type_vars.items()):
    tk.Checkbutton(frame, text=qt.capitalize(), variable=var).grid(row=0, column=i+1)

  tk.Label(frame, text="Save Format:").grid(row=1, column=0, sticky="w")
  save_format_var = tk.StringVar(value="pdf")
  save_formats = ["pdf", "docx"]
  for i, sf in enumerate(save_formats):
    tk.Radiobutton(frame, text=sf.upper(), variable=save_format_var, value=sf).grid(row=1, column=i+1)

  tk.Button(frame, text="Generate Test", command=create_test).grid(row=2, column=0, columnspan=3, pady=10)

  root.mainloop()

  print("Test generator running...")
