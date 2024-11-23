import streamlit as st
import yt_dlp

# Streamlit app title
st.title("YouTube Video Downloader")

# Input for YouTube video URL
link = st.text_input("Enter YouTube video URL:")

# Button to trigger the download process
if st.button("Download and Extract Info"):
    if link:
        st.write("Processing... Please wait.")
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

                # Display the extracted information
                st.success("Video downloaded successfully!")
                st.write(f"**Title:** {title}")
                st.write(f"**Views:** {views}")
                st.write(f"**Duration:** {duration} seconds")
                st.write(f"**Description:** {description}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")
