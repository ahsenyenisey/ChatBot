# RAG Chatbot --- Akbank GenAI Bootcamp Projesi

## Proje Amacı

Bu proje, **Retrieval-Augmented Generation (RAG)** mimarisi kullanarak
bir **akıllı bilgi tabanlı chatbot** geliştirmeyi amaçlar.\
Chatbot, kullanıcıdan gelen soruları anlamlandırır, **vektör
veritabanındaki** dokümanlardan ilgili bilgileri getirir ve **LLM (Large
Language Model)** ile doğal dilde yanıt üretir.\
Amaç, kullanıcıların spesifik bir bilgi kümesi hakkında **doğru, bağlama
uygun ve tutarlı** yanıtlar almasını sağlamaktır.

------------------------------------------------------------------------

## Veri Seti Hakkında

Projede kullanılan veri seti, \[örnek belgeler / domain odaklı
içerikler\] içermektedir.\
Bu içerikler chatbot'un bilgi tabanını oluşturur ve **embedding modeli**
yardımıyla vektör uzayına dönüştürülür.\
Veri seti hazırlık süreci şu adımlarla ilerler:

1.  Metin dosyalarının toplanması veya hazırlanması\
2.  Gereksiz karakterlerin, HTML etiketlerinin temizlenmesi\
3.  Chunk'lara bölünmesi (örneğin 500 token'lık parçalar hâlinde)\
4.  Embedding modeliyle (ör. `text-embedding-3-small` veya
    `sentence-transformers/all-MiniLM-L6-v2`) vektörlerin üretilmesi\
5.  Vektörlerin **Chroma** veya **FAISS** gibi bir vektör veritabanına
    kaydedilmesi

------------------------------------------------------------------------

## Kullanılan Yöntemler ve Teknolojiler

  Bileşen                 Teknoloji / Yöntem
  ----------------------- -------------------------------------------
  **Dil Modeli (LLM)**    OpenAI GPT veya Gemini API
  **Embedding**           Sentence Transformers / OpenAI Embeddings
  **Vektör Veritabanı**   ChromaDB
  **RAG Pipeline**        LangChain
  **Web Arayüzü**         Streamlit
  **Backend**             Python (LangChain + Chroma entegrasyonu)
  **Dağıtım (Deploy)**    Streamlit Cloud / Hugging Face Spaces

**Mimari Akış:** 1. Kullanıcı sorusunu girer.\
2. Soru embedding'e dönüştürülür.\
3. Vektör DB'den en alakalı dökümanlar alınır.\
4. Bu bilgiler LLM'e prompt olarak verilir.\
5. LLM bağlama uygun yanıt üretir ve kullanıcıya gösterilir.

------------------------------------------------------------------------

## Kurulum ve Çalıştırma Kılavuzu

### Ortam Kurulumu

``` bash
git clone https://github.com/ahsenyenisey/rag-chatbot.git
cd rag-chatbot
python -m venv venv
source venv/bin/activate    # for macOS / Linux
venv\Scripts\activate       # for Windows
pip install -r requirements.txt
```

### Çalıştırma

``` bash
streamlit run app.py
```

> 📄 Not: API anahtarınızı `.env` dosyasına eklemeyi unutmayın.\
> Örnek `.env` dosyası:
>
>     OPENAI_API_KEY=your_api_key_here

------------------------------------------------------------------------

## Çözüm Mimarisi

              +------------------+
              |   Kullanıcı UI   |
              +--------+---------+
                       |
                       v
              +--------+---------+
              |    Query Parser   |
              +--------+---------+
                       |
                       v
              +--------+---------+
              |  Embedding Model  |
              +--------+---------+
                       |
                       v
              +--------+---------+
              | Vektör Veritabanı |
              +--------+---------+
                       |
                       v
              +--------+---------+
              |   LLM / RAG Core  |
              +--------+---------+
                       |
                       v
              +--------+---------+
              |  Yanıt Üretimi   |
              +------------------+

------------------------------------------------------------------------

## 💻 Web Arayüzü ve Kullanım

Kullanıcı arayüzü, **Streamlit** ile geliştirilmiştir.\
Ana özellikler: - Basit ve anlaşılır sohbet arayüzü
- Yanıt geçmişi görüntüleme
- Bağlama dayalı yanıt üretimi
- (Opsiyonel) kaynak doküman gösterimi

**Canlı Demo:**\
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

------------------------------------------------------------------------

## Sonuçlar

Proje sonucunda: - RAG mimarisiyle bağlama uygun yanıtlar elde edildi.
- Vektör aramasıyla bilgi doğruluğu arttırıldı.
- Web tabanlı arayüz ile kullanıcı deneyimi sade ve erişilebilir hâle
getirildi.

------------------------------------------------------------------------

## Geliştirici

**Ahsen Yenisey**\
🔗 [GitHub Profilim](https://github.com/ahsenyenisey)

------------------------------------------------------------------------

## Kaynaklar

-   [LangChain Docs](https://python.langchain.com/)
-   [ChromaDB](https://www.trychroma.com/)
-   [OpenAI API](https://platform.openai.com/)
-   [Streamlit](https://streamlit.io/)
