from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import re
import os


class BlogPostGenerator:
    def __init__(self, api_key: str):
        """
        Initialize the Blog Post Generator using Groq LLM (Meta LLaMA model).
        """
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=api_key or os.getenv("GROQ_API_KEY"),
            max_tokens=2048,
            temperature=0.7,
        )

    def generate_blog(
        self,
        prompt: str,
        words: int = 500,
        tone: str = None,
        seo_optimize: bool = True,
    ) -> dict:
        """
        Generate a full blog post with title, summary, hashtags, and content.
        Output is plain text, ready to display.
        """

        # Auto-detect tone if not provided
        if not tone:
            tone_prompt = f"Determine the best tone (e.g., professional, casual, educational) for a blog post about: {prompt}"
            tone_result = self.llm.invoke(tone_prompt)
            tone = tone_result.content.strip()

        seo_text = (
            "Optimize for SEO with keyword-rich headings and natural readability."
            if seo_optimize else ""
        )

        main_prompt = f"""
        You are a professional blog writer.
        Write a detailed blog post about: "{prompt}"
        Tone: {tone}
        Length: approximately {words} words.
        {seo_text}

        Include:
        1. A catchy title on the first line.
        2. A short 2–3 line summary on the next line(s), prefixed with 'Summary:'.
        3. Full blog content after the summary.
        4. 5–8 relevant hashtags at the end, prefixed with 'Hashtags:' (comma or space separated).

        Output in plain text only.
        """

        response = self.llm.invoke(main_prompt)
        raw_output = response.content.strip()
        clean_output = self._clean_text(raw_output)

        # Extract title (first line)
        lines = clean_output.split("\n")
        title = lines[0].strip() if lines else "Untitled Blog Post"

        # Extract summary
        summary_match = re.search(r"Summary[:\-]?\s*(.*)", clean_output, re.IGNORECASE)
        summary = summary_match.group(1).strip() if summary_match else ""

        # Extract hashtags
        hashtags_match = re.search(r"Hashtags[:\-]?\s*(.*)", clean_output, re.IGNORECASE)
        if hashtags_match:
            hashtags_list = re.split(r"[,\s]+", hashtags_match.group(1).strip())
            hashtags_list = [f"#{tag.strip('#')}" for tag in hashtags_list if tag]
            hashtags = " ".join(hashtags_list)
        else:
            hashtags = ""

        # Extract content (everything except title, summary, hashtags)
        content_lines = []
        for line in lines[1:]:
            if line.lower().startswith("summary:") or line.lower().startswith("hashtags:"):
                continue
            content_lines.append(line)
        content = "\n\n".join(content_lines).strip()

        return {
            "title": title,
            "summary": summary,
            "content": content,
            "hashtags": hashtags,
        }

    def _clean_text(self, text: str) -> str:
        """
        Remove unwanted HTML or Markdown formatting.
        """
        text = re.sub(r"<br\s*/?>", "\n\n", text)
        text = re.sub(r"#+", "", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()
