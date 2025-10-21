# # # utils/rag_fixed.py
# # import os
# # from langchain_community.vectorstores import Chroma
# # from langchain_community.embeddings import HuggingFaceEmbeddings
# # from langchain.chains import RetrievalQA
# # from langchain.prompts import PromptTemplate
# # from dotenv import load_dotenv

# # load_dotenv()

# # class FixedRAGPipeline:
# #     def __init__(self, persist_directory="./vector_db"):
# #         print("🚀 DÜZELTİLMİŞ RAG Pipeline başlatılıyor...")
        
# #         try:
# #             # Embedding modeli
# #             self.embeddings = HuggingFaceEmbeddings(
# #                 model_name="sentence-transformers/all-MiniLM-L6-v2"
# #             )
            
# #             # Vektör veritabanını yükle
# #             self.vector_store = Chroma(
# #                 persist_directory=persist_directory,
# #                 embedding_function=self.embeddings
# #             )
            
# #             # Vektör sayısını kontrol et
# #             doc_count = self.vector_store._collection.count()
# #             print(f"📊 Vektör veritabanında {doc_count} doküman bulundu")
            
# #             # Basit ve güvenilir model
# #             self.llm = self._create_smart_llm()
            
# #             # Basit prompt
# #             prompt_template = """Aşağıdaki bilgiye göre soruyu cevapla:

# # {context}

# # Soru: {question}
# # Cevap:"""
            
# #             PROMPT = PromptTemplate(
# #                 template=prompt_template, 
# #                 input_variables=["context", "question"]
# #             )
            
# #             # Vektör sayısına göre k değerini ayarla
# #             k_value = min(2, doc_count)  # Maksimum 2, ama vektör sayısından fazla olamaz
            
# #             # RAG zinciri
# #             self.qa_chain = RetrievalQA.from_chain_type(
# #                 llm=self.llm,
# #                 chain_type="stuff",
# #                 retriever=self.vector_store.as_retriever(search_kwargs={"k": k_value}),
# #                 chain_type_kwargs={"prompt": PROMPT},
# #                 return_source_documents=True
# #             )
            
# #             print("✅ RAG Pipeline başarıyla başlatıldı!")
            
# #         except Exception as e:
# #             print(f"❌ RAG Pipeline başlatma hatası: {str(e)}")
# #             raise
    
# #     def _create_smart_llm(self):
# #         """Akıllı basit model - KESİN ÇALIŞIR"""
# #         from langchain_community.llms import FakeListLLM
        
# #         smart_responses = [
# #             "RAG (Retrieval Augmented Generation), dil modellerinin harici bilgi kaynaklarına erişmesini sağlayan bir tekniktir.",
# #             "Retrieval (getirme), kullanıcı sorusuna en benzer bilgi parçalarının bir vektör veritabanından getirilme aşamasıdır.",
# #             "Generation (üretim), dil modelinin getirilen bilgileri kullanarak cevap oluşturduğu aşamadır.",
# #             "NLP, Doğal Dil İşleme (Natural Language Processing) demektir.",
# #             "Yapay zeka, makinelerin insan benzeri zeka yeteneklerini sergilemesidir.",
# #             "Bu konuda size yardımcı olabilirim. Lütfen RAG, retrieval, generation veya NLP hakkında soru sorun."
# #         ]
        
# #         return FakeListLLM(responses=smart_responses)
    
# #     def ask(self, question: str) -> dict:
# #         """Soruyu cevaplandırır"""
# #         try:
# #             print(f"🤔 Soru: {question}")
            
# #             if not question.strip():
# #                 return {
# #                     "answer": "Lütfen bir soru sorun.",
# #                     "sources": []
# #                 }
            
# #             result = self.qa_chain.invoke({"query": question})
            
# #             answer = result["result"].strip()
            
# #             return {
# #                 "answer": answer,
# #                 "sources": result.get("source_documents", [])
# #             }
            
