import streamlit as st
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Website Maker",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --accent: #ec4899;
    }
    
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Custom container styling */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        margin: 1rem 0;
    }
    
    /* Header styling */
    .header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 1rem 0;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Success/Error messages */
    .stSuccess, .stError, .stInfo {
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Code block styling */
    .stCodeBlock {
        border-radius: 10px;
        background: #1e293b;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_sites' not in st.session_state:
    st.session_state.generated_sites = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    # API Selection
    api_provider = st.selectbox(
        "Select AI Provider",
        ["OpenAI", "Anthropic Claude", "Google Gemini", "Custom API"],
        help="Choose your preferred AI provider"
    )
    
    # API Key Input
    api_key = st.text_input(
        "API Key",
        type="password",
        value=st.session_state.api_key,
        help="Enter your API key securely"
    )
    st.session_state.api_key = api_key
    
    # Template Selection
    st.markdown("### 🎨 Template Style")
    template_style = st.selectbox(
        "Choose Template",
        ["Modern Minimal", "Corporate", "Creative Portfolio", "E-commerce", "Blog", "Landing Page"]
    )
    
    # Color Scheme
    st.markdown("### 🎨 Color Scheme")
    primary_color = st.color_picker("Primary Color", "#667eea")
    secondary_color = st.color_picker("Secondary Color", "#764ba2")
    
    # Advanced Options
    with st.expander("🔧 Advanced Options"):
        include_animations = st.checkbox("Include Animations", value=True)
        responsive_design = st.checkbox("Responsive Design", value=True)
        seo_optimized = st.checkbox("SEO Optimized", value=True)
        
    st.markdown("---")
    st.markdown("### 📊 Statistics")
    st.metric("Sites Generated", len(st.session_state.generated_sites))

# Main content
st.markdown("<h1 class='header'>🌐 AI Website Maker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem;'>Create stunning websites with the power of AI</p>", unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Generate", "📝 Customize", "🔍 Preview", "💾 Export"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Describe Your Website")
        
        website_description = st.text_area(
            "Website Description",
            placeholder="e.g., A modern portfolio website for a freelance photographer specializing in nature photography...",
            height=150,
            label_visibility="collapsed"
        )
        
        col1a, col1b = st.columns(2)
        with col1a:
            industry = st.selectbox("Industry", ["Technology", "Creative", "Business", "Education", "Healthcare", "Retail", "Other"])
        with col1b:
            pages_count = st.number_input("Number of Pages", min_value=1, max_value=10, value=3)
        
        features = st.multiselect(
            "Include Features",
            ["Contact Form", "Gallery", "Blog", "Newsletter", "Testimonials", "FAQ", "Shopping Cart", "Live Chat"]
        )
        
        if st.button("🎨 Generate Website", use_container_width=True):
            if not api_key:
                st.error("⚠️ Please enter your API key in the sidebar")
            elif not website_description:
                st.error("⚠️ Please provide a website description")
            else:
                with st.spinner("✨ AI is crafting your website..."):
                    # Simulate API call
                    import time
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)
                    
                    # Generate mock website data
                    website_data = {
                        "id": len(st.session_state.generated_sites) + 1,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "description": website_description,
                        "template": template_style,
                        "pages": pages_count,
                        "features": features,
                        "colors": {"primary": primary_color, "secondary": secondary_color}
                    }
                    st.session_state.generated_sites.append(website_data)
                    
                    st.success("✅ Website generated successfully!")
                    st.balloons()
    
    with col2:
        st.markdown("### 💡 Tips")
        st.info("""
        **Be Specific:**
        - Mention your brand identity
        - Describe target audience
        - List key features needed
        
        **Best Results:**
        - Include industry/niche
        - Specify tone (formal/casual)
        - Mention competitors for style reference
        """)

with tab2:
    st.markdown("### 🎨 Customize Your Website")
    
    if st.session_state.generated_sites:
        selected_site = st.selectbox(
            "Select Website to Customize",
            range(len(st.session_state.generated_sites)),
            format_func=lambda x: f"Website #{x+1} - {st.session_state.generated_sites[x]['timestamp']}"
        )
        
        site = st.session_state.generated_sites[selected_site]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Content Settings")
            site_title = st.text_input("Site Title", "My Awesome Website")
            tagline = st.text_input("Tagline", "Creating amazing experiences")
            
            st.markdown("#### Typography")
            font_family = st.selectbox("Font Family", ["Inter", "Roboto", "Playfair Display", "Montserrat", "Open Sans"])
            font_size = st.slider("Base Font Size", 14, 20, 16)
        
        with col2:
            st.markdown("#### Layout Settings")
            header_type = st.radio("Header Style", ["Fixed", "Transparent", "Minimal"])
            footer_style = st.radio("Footer Style", ["Simple", "Detailed", "Minimal"])
            
            st.markdown("#### Effects")
            parallax = st.checkbox("Parallax Scrolling")
            smooth_scroll = st.checkbox("Smooth Scrolling", value=True)
        
        if st.button("💾 Save Customizations", use_container_width=True):
            st.success("✅ Customizations saved!")
    else:
        st.info("👈 Generate a website first to customize it")

with tab3:
    st.markdown("### 🔍 Preview Your Website")
    
    if st.session_state.generated_sites:
        preview_mode = st.radio("Preview Mode", ["Desktop", "Tablet", "Mobile"], horizontal=True)
        
        # Mock preview
        st.markdown(f"""
        <div class="card">
            <h2 style="color: {primary_color};">Preview Mode: {preview_mode}</h2>
            <div style="background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 100%); 
                        height: 400px; border-radius: 10px; display: flex; 
                        align-items: center; justify-content: center; color: white; font-size: 1.5rem;">
                🎨 Website Preview Area<br>
                <small style="font-size: 1rem; opacity: 0.8;">Your generated website will appear here</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Load Time", "0.8s", "-0.2s")
        with col2:
            st.metric("Performance", "95/100", "+5")
        with col3:
            st.metric("Accessibility", "98/100", "+3")
    else:
        st.info("👈 Generate a website first to preview it")

with tab4:
    st.markdown("### 💾 Export Your Website")
    
    if st.session_state.generated_sites:
        export_format = st.radio(
            "Export Format",
            ["HTML/CSS/JS", "React", "Vue.js", "WordPress Theme", "Webflow"],
            horizontal=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Export Options")
            minify_code = st.checkbox("Minify Code", value=True)
            include_assets = st.checkbox("Include Assets", value=True)
            include_docs = st.checkbox("Include Documentation", value=True)
        
        with col2:
            st.markdown("#### Deployment")
            deploy_option = st.selectbox("Deploy To", ["Download Only", "Vercel", "Netlify", "GitHub Pages", "AWS S3"])
        
        if st.button("📦 Export Website", use_container_width=True, type="primary"):
            with st.spinner("📦 Preparing your export..."):
                import time
                time.sleep(2)
                
                # Mock export data
                mock_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Website</title>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 100%);
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Your AI-Generated Website</h1>
        <p>This is your beautiful website created with AI!</p>
    </div>
</body>
</html>
                """
                
                st.code(mock_code, language="html")
                st.success("✅ Website exported successfully!")
                st.download_button(
                    label="⬇️ Download Website Package",
                    data=mock_code,
                    file_name="website.html",
                    mime="text/html",
                    use_container_width=True
                )
    else:
        st.info("👈 Generate a website first to export it")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem 0;'>
    <p>Made with ❤️ using AI • Powered by Advanced Language Models</p>
    <p style='font-size: 0.9rem;'>© 2025 AI Website Maker. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)