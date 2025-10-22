import os
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

def load_and_process_documents(data_folder="./data"):
    """
    Basit text dosyası yükleyici
    """
    documents = []
    
    print("📁 Veri dosyaları taranıyor...")
    
    # data klasörü yoksa oluştur
    os.makedirs(data_folder, exist_ok=True)
    
    # data klasöründeki tüm dosyaları kontrol et
    for file in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file)
        
        if file.endswith(".txt"):
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
    
    # BASİT metin bölme
    texts = []
    for doc in documents:
        content = doc.page_content
        # 1000 karakterlik parçalara böl
        for i in range(0, len(content), 800):
            chunk = content[i:i+1000]
            if len(chunk.strip()) > 50:  # Boş parçaları atla
                new_doc = Document(
                    page_content=chunk,
                    metadata=doc.metadata.copy()
                )
                texts.append(new_doc)
    
    print(f"✂️ {len(documents)} doküman → {len(texts)} metin parçası oluşturuldu")
    
    return texts

if __name__ == "__main__":
    texts = load_and_process_documents()
    if texts:
        print(f"\n🧪 İlk parça önizleme:")
        print(f"İçerik: {texts[0].page_content[:200]}...")
        print(f"Kaynak: {texts[0].metadata.get('source', 'Bilinmiyor')}")