import streamlit as st
import time
import subprocess

# Page config
st.set_page_config(page_title="SmartOps Dashboard", layout="wide")

# Title and subtitle
st.title("📊 SmartOps Dashboard")
st.subheader("Centralized control for your automation workflows.")

# Sidebar controls
st.sidebar.header("🔧 Automation Controls")
automation_enabled = st.sidebar.toggle("Enable Automation", value=True)

task = st.sidebar.selectbox("Select a Task", [
    "Run Daily Job",
    "Check System Logs",
    "Restart Automation Service",
    "Run Health Check"
])

# Main section
st.header("⚙️ Task Execution")

if automation_enabled:
    st.success("Automation is ENABLED.")
    if st.button(f"🚀 Execute '{task}'"):
        with st.spinner(f"Executing {task}..."):
            time.sleep(2)  # Simulate task duration
            if task == "Run Daily Job":
                st.code("python daily_job.py")  # Replace with subprocess if needed
                # subprocess.run(["python", "daily_job.py"])
                st.success("✅ Daily job completed.")
            elif task == "Check System Logs":
                st.text("Sample log output:")
                st.code("INFO: System check passed.\nINFO: Last run at 03:00 AM.")
            elif task == "Restart Automation Service":
                st.warning("Restarting service... (simulated)")
                st.success("🔁 Service restarted.")
            elif task == "Run Health Check":
                st.info("Health check OK ✅")
else:
    st.error("Automation is DISABLED. Toggle it on from the sidebar.")

# Logs section
st.write("---")
st.subheader("📄 Logs")
st.text_area("System Logs", height=200, value="INFO: SmartOps initialized...\nINFO: Awaiting task execution...")

