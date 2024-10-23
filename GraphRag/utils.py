
import litellm
import os
from json_repair import loads
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings


#https://cookbook.chromadb.dev/core/document-ids/#uuids

os.environ["OPENAI_API_KEY"] = "any"
BASE_URL = "http://localhost:8080/"
MODEL_NAME = "gpt-4o"
client = chromadb.PersistentClient('chroma_docs')

litellm.set_verbose = False
def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]



class Embed(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        import numpy as np
        # embed the documents somehow
        #embedding_dict =  litellm.embedding('openai/text',input=input,api_base=BASE_URL,dimensions=384).data
        embedding_dict =  litellm.embedding('openai/text',input=input,api_base=BASE_URL).data
        embedding_list = [e['embedding'] for e in embedding_dict]
        return np.array(embedding_list)
        #return embeddings

electronic_collection = client.get_or_create_collection('electronic',
                                                        embedding_function= Embed(),
                                                        metadata={"hnsw:space": "ip"} # "l2", "ip, "or "cosine"

                                                        )

question_collection = client.get_or_create_collection('questions')


def completion(msg,sys_msg="",JSON=True,temperature=0.0):

    messages = [{"role":"system","content":sys_msg},
                {"role": "user", "content":msg }]
    r= litellm.completion(
        model=MODEL_NAME,
        messages=messages,
        base_url=BASE_URL,
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ], 
        response_format= {"type": "json_object"} if JSON else None,
        temperature=temperature,
        
    )
     
    j= r.choices[0].message.content
    return loads(j) if JSON else j



RAG_SYSTEM_PROMPT="""

---Role---

You are a helpful assistant responding to questions about data in the tables provided.


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.

If you don't know the answer, just say so. Do not make anything up.

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:

"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Sources (15, 16), Reports (1), Entities (5, 7); Relationships (23); Claims (2, 7, 34, 46, 64, +more)]."

where 15, 16, 1, 5, 7, 23, 2, 7, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.


---Target response length and format---

{response_type}


---Data tables---

{context_data}


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.

If you don't know the answer, just say so. Do not make anything up.

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:

"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Sources (15, 16), Reports (1), Entities (5, 7); Relationships (23); Claims (2, 7, 34, 46, 64, +more)]."

where 15, 16, 1, 5, 7, 23, 2, 7, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do NOT include information where the supporting evidence for it is NOT provided. If you can not answer based on the provided text just say so and do not continiue.

---Target response length and format---

{response_type}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.

"""
RESPONSE_TYPE = "multiple paragraphs"
def answer_to_quesion(collection , question,prompt=RAG_SYSTEM_PROMPT,isjson=False):
    rag_results = collection.query(query_texts=question,n_results=5)
    context_text=""
    for _id,_text in zip(rag_results['ids'][0],rag_results['documents'][0]):
        context_text += f"[Data: Source unit_text {_id}]\n{_text}\n"
    
    rag_system_prompt = prompt.format(
        
                context_data=context_text, response_type=RESPONSE_TYPE
            )
    llm_result = completion(question,rag_system_prompt,isjson)
    return llm_result



#%%

import pandas as pd
from fpdf import FPDF

# Load the CSV file into a DataFrame

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CSV to PDF Table', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def create_table(self, df):
        # Table header
        self.set_font('Arial', 'B', 12)
        for col in df.columns:
            self.cell(40, 10, col, 1, 0, 'C')
        self.ln()

        # Table body
        self.set_font('Arial', '', 12)
        for i in range(len(df)):
            for col in df.columns:
                self.cell(40, 10, str(df[col].iloc[i]), 1, 0, 'C')
            self.ln()

# Create a PDF instance
def df_to_pdf(df,path):
    pdf = PDF()
    pdf.add_page()

    # Add table to PDF
    pdf.create_table(df)

    # Save PDF to file
    pdf.output(path)
    print("PDF created successfully!")


def df_to_html(df,path):
    import pandas as pd
    # Define custom styles


    # Replace \n with <br> in the DataFrame
    df = df.replace('\n', '<br>', regex=True)

    # Define custom styles for zebra stripes, a black background, and a fixed header
    styles = '''
    <style>
    html, body {
        height: 100%;
        margin: 0;
        background-color: black;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        color: white;
        table-layout: fixed;
        height: 100vh;
    }
    th, td {
        text-align: center;
        padding: 8px;
        border: 1px solid white;
        white-space: pre-wrap;  /* Ensures text wraps and <br> is recognized */
    }
    th {
        position: sticky;
        top: 0;
        background-color: #222222;
        z-index: 10;
    }
    tr:nth-child(even) {
        background-color: #333333;
    }
    tr:nth-child(odd) {
        background-color: #555555;
    }
    body {
        background-color: black;
    }
    tbody {
        display: block;
        overflow-y: auto;
        height: 100%;
    }
    table thead, table tbody tr {
        display: table;
        width: 100%;
        table-layout: fixed;
    }
    </style>
    '''

    # Convert DataFrame to HTML with added style
    # Using escape=False allows rendering the HTML tags
    html = styles + df.to_html(index=False, classes="zebra", justify='center', escape=False)

    # Write the HTML to a file (optional)
    with open(path, "w") as file:
        file.write(html)

    # Print the HTML

