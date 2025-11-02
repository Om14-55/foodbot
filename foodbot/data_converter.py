import pandas as pd
from langchain_core.documents import Document

def dataconveter():
  data=pd.read_csv("data/updated_food.csv")

  data=data[["ingredients_name","name","ingredients_quantity","instructions"]]

  food_list=[]

  for index,row in data.iterrows():
    obj={
      'ingredients_name':row['ingredients_name'],
      'name':row['name'],
      'ingredients_quantity':row['ingredients_quantity'],
      'instructions':row['instructions']
    }
    food_list.append(obj)

  docs=[]
  for entry in food_list:
    metadata = {
        "name": entry["name"],
        "ingredients_quantity": entry["ingredients_quantity"],
        "instructions": entry["instructions"]
    }
    
    doc = Document(
        page_content=entry["ingredients_name"],  # what we’ll search on
        metadata=metadata
    )
    docs.append(doc)
  return docs


