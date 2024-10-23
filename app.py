import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #4B8BBE;
        font-weight: bold;
    }
    .subheader {
        color: #306998;
    }
    .result-box {
        border: 1px solid #cccccc;
        padding: 10px;
        border-radius: 5px;
        background-color: #ffffff;
    }
    .positive {
        color: #28a745;
        font-weight: bold;
    }
    .negative {
        color: #dc3545;
        font-weight: bold;
    }
    .neutral {
        color: #ffc107;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app title
st.markdown("<h1 class='title'>Real-time Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Analyze the sentiment of your text in real-time</h3>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.markdown("<h2 class='subheader'>Input Text</h2>", unsafe_allow_html=True)
user_input = st.sidebar.text_area("Enter Text:", "Type here...")

# Analyze the sentiment of the input text
if st.sidebar.button("Analyze"):
    sentiment_dict = analyzer.polarity_scores(user_input)
    
    # Display the sentiment analysis results
    st.write(f"**Positive:** {sentiment_dict['pos'] * 100:.2f}%")
    st.write(f"**Negative:** {sentiment_dict['neg'] * 100:.2f}%")
    st.write(f"**Neutral:** {sentiment_dict['neu'] * 100:.2f}%")
    st.write(f"**Compound Score:** {sentiment_dict['compound']:.2f}")
    
    # Interpret the compound score
    if sentiment_dict['compound'] >= 0.05:
        st.markdown("<h4 class='positive'>Overall Sentiment: Positive</h4>", unsafe_allow_html=True)
    elif sentiment_dict['compound'] <= -0.05:
        st.markdown("<h4 class='negative'>Overall Sentiment: Negative</h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h4 class='neutral'>Overall Sentiment: Neutral</h4>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<footer><p>Developed by Akhil Sudhakaran</p></footer>", unsafe_allow_html=True)