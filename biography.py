import streamlit as st
from PIL import Image

st.set_page_config(page_title="Diana's Memoir", page_icon=":maple_leaf:", layout="wide")

    
col1, col2 = st.columns([2, 1]) 

with col1:
    st.subheader("Hi, welcome to the biography of")
    st.title("DIANA MAE RETULLA :feather:")
    st.write("I hope this biography will help you know this person more.")
with col2:
    st.image("https://scontent.xx.fbcdn.net/v/t1.15752-9/467482492_1633745790858088_8163750881149738218_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=105&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeEZQlgws7QjiQfTRWCkNwUtMDxunHPGdREwPG6cc8Z1EcNSTodFZJtandNUH5vHxFpi_FKLQcN_-nvwguFuRxxN&_nc_ohc=ebIVglRHkloQ7kNvgFRLh1f&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QF47qAAQ-lgWC9QQmUV-jo3Gd0DjbuU4oRm4ZaV5uIy7w&oe=676CABFC", width=300, caption='Profile picture')


with st.container(): 
    st.write("---")  
    left_column, right_column = st.columns(2) 
   
    with left_column: 
        st.title("ABOUT ME") 
        st.subheader("Personal Details")
        st.write("**Name:** Diana Mae Retulla")  
        st.write("**Birthdate:** March 27, 2006")
        st.write("**Age:** 18")
        st.write("**Course:** Batchelor of Science in Computer Engineering")  
        st.write("**Year:** 1st year college student")
        st.write("**Favorite Food:** Cake, Pizza, Cookies")
        st.write("**Favorite Place:** Natures, Oceans, and Silent places ")  

    with right_column: 
        st.write("###")  
        st.subheader("Family Background")  
        st.write("**Mother's Name:** Emelita c. Retulla")
        st.write("**Birthdate:** March 27, 1986")  
        st.write("**Siblings:** 3 younger brothers (Dave John, John Carl and Ismael Retulla)")  
        st.write("**Family Values:** Respect, Unity, and Hard Work")   
        st.write("##")
    
st.subheader("Educational Attainment")
elem = st.text_input("**Elementary**", "Bernado Vasquez Memorial Central Elementary School, Batch 2018")
hs = st.text_input("**High School**", "Rizal National High School, Batch 2024")
college = st.text_input("**College**", "Surigao del Norte State University")

if "seminars" not in st.session_state:
    st.session_state.seminars = [
        "Kabataan Karapatan Online Caravan (KKOC) of the Commission on Human Rights Caraga.",
        "Basic Life Support and First Aid Training",
        "RNHS Career Guidance Orientation",
    ]

st.subheader("Seminars Attended")
for index, seminar in enumerate(st.session_state.seminars):
    col1, col2 = st.columns([8, 2])
    with col1:
        st.write(f"{index + 1}. {seminar}") 
    with col2:
        if st.button("Remove", key=f"remove_{index}_{seminar[:10]}"):
            st.session_state.seminars.pop(index)
            break  

st.subheader("Add a New Seminar")
new_seminar = st.text_input("Enter a seminar you've attended")

if st.button("Add Seminar"):
    if new_seminar.strip():  
        st.session_state.seminars.append(new_seminar.strip())  
        st.success(f"Added new seminar: {new_seminar.strip()}")
    else:
        st.warning("Please enter a seminar or training before adding.")

if "default_pic" not in st.session_state:
    st.session_state.default_pic = [
        {"title": "Doing Arts", "image": "https://scontent.xx.fbcdn.net/v/t1.15752-9/462566453_8618383344877425_6559558237488665471_n.jpg?stp=dst-jpg_p480x480_tt6&_nc_cat=111&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeGk5uce0LrdyQjdlb-ZlpveKiWGINj8npcqJYYg2Pyel3hpdsvL-bVmLTQYswB2h56qJpM8gyim_xIQWbhLj2br&_nc_ohc=CmhT9thBgmYQ7kNvgE1eml3&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QHK8C_v-VBqIhr_lwb4h_56v8olV-KKsa-lGY2pDu1Yaw&oe=676CA07A"},
        {"title": "Playing Games", "image": "https://scontent.xx.fbcdn.net/v/t1.15752-9/467474003_8907552579338943_3733155093565920094_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=104&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeF3dLkf-JPRq6wY7H-tgD7Fo5F-_3kjwQKjkX7_eSPBAu5gRF6HqXpRRKogPQ9ihbUHuw6t7rgqrBc2Fd8fgmh0&_nc_ohc=bDlxxNZ4vH8Q7kNvgFiFUFv&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QE0qbuwGz1ADgYfpg9gtVwdQ2DAVNLDW_DdUqJjr8DCXQ&oe=676C7762"},
        {"title": "Capturing Moments", "image": "https://scontent.xx.fbcdn.net/v/t1.15752-9/467486094_493921153691985_5341773108228595754_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=101&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeFzb7dM3XaEmLTL9TXsjrFAtNlDFkyszaC02UMWTKzNoMPfuo0R7MjRKN9WZHkenby-JSYusWXuFWXBHub5hrZq&_nc_ohc=YLsY7fGJjc8Q7kNvgF3mBZ0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QGsSyDWaTFCTPLPZzJOqBXt_AnxRkrpvnATRP3NTVnGGQ&oe=676C7B06"},
        {"title": "Bonding with Friends", "image": "https://scontent.xx.fbcdn.net/v/t1.15752-9/467474465_942932167710128_2841787950443147172_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=107&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeFy2CHFq5DXp3jJvVZCMBIokGXRq5LU2a2QZdGrktTZrRjSS6WzD3bDdfMjZcrWJ2fNRVZDsN-boo4lk-mA-R5r&_nc_ohc=K_91N-wHF3kQ7kNvgHRueHc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QHHr1rmwWPWW6jNHNqPxTHZAVl_oPtqwJ9I3YOhi_Mi1A&oe=676C9320"},
    ] 

if "user_pic" not in st.session_state:
    st.session_state.user_pic = []  

st.subheader("What I love to do")
left_column, right_column = st.columns(2)
for i, achievement in enumerate(st.session_state.default_pic):
    column = left_column if i % 2 == 0 else right_column
    with column:
        st.image(achievement["image"], caption=achievement["title"], width=300)

st.subheader("Add a New 'What I Love to Do'")
new_title = st.text_input("Enter the title of the activity:")
new_image_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

if st.button("Add Activty"):
    if new_title.strip() and new_image_file:
        image = Image.open(new_image_file)
        st.session_state.user_pic.append({"title": new_title.strip(), "image": image})
        st.success(f"Added activity: {new_title}")
    else:
        st.warning("Please provide both a title and an image file.")

if st.session_state.user_pic:
    st.subheader("User-Added 'What I Love to Do'")
    left_column, right_column = st.columns(2)
    indices_to_remove = [] 

    for i, activity in enumerate(st.session_state.user_pic):
        column = left_column if i % 2 == 0 else right_column
        with column:
            st.image(activity["image"], caption=activity["title"], width=150)
            if st.button(f"Remove {activity['title']}", key=f"remove_{i}"):
                indices_to_remove.append(i)  

    for index in sorted(indices_to_remove, reverse=True):
        del st.session_state.user_pic[index]

else:
    st.write("No additional activities added yet.")
