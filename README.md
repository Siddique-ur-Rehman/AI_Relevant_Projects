# 🤖 AI Customer Support Analyzer (Streamlit + Gemini)

This Streamlit web app allows you to analyze customer messages using Google’s Gemini LLM. For each message, the app returns:

- **Category** (one of 7 allowed labels)  
- **Sentiment** (Positive, Neutral, Negative)  
- **Professional Auto-Reply**  

The system ensures all outputs are **strictly JSON**, validated, and consistent with task rules.  

---

## **Features**

- Streamlit-based clean UI  
- Real-time processing of customer messages  
- Strict enforcement of allowed categories and sentiments  
- Short, professional auto-replies  
- Robust error handling and fallback for invalid outputs  
- Optional JSON view for evaluators  

---

## **Allowed Labels**

**Categories:**  
- Complaint  
- Refund/Return  
- Sales Inquiry  
- Delivery Question  
- Account/Technical Issue  
- General Query  
- Spam  

**Sentiments:**  
- Positive  
- Neutral  
- Negative  

---

## **Setup Instructions**

### 1) Clone the repository
```bash
git clone <your-repo-url>
cd ai_support_streamlit
