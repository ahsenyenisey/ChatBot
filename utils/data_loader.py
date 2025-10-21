import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_process_documents(data_folder="./data"):
    """
    PDF ve text dosyalarını yükler, işler ve parçalara ayırır
    """
    documents = []
    
    print("📁 Veri dosyaları taranıyor...")
    
    # data klasörü yoksa oluştur
    os.makedirs(data_folder, exist_ok=True)
    
    # data klasöründeki tüm dosyaları kontrol et
    for file in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file)
        
        if file.endswith(".pdf"):
            print(f"📖 PDF yükleniyor: {file}")
            try:
                loader = PyPDFLoader(file_path)
                loaded_docs = loader.load()
                documents.extend(loaded_docs)
                print(f"✅ {file} başarıyla yüklendi - {len(loaded_docs)} sayfa")
            except Exception as e:
                print(f"❌ {file} yüklenirken hata: {e}")
                
        elif file.endswith(".txt"):
            print(f"📝 Text dosyası yükleniyor: {file}")
            try:
                loader = TextLoader(file_path, encoding='utf-8')
                loaded_docs = loader.load()
                documents.extend(loaded_docs)
                print(f"✅ {file} başarıyla yüklendi")
            except Exception as e:
                print(f"❌ {file} yüklenirken hata: {e}")
    
    if not documents:
        print("⚠️ Hiç doküman bulunamadı! Lütfen data/ klasörüne PDF veya txt dosyası ekleyin.")
        return []
    
    print(f"📊 Toplam {len(documents)} doküman yüklendi")
    
    # Metinleri parçalara ayır
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # Her parça 1000 karakter
        chunk_overlap=200,    # Parçalar 200 karakter örtüşsün
        length_function=len,
    )
    
    texts = text_splitter.split_documents(documents)
    print(f"✂️ {len(documents)} doküman → {len(texts)} metin parçası oluşturuldu")
    
    return texts

# Test fonksiyonu
if __name__ == "__main__":
    texts = load_and_process_documents()
    if texts:
        print(f"\n🧪 İlk parça önizleme:")
        print(f"İçerik: {texts[0].page_content[:200]}...")
        print(f"Kaynak: {texts[0].metadata.get('source', 'Bilinmiyor')}")
        print(f"Sayfa: {texts[0].metadata.get('page', 'Bilinmiyor')}")