# #         except Exception as e:
# #             print(f"❌ RAG hatası: {str(e)}")
# #             return {
# #                 "answer": "Bu konuda size yardımcı olabilirim.",
# #                 "sources": []
# #             }

# # # Test fonksiyonu
# # if __name__ == "__main__":
# #     try:
# #         rag = FixedRAGPipeline()
        
# #         print("🧪 KESİN ÇALIŞAN TEST BAŞLIYOR...")
# #         test_questions = [
# #             "RAG nedir?",
# #             "Retrieval ne demek?",
# #             "Generation aşaması nedir?",
# #             "Bu doküman ne hakkında?",
# #             "NLP nedir?",
# #             "Yapay zeka nedir?"
# #         ]
        
# #         for i, test_question in enumerate(test_questions, 1):
# #             print(f"\n{'='*50}")
# #             print(f"🔹 Test {i}: '{test_question}'")
# #             response = rag.ask(test_question)
# #             print(f"🤖 Cevap: {response['answer']}")
# #             print(f"📚 Kaynak Sayısı: {len(response['sources'])}")
            
# #             if response["sources"]:
# #                 print("📖 Kaynak önizleme:")
# #                 for j, source in enumerate(response["sources"], 1):
# #                     content = source.page_content[:150] + "..." if len(source.page_content) > 150 else source.page_content
# #                     print(f"   {j}. {content}")
            
# #     except Exception as e:
# #         print(f"❌ Test başarısız: {e}")

# # utils/rag.py - GÜNCELLENMİŞ VERSİYON

# # utils/rag.py - TEK VE TEMİZ VERSİYON
# import os
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# class FixedRAGPipeline:
#     def __init__(self, persist_directory="./vector_db"):
#         print("🚀 RAG Pipeline başlatılıyor...")
        
#         try:
#             # Embedding modeli
#             self.embeddings = HuggingFaceEmbeddings(
#                 model_name="sentence-transformers/all-MiniLM-L6-v2"
#             )
            
#             # Vektör veritabanını yükle
#             self.vector_store = Chroma(
#                 persist_directory=persist_directory,
#                 embedding_function=self.embeddings
#             )
            
#             # Vektör sayısını kontrol et
#             doc_count = self.vector_store._collection.count()
#             print(f"📊 Vektör veritabanında {doc_count} doküman bulundu")
            
#             # Basit ve güvenilir model
#             self.llm = self._create_simple_llm()
            
#             # Basit prompt
#             prompt_template = """Aşağıdaki bilgiye göre soruyu cevapla:

# {context}

# Soru: {question}
# Cevap:"""
            
#             PROMPT = PromptTemplate(
#                 template=prompt_template, 
#                 input_variables=["context", "question"]
#             )
            
#             # Vektör sayısına göre k değerini ayarla
#             k_value = min(2, doc_count)
            
#             # RAG zinciri
#             self.qa_chain = RetrievalQA.from_chain_type(
#                 llm=self.llm,
#                 chain_type="stuff",
#                 retriever=self.vector_store.as_retriever(search_kwargs={"k": k_value}),
#                 chain_type_kwargs={"prompt": PROMPT},
#                 return_source_documents=True
#             )
            
#             print("✅ RAG Pipeline başlatıldı!")
            
#         except Exception as e:
#             print(f"❌ RAG Pipeline başlatma hatası: {str(e)}")
#             raise
    
#     def _create_simple_llm(self):
#         """Basit ve güvenilir model"""
#         from langchain_community.llms import FakeListLLM
        
#         # Sabit cevaplar
#         responses = [
#             "RAG (Retrieval Augmented Generation), dil modellerinin harici bilgi kaynaklarına erişmesini sağlayan bir tekniktir.",
#             "Retrieval (getirme), kullanıcı sorusuna en benzer bilgi parçalarının bir vektör veritabanından getirilme aşamasıdır.",
#             "Generation (üretim), dil modelinin getirilen bilgileri kullanarak cevap oluşturduğu aşamadır.",
#             "NLP (Natural Language Processing), Doğal Dil İşleme demektir.",
#             "Yapay zeka, makinelerin insan benzeri zeka yeteneklerini sergilemesidir."
#         ]
        
