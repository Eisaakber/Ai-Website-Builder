# 🌐 AI Website Maker

<div align="center">

![AI Website Maker](https://img.shields.io/badge/AI-Website%20Maker-blueviolet?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Create stunning websites with the power of AI in minutes, not days.**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Integration](#-api-integration)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Integration](#-api-integration)
- [Configuration](#-configuration)
- [Export Formats](#-export-formats)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

AI Website Maker is a powerful Streamlit application that leverages advanced AI models to generate complete, customizable websites from simple text descriptions. Whether you're a developer, designer, or business owner, create professional websites in minutes without writing a single line of code.

### Why AI Website Maker?

- 🚀 **Fast Generation**: Create complete websites in seconds
- 🎨 **Beautiful Design**: Modern, responsive templates with smooth animations
- 🔧 **Fully Customizable**: Adjust colors, fonts, layouts, and more
- 🤖 **AI-Powered**: Integrates with OpenAI, Anthropic Claude, Google Gemini
- 📦 **Multiple Export Formats**: HTML, React, Vue.js, WordPress, and more
- 🎭 **Live Preview**: See changes in real-time across devices

## ✨ Features

### Core Functionality

- **🤖 AI Integration**
  - Support for OpenAI, Anthropic Claude, Google Gemini
  - Custom API endpoints
  - Intelligent content generation

- **🎨 Design Customization**
  - 6+ pre-built templates (Modern, Corporate, Creative, etc.)
  - Custom color schemes
  - Typography controls
  - Layout options (Fixed, Transparent, Minimal headers)

- **📱 Responsive Preview**
  - Desktop, Tablet, and Mobile views
  - Real-time performance metrics
  - Accessibility scoring

- **💾 Export Options**
  - HTML/CSS/JS
  - React Components
  - Vue.js
  - WordPress Themes
  - Webflow-compatible
  - Code minification
  - Asset bundling

- **⚡ Advanced Features**
  - Parallax scrolling effects
  - Smooth animations
  - SEO optimization
  - Contact forms, galleries, blogs
  - Shopping cart integration
  - Live chat widgets

## 🎬 Demo

```bash
# Quick start
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-website-maker.git
cd ai-website-maker
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

## 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
openai>=1.3.0
anthropic>=0.7.0
google-generativeai>=0.3.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## 🎮 Usage

### Basic Workflow

1. **Configure API**
   - Select your AI provider (OpenAI, Claude, Gemini)
   - Enter your API key securely
   - Choose template style

2. **Generate Website**
   - Describe your website in natural language
   - Select industry and features
   - Click "Generate Website"

3. **Customize**
   - Adjust colors, fonts, and layouts
   - Enable/disable animations and effects
   - Preview changes in real-time

4. **Export**
   - Choose export format
   - Configure deployment options
   - Download or deploy directly

### Example Prompt

```
A modern portfolio website for a freelance photographer specializing 
in nature photography. Include a gallery, about page, contact form, 
and blog. Use earthy tones with a minimalist design.
```

## 🔌 API Integration

### OpenAI Setup

```python
import openai

openai.api_key = "your-api-key-here"

# Example API call
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a website code generator"},
        {"role": "user", "content": website_description}
    ]
)
```

### Anthropic Claude Setup

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key-here")

# Example API call
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": website_description}
    ]
)
```

### Google Gemini Setup

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key-here")
model = genai.GenerativeModel('gemini-pro')

# Example API call
response = model.generate_content(website_description)
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
```

### Customization Options

Edit the configuration in the sidebar:

- **Template Styles**: Modern Minimal, Corporate, Creative Portfolio, E-commerce, Blog, Landing Page
- **Color Schemes**: Custom primary and secondary colors
- **Advanced Options**: Animations, responsive design, SEO optimization
- **Page Count**: 1-10 pages
- **Features**: Contact forms, galleries, blogs, testimonials, shopping carts

## 📤 Export Formats

### HTML/CSS/JS
Pure static website, ready to deploy anywhere

### React
Modern React components with hooks

### Vue.js
Vue 3 components with Composition API

### WordPress Theme
Complete WordPress theme structure

### Webflow
Webflow-compatible export

## 📸 Screenshots

### Main Dashboard
![Dashboard](screenshots/dashboard.png)

### Generation Interface
![Generate](screenshots/generate.png)

### Customization Panel
![Customize](screenshots/customize.png)

### Preview Mode
![Preview](screenshots/preview.png)

## 🗺️ Roadmap

- [ ] Add more AI model integrations (Cohere, Mistral)
- [ ] Database integration for saving projects
- [ ] Team collaboration features
- [ ] Version control for websites
- [ ] Built-in hosting platform
- [ ] A/B testing tools
- [ ] Analytics dashboard
- [ ] Mobile app version

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Keep commits atomic and well-described

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- AI powered by OpenAI, Anthropic, and Google
- Icons from [Lucide Icons](https://lucide.dev/)
- Inspired by modern web design trends

</div>
