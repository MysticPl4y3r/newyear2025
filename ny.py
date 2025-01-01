import streamlit as st


quotes=st.empty()

with quotes.container():
    st.header("As curtain falls...")
    st.markdown('''As 2024 draws to a close, you wind up on any works that you have and begin to prepare for celebrations with your family and friends.
                You begin to recall fondly on various memories from 2024. From joy of many moments as well as suffering, you feel many emotions
                ranging from cringe at your mishaps to smiles to wonderful memories you have helped created with your friends and family. Can life really get
                better from this? Despite everything that is happening around the world, you situation isn't exactly any worse compared to the rest of world. 
                Hence you take a step back and think about whatever that has happened and contemplate on the optimistic future''')
    st.markdown('''Suddenly you receive a letter from an old friend from afar. As much as heartwarming it is to receive a letter from far away, 
                you find the contents of the letter to be odd. It isn't unlike any other letter that simply wishes you happy new year or any other wishes.
                Instead, there seems to be something that is hard, quite possibly a hardcover of sorts and what looks to be a device that is of mysterious nature.
                However, something beckons you to open it. Surely, it cannot be something that harms you or anything. After all, its your own friend that
                sent this letter. So now, you decide to....''')

if st.button("Open the Letter"):
    quotes.empty()
    st.image("ny2025.png")
    st.audio("newyear.mp3", format="audio/mpeg", loop=False, autoplay=True)