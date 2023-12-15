import json

# ----ABOUT ME----
about_me = """
<p style='text-align: justify;'>Hey there! Welcome to my digital playground! I'm Hengki, originally from West Sumatra, Indonesia. Once into geology, I realized my passion lies in playing with data rather than deciphering ancient stones.</p>
<p style='text-align: justify;'>This website serves as my hub, dedicated to personal branding and documenting my learning journey.</p>
<p style='text-align: justify;'>Beyond bits and bytes, I'm an explorer in both the data realm and the physical world. When not coding, I'm out capturing moments in new places, camera in hand, lost in the beauty of unfamiliar landscapes.</p>
<p style='text-align: justify;'>Explore my portfolio to see the projects defining my coding journey. Whether you're a coding buddy, a talent scout in search of a data maestro, or just curious about my work, you're in for a treat. Join me in this web corner where I showcase my coding adventures.</p>
Cheers,
\nHengki
"""

lottie_skill_url = "https://lottie.host/0ef8164d-3e8f-4513-a293-2cd4229815b6/ylnlenwEmd.json" #v1
lottie_aboutme_url = "https://lottie.host/df307404-7a45-43c8-9d7f-5432ed179524/uFvnMstFZJ.json"
linkedin_url = 'https://www.linkedin.com/in/hengki-i-72082960/'
github_url = 'https://github.com/hengki-irawan/learning-and-projects.git'
tableau_url = "https://public.tableau.com/profile/hengki.irawan#!/"


# ----PORTFOLIO----
#read contents from json file & reformat
def create_project(title, desc, link):
    project_info = f"""
    ## {title}
    <p style="font-weight: bold;"><a href="{link}" target="_blank" rel="noopener noreferrer">Github</a></p>

    **Description:** {desc}
    """
    return project_info

with open("website-streamlit/projects_description.json", "r") as f:
    project_data = json.load(f)

portfolio_dict = {}
for project_name, project_info in project_data.items():
    name = project_info["name"]  
    description = project_info["description"]
    github_link = project_info["github_link"]

    portfolio_dict[project_name] = [create_project(name, description, github_link), project_info["video_path"]]

sphirogram_dots = portfolio_dict['sphirogram_dots']
python_etl_project = portfolio_dict['python_etl_project']
datawrangling_pyspark = portfolio_dict['datawrangling_pyspark']
marketing_nanodegreee = portfolio_dict['marketing_nanodegreee']
webpage = portfolio_dict['webpage']


portfolio = {
    "Sphirogram & Dots":sphirogram_dots,
    "Simple ETL Process": python_etl_project,
    "Data wrangling with pyspark":datawrangling_pyspark,
    "Marketing Analytics Nanodegree projects": marketing_nanodegreee,
    "Personal Webpage Deployment": webpage
    }

print(portfolio)
# ----Skills and Expertise
skills_n_expertise = ("Amazon Redshift", "Amazon S3", "Amazon Athena", "Matillion", "Google BigQuery",
                      "Serverless Lambda", "Python", "Google Analytics", "Terraform", "Github/Gitlab",
                      "Jenkins")


# ----Photo Gallery----
image_descriptions = {
    "images_1.JPG": "Hot air balloon in Cappadocia",
    "images_2.JPG": "Amsterdam's canal",
    "images_3.JPG": "Art Gallery in The Hague",
    "images_4.JPG": "Heydar Aliyev Center, Baku",
    "images_5.JPG": "Expo2020 Dubai with the Gang",
    "images_6.JPG": "Royal Alcázar of Seville",
    "images_7.JPG": "Gundam Glory in Riyadh",
    "images_8.JPG": "Amazing Porto",
    "images_9.JPG": "Sunset in Alexandria, Egypt",
    "images_10.JPG": "The Clock Towers, Makkah",
    "images_11.JPG": "Autumn in Delft",
    "images_12.JPG": "Kaindy Lake Serenity"
}

