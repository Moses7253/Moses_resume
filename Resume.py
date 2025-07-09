import streamlit as st

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Moses N - Full Stack Resume", layout="wide")

# ----- HEADER -----
st.title("💼 Moses N")
st.markdown("""
📍 Bangalore | 📧 [mosesn8919@gmail.com](mailto:mosesn8919@gmail.com) | 📞 +91 7760738603  
""")

# ----- PROFESSIONAL OBJECTIVE -----
st.header("🎯 Professional Objective")
st.write("""
Dedicated and highly skilled Full Stack Engineer with over 2.6+ years of experience in both frontend and backend development.
Proven ability to deliver high-quality, scalable software solutions and collaborate effectively with cross-functional teams.
Experienced in technologies such as Angular, React, and NodeJS. Passionate about driving innovation and consistently exceeding
client expectations. Seeking a challenging role to leverage my technical expertise, leadership skills, and dedication to delivering
exceptional value to both clients and stakeholders.
""")

# ----- PROFESSIONAL SUMMARY -----
st.header("🧾 Professional Summary")
st.markdown("""
- 2.6+ years of experience in Application Development with a strong focus on Frontend technologies and full stack development.  
- Expertise in React JS, Angular 11, TypeScript, JavaScript, HTML, CSS, REST APIs, and Microservices architecture.  
- Hands-on experience in scalable Frontend–Backend solutions with Microservices Architecture.  
- Backend service development using Node.js and integration with RESTful APIs.  
- Proficient in MySQL and version control systems like Git.  
- Familiar with Agile, unit testing (Jest), quick learner with strong communication skills.
""")

# ----- SKILLS -----
st.header("🛠 Skills")
st.markdown("""
- **Frontend Development:** React JS, Angular 11, TypeScript, JavaScript, HTML5, CSS3  
- **Backend & APIs:** Node.js, Express.js, RESTful APIs, Microservices Architecture  
- **Databases:** MySQL  
- **Version Control & Tools:** Git, Bitbucket, Postman  
- **Cloud Platforms:** AWS (S3), PCF, Config Server  
- **Testing:** Jest (unit testing), Postman (API testing)  
- **Other:** Scalable app design & deployment best practices
""")

# ----- EXPERIENCE -----
st.header("💼 Experience")
st.subheader("Software Engineer – Graylinx Pvt Ltd")
st.caption("Jan 2023 – Present")
st.markdown("""
- Worked as a Full Stack Developer on enterprise-level BMS and Energy Analytics platforms.  
- Developed scalable APIs and UI for HVAC systems like AHU, LMS, Chillers.  
- Participated in CI/CD workflows using Jenkins and Agile methodologies.
""")

# ----- EDUCATION -----
st.header("🎓 Education")
st.markdown("""
**Master of Computer Applications (MCA)**  
_TJOHN College, Bangalore University – 2021 to 2023_
""")

# ----- PROJECTS -----
st.header("🚀 Projects")

st.subheader("Project 1: BMS (Building Management System) Solution")
st.caption("Clients: Infor, Intel, Qualcomm, Mindtree, Honeywell, Kauvery")
st.markdown("""
- **Environment:** Node.js, React JS, MySQL, TypeScript, HTML, CSS  
- **Tools:** Git, Postman, VS Code, Jest, Jenkins  
- Developed intuitive UI for AHU, Chiller, LMS using React JS.  
- Built control logic in Node.js and used MySQL for data storage.  
- Integrated REST APIs to control sensors/equipment.  
- Wrote unit tests using Jest and deployed via Jenkins.
""")

st.subheader("Project 2: Energy Analytics Platform")
st.caption("Client: ServiceNow")
st.markdown("""
- **Environment:** Node.js, React JS, Material UI, MySQL, Cron Jobs  
- **Tools:** Git, Postman, VS Code  
- Designed dashboards, VAV controls, scheduling modules using React + MUI.  
- Created backend logic in Node.js with cron-based automation.  
- Implemented real-time energy data visualization and analytics.  
- Integrated with building systems and external sources.
""")

# ----- FOOTER -----
st.markdown("---")
st.caption("✅ Built with Streamlit | 🔧 Last updated July 2025")
