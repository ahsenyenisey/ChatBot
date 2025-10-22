import streamlit as st
import sys
import os

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Akbank RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Gerekli modülleri ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.rag import FixedRAGPipeline

def initialize_rag():
    """RAG pipeline'ını başlat"""
    try:
        if 'rag' not in st.session_state:
            with st.spinner('🤖 RAG sistemi başlatılıyor...'):
                st.session_state.rag = FixedRAGPipeline()
        return True
    except Exception as e:
        st.error(f"❌ RAG sistemi başlatılamadı: {str(e)}")
        return False

def main():
    st.title("🤖 Akbank RAG Chatbot")
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ Hakkında")
        st.write("""
        **Akbank GenAI Bootcamp** projesi kapsamında geliştirilmiş RAG tabanlı chatbot.
        """)
        
        st.header("💡 Örnek Sorular")
        questions = [
            "RAG nedir?",
            "Retrieval ne demek?", 
            "NLP nedir?",
            "Yapay zeka nedir?"
        ]
        for q in questions:
            if st.button(q):
                st.session_state.user_input = q
    
    # Sistem başlat
    if not initialize_rag():
        return
    
    # Sohbet geçmişi
    if 'messages' not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", 
            "content": "👋 Merhaba! Size nasıl yardımcı olabilirim?"
        }]
    
    # Mesajları göster
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Kullanıcı girişi
    user_input = st.chat_input("Sorunuzu yazın...")
    
    if 'user_input' in st.session_state:
        user_input = st.session_state.user_input
        del st.session_state.user_input
    
    if user_input:
        # Kullanıcı mesajı
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Asistan cevabı
        with st.chat_message("assistant"):
            with st.spinner("🤔 Düşünüyorum..."):
                try:
                    response = st.session_state.rag.ask(user_input)
                    
                    # Cevap
                    st.markdown(response['answer'])
                    
                    # Geçmişe ekle
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response['answer']
                    })
                    
                except Exception as e:
                    error_msg = f"❌ Hata oluştu: {str(e)}"
                    st.error(error_msg)

if __name__ == "__main__":
    main()