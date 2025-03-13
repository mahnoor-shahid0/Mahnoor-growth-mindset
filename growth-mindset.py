import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🧠", layout="wide")
st.title("Growth Mindset Challenge")
st.header("Welcome to the Growth Mindset Journey! 🌱")
st.write("This is a simple web app that will help you develop a growth mindset. 🧠")

#Quote section
st.header("Quote of the Day")
quote = "Success is not final, failure is not fatal: It is the courage to continue that counts."
author = "Winston Churchill"
st.write(quote)
st.write(author)

st.header("Challenge of the Day")
user_input = st.text_area("What is your challenge for today?", "I will learn something new today.")
st.write(f"Your challenge for today is: {user_input}")

#condition
if user_input:
    st.success(f"You're facing : {user_input}. keep pishing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

    #Reflection section
    st.header("Reflection on your learning!")
    reflection = st.text_area("write your outcomes here!")
    if reflection:
        st.success(f"Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your learning outcomes here.")
        
        #Achievments section
        st.header("Celebrate your Achievements!")
        achievements = st.text_area("write your achievements here!")

        if achievements:
            st.success(f"✨Amazing! You Achieved⭐: {achievements}")
        else:
            st.info("Big or Small, every achievement counts! Share your achievements here ✌")

            #Footer
            st.write("...")
            st.write("Keep believing in yourself! You are Doing Absolutely Great! 🌟")
            st.write("""© created by Mahnoor Daniyal!""")

