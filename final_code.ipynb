import re
import os
import pandas as pd
from collections import defaultdict

def extract(input_string):    
    before_pattern = r'((?:\b[A-Za-z0-9\-\.]+\b\s+){0,5})(\b[A-Za-z0-9\-\.]+)(?=\s+v\b)'
    after_pattern = r'\bv\s+((?:\b[A-Za-z0-9\-\.]+\b\s+){0,5})(\b[A-Za-z0-9\-\.]+)'
    before_match = re.search(before_pattern, input_string, re.IGNORECASE)
    after_match = re.search(after_pattern, input_string, re.IGNORECASE)

    before_words = []
    after_words = []
    if before_match:
        before_words = before_match.group(1).split()
        before_words.append(before_match.group(2))
    if after_match:
        after_words = after_match.group(1).split()
        after_words.append(after_match.group(2))

    if "CITATION" not in before_words:
      return (before_words, after_words)
    else:
      return None

def clean(input):
  remove_string= ["APPLICANT","PTY","Ltd","Pty","LTD","RESPONDENT","APPLICANTS",
                  "Construction"]
  if type(input) == str:
    input = input.split()
  tmp = []
  for word in input:
    if word not in remove_string:
      tmp.append(word)
  return tmp

df = pd.read_excel('/content/drive/MyDrive/DS_PROJ_MAST90106/Data_checks/rbe_case_info_extraction.xlsx')
df = df.fillna("None")
df['refer_file'] = [[] for _ in range(len(df))]
df["refer_ID"] = [[] for _ in range(len(df))]

directory = "/content/drive/MyDrive/DS_PROJ_MAST90106/data/final_data"
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

accessed_file = 0
counter = 0
count_v = 0
extract_dict = defaultdict(int)
success_file = defaultdict(int)

for file_name in txt_files:
  accessed_file +=1
  file_path = os.path.join(directory, file_name)

  with open(file_path, 'r') as file:
    file_contents = file.read()
    file_name = file_name.replace(".txt",".pdf")

    try:
      extraction = extract(file_contents)
      
      if extraction is not None:
        before,after = extraction
        before = clean(before)
        after = clean(after)
        app = before[-1].lower()
        res = after[0].lower()

        if (app and res):
          count_v +=1
          extract_dict[file_name]+=1

        for i in df.index:
          if (app in df.loc[i]["applicant"].lower()) and (res in df.loc[i]["respondent"].lower()):
            if df.loc[i]["doc"] != file_name:
              print("6666666666666666666666666666666666666666",file_name)
              counter+=1
              success_file[file_name]+=1
              ref_file = df.loc[i]["doc"]
              ref_ID = df.loc[i]["vcat_no"] 

              # Get the current lists, append to them, then reassign them
              current_refer_file = df.loc[df["doc"] == file_name, "refer_file"].iloc[0]
              current_refer_ID = df.loc[df["doc"] == file_name, "refer_ID"].iloc[0]

              current_refer_file.append(ref_file)
              current_refer_ID.append(ref_ID)

              df.loc[df["doc"] == file_name, "refer_file"] = [current_refer_file]
              df.loc[df["doc"] == file_name, "refer_ID"] = [current_refer_ID]
    except IndexError:
      pass
      #print("IndexError in file: ", file_name)
    except AttributeError:
      pass
      #print("AttributeError in file: ", file_name)

print(counter)
print(accessed_file)
print(success_file)
print(extract_dict)
print("count_v",count_v)

csv_file_path = "/content/drive/MyDrive/DS_PROJ_MAST90106/data/full/extracted_final.csv"
# Finally, save the DataFrame to the CSV file using the to_csv() method
with open(csv_file_path,"w",encoding = "utf-8") as f:
  df.to_csv(f)
