import streamlit as st
from pytube import YouTube
import os

def download_video(youtube_url, download_path):
    try:
        yt = YouTube(youtube_url)
        st.write("Downloading video...")
        yt.streams.filter(progressive=True, file_extension='mp4').first().download(download_path)
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.title("YouTube Video Downloader")

    # Input field for entering YouTube URL
youtube_url = st.text_input("Enter YouTube Video URL:")

    # Button to trigger the downloa
if st.button("Download"):
        if not youtube_url:
            st.warning("Please enter a YouTube video URL.")
        else:
            download_path = os.path.join(os.getcwd(), "downloads")
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            download_video(youtube_url, download_path)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Heflin Stephen Raj S</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)