import fitz  
from sentence_transformers import SentenceTransformer, util

class ResumeScreening:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def start_screening(self,resume_path, job_description, match_rate):
        resume_text = self.extract_text_from_pdf(resume_path)
        resume_embedding = self.get_sentence_embeddings(resume_text)
        job_description_embedding = self.get_sentence_embeddings(job_description)
        result = self.min_match_satisfied(resume_embedding, job_description_embedding, match_rate)
        return result
        
    def extract_text_from_pdf(self, file_path):
        document = fitz.open(file_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text

    def get_sentence_embeddings(self, text):
        return self.model.encode(text, convert_to_tensor=True)

    def min_match_satisfied(self, resume_embedding,job_description_embedding,  match_rate):
        match_rate = match_rate
        cosine_sim = util.pytorch_cos_sim(resume_embedding, job_description_embedding).item()
        normalized_score = (cosine_sim + 1) / 2 
        return normalized_score * 100 >= match_rate