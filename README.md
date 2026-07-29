# 🚀 LinkedIn Post Generator

### *Turn a topic into a scroll-stopping LinkedIn post — in your voice, in seconds.*

An AI-powered content generation tool that learns from real LinkedIn posts and produces new ones matching a target writing style, tone, and length — powered by **Few-Shot Learning** and **LLaMA 3.1 70B** via Groq.

---

## 🎯 Why This Project Exists

Writing consistent, engaging LinkedIn content is time-consuming — and most AI writing tools produce generic, robotic output that sounds nothing like a real person. This project solves that by teaching the LLM **your own writing style** using real examples, instead of relying on a one-size-fits-all prompt.

**Objectives:**
- 🧠 Demonstrate practical **Generative AI application** beyond simple chatbot wrappers
- ✍️ Generate posts that sound human, on-brand, and topic-relevant
- ⚡ Automate the tedious parts of content creation (ideation, tagging, structuring) using LLMs
- 🔍 Show how **prompt engineering + data preprocessing** can outperform naive prompting

---

## 🧩 How It Works — The Pipeline
 
```
 📄 Raw Posts  ─▶  🤖 LLM Metadata      ─▶  🏷️ Tag Unification  ─▶  💾 Processed Data
(raw_posts.json)   (tags, language,          (merges similar          (processed_posts.json)
                     line count)               tags via LLM)
 
                                                                              │
                                                                              ▼
 
 📝 Final Post  ◀─  ⚡ LLM Generation   ◀─  🧠 Prompt Built     ◀─  🔎 Few-Shot Retrieval
                    (LLaMA 3.1 70B          (instructions +          (filtered by topic,
                     via Groq)               examples injected)       length, language)
```

**In plain English:**
1. Real LinkedIn posts are fed in as raw data.
2. An LLM automatically extracts metadata — how long each post is, what language it's in, and what topics it covers.
3. Similar tags (e.g. "Job Hunting" and "Jobseekers") get merged into clean, unified categories.
4. When a user picks a topic, length, and language, the app retrieves the most relevant *real* examples.
5. Those examples are injected into the prompt as **few-shot references**, guiding the LLM to match that exact style.
6. The LLM generates a brand-new, original post — not a copy, but stylistically aligned.

---

## ✨ Features

- 🎯 **Topic-based generation** — pick from auto-extracted, AI-unified tags
- 📏 **Length control** — Short, Medium, or Long posts
- 🌐 **Multilingual support** — English & Hinglish
- 🔄 **One-click regenerate** — don't like it? Instantly try again
- 📊 **Live post metrics** — word/character count with LinkedIn best-practice guidance
- 🧠 **Few-shot style matching** — grounded in real writing examples, not generic AI tone

---

## 🖥️ Live Demo

🔗 **[Try it here](https://linkedin-post-generator-zkja39ab2jykijg5qr4s9s.streamlit.app/)**

> ⚠️ Note: This app is hosted on Streamlit's free tier and may take 30-60 seconds to wake up if inactive.

<img width="577" height="301" alt="LinkedIn post gen snapshot" src="https://github.com/user-attachments/assets/83e78b34-a6bb-493a-9409-a1e20061c708" />

---

## 🧠 GenAI Concepts Applied

| Concept | Where It's Used |
|---|---|
| **Few-Shot Prompting** | Retrieved real posts are injected into the prompt as style references |
| **LLM-based Data Labeling** | Metadata (tags, language, line count) extracted automatically instead of manual labeling |
| **Prompt Engineering** | Structured prompt templates with explicit constraints (length, language, tone) |
| **Structured Output Parsing** | LLM responses parsed as strict JSON using `JsonOutputParser` |
| **Semantic Tag Normalization** | LLM merges inconsistent tags into a clean taxonomy |

---

## 💼 Real-World Use Cases

- **Content creators & founders** who want to post consistently without burning hours on ideation
- **Personal branding agencies** managing writing style across multiple clients
- **Marketing teams** needing on-brand social copy at scale
- **Job seekers** looking to build LinkedIn presence for job search visibility
- Extendable to **Twitter/X threads, newsletters, or blog intros** using the same few-shot architecture

---

## 🛠️ Tech Stack

- **LLM:** LLaMA 3.1 70B via **Groq API** (near-instant inference)
- **Orchestration:** LangChain
- **Frontend:** Streamlit
- **Data Handling:** Pandas
- **Language:** Python

---


## 📂 Project Structure

```
linkedin-post-generator/
├── data/
│   ├── raw_posts.json          # Original scraped/collected posts
│   └── processed_posts.json    # Posts enriched with AI-extracted metadata
├── few_shots.py                # Loads & filters posts for few-shot examples
├── llm_helper.py                # LLM client configuration
├── post_generator.py           # Prompt construction & generation logic
├── preprocess.py               # Metadata extraction & tag unification pipeline
├── main.py                     # Streamlit application entry point
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

- 🔍 Embedding-based semantic search for smarter example retrieval (beyond exact tag match)
- 🔁 Multi-LLM provider support (OpenAI, Anthropic, Groq — switchable)
- 📈 Engagement-aware suggestions based on historical post performance
- 🗂️ Multi-post variation generation (choose your favorite from 3 options)

---

## 📬 Connect

Built by **VIKASINI D** — feel free to reach out on [LinkedIn](https://www.linkedin.com/in/vikasini-d-287251259/) or check out more projects on [GitHub](https://github.com/brickstoviks008).

⭐ If you found this project interesting, consider giving it a star!
