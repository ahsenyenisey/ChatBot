from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

def create_vector_store(texts, persist_directory="./vector_db"):
    """
    Metinleri vektör veritabanına kaydeder
    """
    print("🔤 Embedding modeli yükleniyor...")
    
    # Embedding modelini yükle
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    print("🗄️ Vektör veritabanı oluşturuluyor...")
    
    # Eski veritabanını temizle (varsa)
    if os.path.exists(persist_directory):
        import shutil
        shutil.rmtree(persist_directory)
    
    # Vektör veritabanını oluştur
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    vector_store.persist()
    print(f"✅ Vektör veritabanı oluşturuldu: {persist_directory}")
    print(f"📊 Toplam {len(texts)} vektör kaydedildi")
    return vector_store

def load_vector_store(persist_directory="./vector_db"):
    """
    Kayıtlı vektör veritabanını yükler
    """
    if not os.path.exists(persist_directory):
        raise FileNotFoundError(f"❌ Vektör veritabanı bulunamadı: {persist_directory}")
    
    print("🔤 Embedding modeli yükleniyor...")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    print("🗄️ Vektör veritabanı yükleniyor...")
    
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    print("✅ Vektör veritabanı yüklendi")
    return vector_store

# Test fonksiyonu
if __name__ == "__main__":
    from data_loader import load_and_process_documents
    
    try:
        texts = load_and_process_documents()
        if texts:
            vector_store = create_vector_store(texts)
            print("🧪 Embedding testi başarılı!")
        else:
            print("❌ Test için veri bulunamadı!")
    except Exception as e:
        print(f"❌ Test başarısız: {e}")