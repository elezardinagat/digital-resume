import streamlit as st # type: ignore

from forms.contact import contact_form # type: ignore

# Custom CSS to inject
custom_css = """
<style>
   button[data-baseweb="tab"] {
   font-size: 30px !important;
   margin: 0;
   width: 100%;
   }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

# Path to your PDF file
pdf_path = "assets/resume.pdf"

# Read the PDF file in binary mode
with open(pdf_path, "rb") as file:
    pdf_data = file.read()

with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Elezar D. Dinagat", anchor=False)
    st.write(
        "Full-Stack Software Developer, helps companies and individual entrepreneurs build their businesses in the world of technology."
    )

    left, right = st.columns(2, vertical_alignment="bottom")

    with left:
        if st.button("✉️ Contact Me", use_container_width=True):
            show_contact_form()
    with right:
        st.download_button(
            label="📑 Download CV",
            data=pdf_data,
            file_name="cv.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# Define skill rates
skills = {
    "PHP | C# | HTML | CSS": 90,
    "Python | JavaScript | React | Angular | Laravel": 80,
    "WordPress Development": 90,
    "Database Management": 80,
    "Project Management": 90,
    "Git | Adobe Creative Suit | Canva | Figma": 85,
    "Technical Support | Admin": 80
}

st.write("\n\n")
st.subheader("Skills rate")

# Display progress bars for each skill in columns
for skill, rate in skills.items():
    col1, col2, col3 = st.columns([5, 4, 1])
    with col1:
        st.write(f"**{skill}**")
    with col2:
        st.progress(rate)
    with col3:
        st.write(f"{rate}%")

st.write("\n\n")

tab1, tab2, tab3 = st.tabs(["About Me", "Profolio", "Work Experience"])

with tab1:
# --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n\n")
    st.subheader("Experience & Qualifications", anchor=False)
    st.write(
        """
        - Web Development: Developed responsive web interfaces using HTML, CSS, JavaScript, Laravel, and Angular. Managed server-side applications with Python or PHP and MySQL database management. Implemented data protection and user authentication best practices.
        - IT Management: Maintained and debugged school portals, managed system data, addressed stakeholder queries, and oversaw IT department operations. Prepared data backup, recovery processes, and IT policy implementation.
        - Team Leadership: Led development teams, coordinated project tasks, and ensured adherence to coding standards and project timelines.
        - IT Strategy and Infrastructure: Created and implemented IT strategies, policies, and procedures. Developed company websites, maintained IT infrastructure, and led technology projects.
        - Technical Support: Provided web development with WordPress, PHP, and Laravel. Offered graphics design services and resolved technical issues related to servers, CCTV, network cables, and personal computers.
        """
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Technical Skills", anchor=False)

    txt3('Programming Languages', '`PHP`, `Python`, `JavaScript`, `C#`')
    txt3('Web Development', '`WordPress`, `HMTL`, `CSS`, `Bootstrap`, `Laravel`, `React`, `Angular`')
    txt3('Database Management', '`MySQL`, `MS SQL`, `MS Access`')
    txt3('Graphics Design', '`Adobe Creative Suite`, `Canva`, `Figma`')
    txt3('Technical Support', '`System security`, `data backup`, `recovery processes`')
    txt3('Big Data Analysis Tools', '`Python Programming Language`, `Excel Advanced`, `SQL & MySQL`')

    # --- CORE COMPETENCIES ---
    st.write("\n")
    st.subheader("Core Competencies", anchor=False)
    st.write(
        """
        - Software and Web Development
        - Leadership and Team Management
        - Project Management
        - Strategic IT Planning
        - Technical Support and Troubleshooting
        """
    )

    # --- EDUCATION BACKGROUND ---
    st.write("\n")
    st.subheader("Educational Background", anchor=False)
    st.write(
        """
        - B.S. in Information Technology, Holy Cross of Davao College (2011 - 2015)
        - B.S. in Business Administration, Financial Accounting, Holy Cross of Davao College (2007 - 2010)
        """
    )

with tab2:
    #####################
    # Custom function for printing text
    def txt4(a, b, c):
        col1, col2, col3 = st.columns([1.5,2.5,2])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

    st.markdown('''
    ## Portfolio
    ''')

    st.markdown('''
        Welcome to my portfolio! Here, you'll find a showcase of my work spanning over 8 years in the technology sector. From developing responsive web interfaces and managing server-side applications to creating comprehensive IT strategies and providing technical support, my experience covers a wide range of skills and industries. Each project highlights my commitment to quality, innovation, and helping businesses thrive in the digital world. Explore my portfolio to see how I can bring your vision to life and drive your business forward with cutting-edge technology solutions.
    ''')
    st.write("\n\n\n")
    txt4('ALLY HEALTH CARE', 'is a platform focused on providing comprehensive healthcare solutions, including access to medical professionals, health management tools, and patient support services. It aims to enhance healthcare delivery by offering a range of services such as telemedicine, patient records management, and personalized health care plans.','https://allyhealthcare.net/')
    txt4('UPHIRES', 'is a platform designed for hiring freelancers, particularly in the Philippines. It connects businesses with talented professionals across various fields, including programming, design, marketing, and more. The platform focuses on providing quality freelance services with a seamless hiring experience for companies looking to outsource work or find specialized skills.', 'https://uphires.ph')
    txt4('UIPS', 'it is an integrated school system designed to manage administrative tasks and dashboards. Some of the portals are actively maintained and updated.', 'https://uips.online/iss')
    txt4('THE FITTEST YOU TRAINING', 'a website focused on fitness and personal training services. It offers various programs and services to help individuals achieve their fitness goals, including personalized training plans, group fitness classes, and nutrition advice. The platform likely includes features for scheduling sessions, tracking progress, and accessing resources related to fitness and wellness.', 'https://thefittestyoutraining.ca/')
    txt4('TAVERNASCALINETTO', 'a website related to a restaurant or dining establishment. It likely provides information about the restaurant menu, services, location, and possibly the option to make reservations or order food. The site may also feature details about the restaurant’s ambiance, special events, and contact information.','https://tavernascalinetto.it/')
    txt4('TRILOGY TREE', 'a website related to a company or organization focused on providing specialized services or products. Based on the URL, it might be involved in areas like consulting, business solutions, or another niche market. The site would typically include information about their services, team, contact details, and potentially client testimonials or case studies.', 'https://trilogytree.ca/')
    txt4('XPERT CHIMNEY SWEEP', 'a website dedicated to chimney cleaning and maintenance services. It likely offers information about their services, such as chimney inspections, cleaning, repairs, and possibly installations. The site might also include details about the company expertise, customer testimonials, and contact information for scheduling services.', 'https://xpertchimneysweep.com/')

with tab3:
    #####################
    # Custom function for printing text
    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    st.markdown('''
    ## Work Experience
    ''')

    txt('**Computer Programmer | LMS Coordinator | IT Offier**, IT Department, United International Private School LLC, Dubai',
    'January, 2024 - July, 2024')
    st.markdown('''
    - `Computer Programmmer` 
        - Maintain and debug school portals, including parent, payment, reservation, student portal, and school website.
    - `LMS Coordinator` 
        - Manage the Edu-nation system data, including report cards, teacher class schedules, announcements, etc.
        - Address queries and concerns from parents, students, teachers, school staff, and management.
    - `IT Officer` 
        - Oversee the overall work of the IT Department (Graphics Design and Networking troubleshooting).
        - Prepare announcements through SMS and Edu-nation system.
        - Prepare for the upcoming school year, including enrollment, fees, and other related tasks.
        - Ensure data backup and recovery processes are in place and functioning correctly.
        - Respond to parents' concerns and develop and implement IT policies and procedures.
    ''')
    st.write("\n")
    txt('**Full Stack Developer**, Freelance Developer, USA - CANADA - ITALY',
    'March 2022 - June 2023')
    st.markdown('''
    - `Web Development` 
        - Create and maintain responsive web interfaces using WordPress, HTML, CSS, JavaScript, Jquery and frameworks like Laravel or Angular.
    - `Backend Development` 
        - Develop and manage server-side applications with Python or PHP, and handle database management(MySQL).
    - `Security` 
        - Implement best practices for data protection and user authentication.
    - `Project Management` 
        - Assist in managing the development process from start to finish, including gathering requirements, designing, coding, testing, and deploying applications.
    - `Integration` 
        - Work with APIs and integrate with other software systems to ensure seamless functionality.
    ''')

    st.write("\n")
    txt('**IT Manager | Web Developer**, KHOHK WE MESHMESH & BURGER LAND, Kuwait',
    'July 2018 - February 2020')
    st.markdown('''
    - Develop and implement IT strategies, policies, and procedures to support organizational objective and created a company website.
    - Collaborate with other departments to understand their technology needs and ensure IT solutions align with business requirements.
    - Evaluate and recommend new technologies and solutions to improve business processes and efficiency.
    - Ensure the security and integrity of the organization's data, networks, systems, and information.
    - Monitor and maintain IT infrastructure, including servers, networks, hardware, and software.
    - Maintain compliance with relevant regulations and standards in technology and data management.
    - Plan, oversee, and execute technology projects, ensuring they are delivered on time and within budget.
    - Provide technical leadership and guidance to resolve complex technical issues.
    ''')

    st.write("\n")
    txt('**FULLSTACK DEVELOPER | TECHNICAL SUPPORT**, InfoSoft Studio, Davao City, Mindanao, Philippines',
    'January 2016 - February 2018')
    st.markdown('''
    - `Software Development` 
        - We provide a website using WordPress Development or Web/Form Based Application using PHP and Laravel framework with HTML, CSS, JavaScript, C#.
    - `Graphics Design` 
        - We cater logos, calling card, menus, brochures, banners, and many more.
    - `Technical Support` 
        - We do some troubleshooting issues such as server, cctv, network cable, personal computer, and website performance.
    ''')

    st.write("\n")
    txt('**TEAM LEAD PROGRAMMER | GRAPHICS DESIGNER**, MINDANAO AUTHORITY DEVELOPMENT - MINDA, Davao City, Mindanao, Philippines',
    'JSeptember 2015 - March 2016')
    st.markdown('''
    - Lead a team of developers, providing technical guidance, mentoring, and performance management.
    - Collaborate with project managers to define project scope, objectives, and timelines.
    - Coordinate with cross-functional teams to gather requirements, analyze user needs, and translate them into technical specifications.
    - Delegate tasks and allocate resources effectively within the development team.
    - Monitor and manage the software development life cycle, ensuring adherence to coding standards, version control, and documentation.
    ''')
