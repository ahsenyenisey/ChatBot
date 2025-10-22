import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import FakeListLLM

class FixedRAGPipeline:
    def __init__(self, persist_directory="./vector_db"):
        print("🚀 RAG Pipeline başlatılıyor...")
        
        try:
            # Embedding modeli
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            
            # Vektör veritabanını yükle
            self.vector_store = Chroma(
                persist_directory=persist_directory,
                embedding_function=self.embeddings
            )
            
            # Vektör sayısını kontrol et
            doc_count = self.vector_store._collection.count()
            print(f"📊 Vektör veritabanında {doc_count} doküman bulundu")
            
            # Basit LLM
            self.llm = FakeListLLM(responses=[
                "RAG (Retrieval Augmented Generation), dil modellerinin harici bilgi kaynaklarına erişmesini sağlayan bir tekniktir.",
                "Retrieval aşamasında, kullanıcı sorusuna en benzer bilgi parçaları vektör veritabanından getirilir.",
                "Generation aşamasında, dil modeli getirilen bilgileri kullanarak doğal dilde cevap oluşturur.",
                "NLP (Natural Language Processing), Doğal Dil İşleme anlamına gelir.",
                "Yapay zeka, makinelerin insan benzeri zeka yeteneklerini sergilemesidir.",
            ])
            
            print("✅ RAG Pipeline başlatıldı!")
            
        except Exception as e:
            print(f"❌ RAG Pipeline başlatma hatası: {str(e)}")
            raise
    
    def ask(self, question: str) -> dict:
        """Basit soru-cevap"""
        try:
            print(f"🤔 Soru: {question}")
            
            # Basit benzerlik arama
            docs = self.vector_store.similarity_search(question, k=2)
            
            # Basit cevap oluşturma
            if docs:
                answer = self.llm.invoke(question)
                return {
                    "answer": answer,
                    "sources": docs
                }
            else:
                return {
                    "answer": "Bu konuda bilgim yok.",
                    "sources": []
                }
            
        except Exception as e:
            print(f"❌ RAG hatası: {str(e)}")
            return {
                "answer": "Şu anda bu soruyu cevaplayamıyorum. Lütfen daha sonra deneyin.",
                "sources": []
            }

if __name__ == "__main__":
    rag = FixedRAGPipeline()
    response = rag.ask("RAG nedir?")
    print(f"🤖 Cevap: {response['answer']}")
    print(f"📚 Kaynak sayısı: {len(response['sources'])}")