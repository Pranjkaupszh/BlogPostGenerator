# 📝 BlogPostGenerator.AI
Create professional, engaging, and SEO-friendly blog posts in seconds using AI.

This Streamlit application allows you to generate full-length blog content with customizable tone, automatic summaries, and relevant hashtags — all optimized for readability and social sharing.

# 🌟 Key Features

AI-Powered Blog Writing: Uses Groq LLM (Meta LLaMA) to produce natural, human-like blog content.

Custom Tone Options: Choose from professional, casual, educational, or any tone that suits your audience.

SEO-Ready: Generates keyword-rich content for better search engine visibility.

Smart Hashtags: Generates relevant hashtags, formatted for LinkedIn or social media.

Interactive Streamlit Interface: Simple UI to enter prompts, select word count, and generate posts instantly.

# 💻 Installation
Prerequisites:

Python 3.10 (or higher)

Groq API Key 

Steps:

1.Clone the repository:

git clone https://github.com/Pranjkaupszh/BlogPostGenerator.git

cd BlogPostGenerator


2.Install required packages:
pip install -r requirements.txt


3.Configure your Groq API key for Streamlit:

Create a folder .streamlit with file secrets.toml inside your project directory and place you api key there:

GROQ_API_KEY = "your_api_key_here"

# 🚀 Usage

Run the Streamlit application:

streamlit run blogpostapp.py

or 

flask run blogpostapp.py


Open http://localhost:8501 or (//localhost:5000)
 in your browser.

Enter your blog topic or prompt.

Set the desired word count and tone (optional).

Click Generate Blog.

You’ll get: Title of the blog post,Full blog content,Summary,Hashtags for social sharing

# 🗂 Project Structure
blogpostapp.py : Streamlit UI for blog generation

blogpostgenerator.py : Core AI logic for generating blogs

.streamlit/secrets.toml : Groq API key configuration

requirements.txt : Dependencies

# 📊 How It Works

Prompt Handling: The user provides a topic or prompt.

Tone Selection: AI automatically detects tone if none is specified.

Blog Generation: Groq LLM writes a natural, coherent blog post with proper formatting.

Content Cleaning: Stray HTML/Markdown is removed.

