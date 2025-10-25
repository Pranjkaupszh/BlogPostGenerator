from flask import Flask, request, jsonify
from blogpostgenerator import BlogPostGenerator
import streamlit as st
import os

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_blog():
    data = request.json
    try:
        generator = BlogPostGenerator(api_key=st.secrets["GROQ_API_KEY"])
        result = generator.generate_blog(
            prompt=data["prompt"],
            words=data.get("words", 500),
            tone=data.get("tone"),
            seo_optimize=data.get("seo_optimize", True),
        )
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


def streamlit_app():
    st.set_page_config(page_title="BlogPostGenerator App📝", page_icon="🪶")

    st.markdown(
        "<h1 style='text-align:center;'>🪶 BlogPostGenerator.AI</h1>"
        "<p style='text-align:center;font-size:1.2em;'>Create SEO-optimized, engaging blog posts with GenAI ✨</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    with st.form("blog_form"):
        prompt = st.text_area("🧠 Blog Topic / Prompt", placeholder="E.g. The impact of AI on education in 2025")
        words = st.slider("Approx. Word Count", 200, 1500, 600)
        tone = st.text_input("🎭 Desired Tone (optional)", placeholder="E.g. professional, casual, educational")
        seo_optimize = st.checkbox("🔍 SEO Optimize", value=True)
        
        submitted = st.form_submit_button("✨ Generate Blog ✨")

    if submitted and prompt:
        with st.spinner("⏳ Generating your blog post..."):
            try:
                generator = BlogPostGenerator(api_key=st.secrets["GROQ_API_KEY"])
                result = generator.generate_blog(prompt, words, tone, seo_optimize)

                st.success("Blog post generated successfully!")

                st.markdown(f"### 🏷️ Title: {result['title']}")
                st.write(result["content"])
                if result.get("hashtags"):
                    st.markdown(f"**🏷️ Hashtags:** {result['hashtags']}")

                st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {e}")


if __name__ == "__main__":
    streamlit_app()
