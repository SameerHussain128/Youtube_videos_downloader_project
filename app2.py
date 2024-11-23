import streamlit as st
import yt_dlp

# Set up the page configuration
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add a header image or banner
st.image(
    "https://www.gstatic.com/youtube/img/branding/youtubelogo/svg/youtubelogo.svg", 
    use_column_width=True
)

# App title and description
st.title("🎥 YouTube Video Downloader")
st.markdown(
    """
    Welcome to the YouTube Video Downloader! 🚀  
    Enter a YouTube video URL below, and this app will download the video and display its details.  
    **No ads. No nonsense. Just download!** 😎
    """
)

# Input for YouTube video URL
link = st.text_input("🔗 Enter YouTube Video URL:")

# Action button to download and process video
if st.button("Download Video"):
    if link:
        st.info("Processing your request... Please wait!")
        try:
            # yt-dlp options
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)

                # Extracting video details
                title = info_dict.get('title', "N/A")
                views = info_dict.get('view_count', "N/A")
                duration = info_dict.get('duration', "N/A")
                description = info_dict.get('description', "N/A")
                thumbnail_url = info_dict.get('thumbnail', None)

                # Display results with enhanced UI
                st.success("🎉 Video downloaded successfully!")
                if thumbnail_url:
                    st.image(thumbnail_url, caption="Video Thumbnail", use_column_width=True)
                st.markdown(f"### **Title:** {title}")
                st.markdown(f"**Views:** {views:,}")
                st.markdown(f"**Duration:** {duration} seconds")
                st.markdown(f"**Description:**\n {description}")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL!")

# Footer
st.markdown("---")
st.markdown(
    """
    Made with ❤️ using [Streamlit](https://streamlit.io) and [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
    📧 For inquiries or suggestions, reach out at **mohdsameerhussain28@gmail.com**.                  
    Drop message on whatsapp **6303452296**
    """
)
