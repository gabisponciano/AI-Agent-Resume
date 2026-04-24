from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate



db_path = "vector_db"

prompt_template = """You are an expert in IT professional resumes.

Answer the user's question: {question}

Based on the following information:
{context}

If you cannot find the answer, say that you don't know.

Be simple and direct.
"""
def ai_ask(question):
      embeddings = OllamaEmbeddings(model="nomic-embed-text")

      db = Chroma(persist_directory=db_path, embedding_function = embeddings)
      db_results = db.similarity_search_with_relevance_scores(question)

      if len(db_results) == 0 or db_results[0][1] < 0.7:
            print("Could not find a relevant answer.")
      results_texts = []
      for result in db_results:
            text = result[0].page_content
            results_texts.append(text)
      context = "\n\n----\n\n".join(results_texts)

      prompt = ChatPromptTemplate.from_template(prompt_template)
      prompt = prompt.invoke({"question":question, "context":context})

      model = OllamaLLM(model="llama3")
      test_result = model.invoke(prompt)
      print(test_result)
      return test_result      


