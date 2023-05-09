from pathlib import Path
from PIL import Image

import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mike Thompson"
PAGE_ICON = ":wave:"
NAME = "Mike Thompson"
DESCRIPTION = """
Data Engineering Manager
"""
EMAIL = "met600@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/michael-thompson-6a42532b/",
    "GitHub": "https://github.com/thethomp/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF, and Profile pic
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫", EMAIL)

# Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience
st.write("#")
st.subheader("Profile")
st.write("---")
st.write(
    """
    I am a software engineer with over 10 years of experience designing, building, and operating production data systems. I specialize in data system design and enjoy building efficient data platforms that bring diverse data sets together for engineers, scientists, analysts, and end users to derive valuable insights from. I thrive on working with cross-functional teams to understand their goals and finding creative data-powered solutions to their problems. I have extensive experience working with video game development teams throughout all phases of the game development lifecycle across disciplines from engineering to design to QA and more. I’m also a gamer! As such I find working in the games industry highly motivating, exciting, and inspiring.
    """
)

# Skills
st.write("\n")
st.subheader("Skills")
st.write("---")
st.markdown(
    """
    **Proficient Languages** 
    - Python, Java, SQL
    """
) 
st.markdown(
    """
    **Data Technologies** 
    - AWS Technologies (e.g. Kinesis, S3, Glue, Lamda), Google Cloud Technolgoies (e.g. PubSub, GCS, BigQuery), Spark, Kafka, Snowflake, DBT, Datadog, InfluxDB, Elasticsearch, Hadoop, Redis
    """
)

# Work History
st.write("\n")
st.subheader("Professional Experience")
st.write("---")

# PM xp
st.write("**Data Architect, Data Engineering Manager | ProbablyMonsters | June 2018 - Present**")
st.markdown(
    """
* Helped establish, lead, and eventually manage the Data Insights team for the company from the ground up, contributing to the vision and goals for the team as well as the engagement model for working with game studios.
* Designed a game agnostic, end to end cloud based data analytics system. This includes schema management, data ingestion, data lake storage, ETL processing layers, data warehousing, and more.
* Designed and built an internal distributed telemetry data system to handle all logs, metrics, crash information, and more from internal company systems, game clients, and servers as the company started to grow.
* Established the company's observability engineering discipline. Scaled the team to work efficiently while supporting multiple partner studios and internal teams.
"""
)

# Bungie xp 1
st.write("**Software Engineer, Product Owner | Bungie | April 2016 - May 2018**")
st.markdown(
    """
* Responsible for the long-term roadmap, planning, and prioritization of work for the Data Platforms Team, a cross-functional team of data engineers and platform administrators that work to provide Bungie with scalable, reliable, stable data platforms for development and production use. 
* Collaborate closely with engineering, production, and studio leadership teams to plan and prioritize work that will help empower developers and software services with stable data platforms to utilize.
* Manage production Hadoop, Elasticsearch, and Redis clusters. This includes duties such as performance tuning, high availability configurations, monitoring, operational tools development, and documentation and training to client teams that utilize the technologies.
* Design and prototype creative data solutions and pipelines for handling an ever changing set of use cases for a growing gaming franchise.
"""
)

# Bungie xp 2
st.write("**Destiny Operations Lead | Bungie | November 2013 - April 2016**")
st.markdown(
    """
* Leadership role on the Destiny Operations Center (DOC), a 24/7 team that monitors and supports all of the data center hardware and network infrastructure the Destiny games run on.
* Worked closely with services teams in the studio to develop processes, procedures, and tools for individual contributors of the DOC to use in order to ensure SLA compliance and a high quality of service for players of Destiny.
* Develop automation and monitoring for various parts of the big data pipeline, including tools that ingest content from major social media outlets such as Twitter and Reddit into ElasticSearch to allow for real time data analysis and visualization.
"""
)

# LawLogix xp
st.write("**Data Migration Software Engineer | LawLogix | May 2012 - August 2013**")
st.markdown(
    """
    * Worked directly with clients to understand requirements for transforming and migrating abstract data sources to the LawLogix Guardian platform (PostgreSQL backend).
    * Developed robust automation software using Python, Bash, and 4D to manage data migrations.
    * Led the development effort of integrating Oracle's Taleo with the LawLogix Guardian platform using SOAP web services.
    * Refactored and helped redesign the existing 4D data migration code base into a Django driven system that integrated with other LawLogix products.
    """
)

# Cognizant xp
st.write("**Software Developer | Cognizant Technology Solutions | Jan 2011 - May 2012**")
st.markdown(
    """
    * Fast paced, Agile development environment with a top international search engine company as main client.
    * Using Hadoop, MapReduce, Hive, Pentaho, and AWS, developed a new high traffic cloud infrastructure for handling large amounts of analytical business data, improving upon the reliability and efficiency of the previous infrastructure.
    * Developed robust monitoring system for said infrastructure using a highly customized Zenoss, including full failover support in case of region wide data center outages.
    """
)

# Uni xp
st.write("**Research Assistant | University of Arizona Computer Vision Lab | 2007 - 2010**")
st.markdown(
    """
    * Developed, implemented, and tested dynamic string matching algorithms used for matching presentation slide words with the output of automatic speech recognition systems.
    * Published results to ICPR in 2010: "Improving and aligning speech with presentation slides," International Conference on Pattern Recognition 2010 (ICPR), August, 2010.
    """
)