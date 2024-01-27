import pandas as pd

# ----ABOUT ME----
about = """
<p style='text-align: justify;'>Hello and welcome to my digital hideout! I'm Hengki, a West Sumatra native now navigating the exciting realms of the digital world. Once enchanted by the wonders of geology, I discovered my true love lies in toying with data rather than decoding ancient stones.</p>
<p style='text-align: justify;'>After bidding farewell to Instagram, I decided to carve out a space dedicated to capturing the sheer beauty of the world. This website is all about documenting and seizing moments in new places, camera in hand, getting happily lost in the beauty of unfamiliar landscapes.</p>
<p style='text-align: justify;'>Join me in exploring the beauty of our incredible Earth!</p>
Cheers,
\nHengki
"""

lottie_aboutme_url = "https://lottie.host/6601a619-033c-49f3-9802-4a1af65013f6/cGpNewt0eH.json"
linkedin_url = 'https://www.linkedin.com/in/hengki-i-72082960/'

# ----Photo Gallery----
image_logs = pd.read_csv("image_logs.csv")
images= {}
for index in range(len(image_logs)):
    image_path = image_logs.loc[index, 'image_path']
    description = image_logs.loc[index, 'descriptions']
    images[image_path] = description
print(images)
