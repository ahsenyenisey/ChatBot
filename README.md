# 🤖 Akbank RAG Chatbot

## 🎯 Proje Amacı
Retrieval Augmented Generation (RAG) teknolojisi kullanarak akıllı soru-cevap chatbotu geliştirmek.

## Requirements & Configuration
- Python 3.10+
- Create and fill `.env` from `.env.template`
  - `OPENAI_API_KEY` : OpenAI API anahtarınız
  - `HF_TOKEN` : HuggingFace token (opsiyonel)
  - `CHROMA_PERSIST_DIR` : Chroma persist dizini (varsayılan: chroma_db)

## Quick start (local)
1. git clone https://github.com/enesmanan/gaih-chatbot.git
2. python -m venv .venv
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. cp .env.template .env  # .env içine gerekli API anahtarlarını koy
6. python utils/data_loader.py   # veri hazırlama & chunking
7. python utils/embedding.py     # embedding ve Chroma persist
8. streamlit run app.py

## Deployment
- 

## 📊 Veri Seti
- **Kaynak**: Yapay Zeka ve Makine Öğrenmesi terimleri
- **Format**: PDF ve TXT dosya desteği
- **İçerik**: RAG, NLP, Yapay Zeka, Makine Öğrenmesi konuları

## 🛠️ Kullanılan Teknolojiler
- **Framework**: LangChain
- **Vektör DB**: Chroma
- **Embedding**: HuggingFace (sentence-transformers/all-MiniLM-L6-v2)
- **Web Arayüz**: Streamlit
- **LLM**: FakeListLLM (fallback)

## 🚀 Kurulum
```bash
# Sanal ortam oluştur
python -m venv rag_env
source rag_env/bin/activate  # Windows: rag_env\Scripts\activate

# Gerekli paketleri yükle
pip install -r requirements.txt

# Verileri işle ve vektör DB oluştur
python utils/data_loader.py
python utils/embedding.py

# Uygulamayı başlat
streamlit run app.py