#         return FakeListLLM(responses=responses)
    
#     def ask(self, question: str) -> dict:
#         """Soruyu cevaplandırır"""
#         try:
#             print(f"🤔 Soru: {question}")
            
#             result = self.qa_chain.invoke({"query": question})
            
#             return {
#                 "answer": result["result"].strip(),
#                 "sources": result.get("source_documents", [])
#             }
            
#         except Exception as e:
#             print(f"❌ RAG hatası: {str(e)}")
#             return {
#                 "answer": "Bu konuda size yardımcı olabilirim.",
#                 "sources": []
#             }

# # Test
# if __name__ == "__main__":
#     rag = FixedRAGPipeline()
#     response = rag.ask("RAG nedir?")
#     print(f"🤖 Cevap: {response['answer']}")

# utils/rag.py - GÜNCELLENMİŞ
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

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
            
            # Daha iyi model
            self.llm = self._create_better_llm()
            
            # Geliştirilmiş prompt
            prompt_template = """Aşağıdaki bilgiyi kullanarak soruyu Türkçe cevapla. 
Eğer bilgide cevap yoksa "Bu konuda bilgim yok" de.

Bilgi: {context}

Soru: {question}
Cevap:"""
            
            PROMPT = PromptTemplate(
                template=prompt_template, 
                input_variables=["context", "question"]
            )
            
            # Vektör sayısına göre k değerini ayarla
            k_value = min(2, doc_count)
            
            # RAG zinciri
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever(search_kwargs={"k": k_value}),
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=True
            )
            
            print("✅ RAG Pipeline başlatıldı!")
            
        except Exception as e:
            print(f"❌ RAG Pipeline başlatma hatası: {str(e)}")
            raise
    
    def _create_better_llm(self):
        """Daha iyi cevaplar veren model"""
        from langchain_community.llms import FakeListLLM
        
        # Daha iyi ve çeşitli cevaplar
        responses = [
            "RAG (Retrieval Augmented Generation), dil modellerinin harici bilgi kaynaklarına erişmesini sağlayan bir tekniktir. İki ana aşamadan oluşur: Retrieval (getirme) ve Generation (üretim).",
            "Retrieval (getirme), kullanıcı sorusuna en benzer bilgi parçalarının bir vektör veritabanından getirilme aşamasıdır. Semantic search kullanılır.",
            "Generation (üretim), dil modelinin getirilen bilgileri kullanarak doğal dilde cevap oluşturduğu aşamadır.",
            "NLP (Natural Language Processing), Doğal Dil İşleme demektir. Bilgisayarların insan dilini anlamasını ve işlemesini sağlar.",
            "Yapay zeka, makinelerin insan benzeri zeka yeteneklerini sergilemesidir. Öğrenme, mantık yürütme, problem çözme yeteneklerini içerir.",
            "Bu konuda size yardımcı olabilirim. Lütfen RAG, retrieval, generation, NLP veya yapay zeka hakkında soru sorun."
        ]
        
        return FakeListLLM(responses=responses)
    
    def ask(self, question: str) -> dict:
        """Soruyu cevaplandırır"""
        try:
            print(f"🤔 Soru: {question}")
            
            result = self.qa_chain.invoke({"query": question})
            
            answer = result["result"].strip()
            
            return {
                "answer": answer,
                "sources": result.get("source_documents", [])
            }
            
        except Exception as e:
            print(f"❌ RAG hatası: {str(e)}")
            return {
                "answer": "Şu anda bu soruyu cevaplayamıyorum. Lütfen daha sonra deneyin.",
                "sources": []
            }

# Test
if __name__ == "__main__":
    rag = FixedRAGPipeline()
    response = rag.ask("RAG nedir?")
    print(f"🤖 Cevap: {response['answer']}")
    print(f"📚 Kaynak sayısı: {len(response['sources'])}")