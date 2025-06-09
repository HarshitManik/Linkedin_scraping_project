import streamlit as st
import pandas as pd
from datetime import datetime
import io
from linkedin_bot import run_linkedin_bot  # Ensure this is the debugged version from previous message

st.set_page_config(page_title="LinkedIn Auto Connector", layout="centered")
st.title("🤖 LinkedIn Auto-Connector Dashboard")

# --- Sidebar: Credentials and Basic Info ---
st.sidebar.header("🔐 LinkedIn Credentials")
email = st.sidebar.text_input("LinkedIn Email", type="default")
password = st.sidebar.text_input("LinkedIn Password", type="password")

st.sidebar.header("📌 Search Options")
default_keywords = [
    "Talent Acquisition Intern Google",
    "Campus Recruiter Infosys",
    "Student Ambassador Microsoft"
]
keyword = st.sidebar.text_input("Enter keyword", value=default_keywords[0])
location_filter = st.sidebar.text_input("Filter by location (e.g. India)", value="India")
university_filter = st.sidebar.text_input("University filter (e.g. Thapar University)", value="")

num_pages = st.sidebar.slider("Number of search result pages", min_value=1, max_value=10, value=3)
run_button = st.sidebar.button("🚀 Run Automation")

# --- Instructions ---
st.markdown("""
### 🔍 How It Works:
1. Enters your LinkedIn credentials securely (stored temporarily).
2. Searches people based on your keywords.
3. Filters based on country/university.
4. Sends automated connection requests with personalized messages.
""")

# --- Display Keyword Suggestions ---
st.markdown("### 🧠 Recommended Keywords:")
st.markdown("""
- `Talent Acquisition Intern Google`
- `Campus Recruiter Infosys`
- `Student Ambassador Microsoft`
- `Tech HR Amazon`
- `Startup Founder IIT`
""")

# --- Placeholder for Logs ---
log_area = st.empty()

# --- Run Bot and Display Results ---
if run_button:
    if not email or not password:
        st.error("Please enter both email and password!")
    else:
        log_area.info("🚧 Running automation... This can take a few minutes.")
        try:
            result_message = run_linkedin_bot(email, password, keyword, num_pages)
            logs_df = pd.read_excel("output.xlsx")

            st.success(result_message)
            st.dataframe(logs_df)

            # Prepare Excel download
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            excel_buffer = io.BytesIO()
            logs_df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)

            st.download_button(
                label="📅 Download Log as Excel",
                data=excel_buffer,
                file_name=f"linkedin_log_{now}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except FileNotFoundError:
            st.error("⚠️ No output file found. Please make sure the script ran correctly.")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")

# --- Footer ---
st.markdown("---")
st.caption("Built for student outreach and career growth 🚀")

