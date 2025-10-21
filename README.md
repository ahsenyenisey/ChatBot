# 🤖 Akbank RAG Chatbot

## 🎯 Proje Amacı
Retrieval Augmented Generation (RAG) teknolojisi kullanarak akıllı soru-cevap chatbotu geliştirmek.

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