from fastapi import APIRouter, UploadFile, File
from app.ai_service import ai_ask
import PyPDF2
from io import BytesIO
from app.vector_database import chunks_particioner,vectorize_chunks
from langchain_core.documents import Document



ai_router = APIRouter(prefix="/ai_agent", tags=["ai_agent"])

@ai_router.post("/file_upload")
async def file_upload(file: UploadFile = File(...)):
    content = await file.read()

    pdf_reader = PyPDF2.PdfReader(BytesIO(content))

    full_text = ""
    for page in pdf_reader.pages:
        full_text += page.extract_text() or ""

    docs = [Document(page_content=full_text, metadata={"source": file.filename})]

    chunks = chunks_particioner(docs)

    vectorize_chunks(chunks)

    return {"Message": "File processed successfully"}


@ai_router.post("/ai_expert")
def ai_cv_expert(question:str):
      response = ai_ask(question)
      return {"response": response}
