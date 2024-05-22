import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names  # Ensure the function returns the list

st.set_page_config(page_title="Movie Recommender System", page_icon=":clapper:", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        color: #333333;
    }
    .background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: radial-gradient(circle, rgba(63,94,251,1) 0%, rgba(252,70,107,1) 100%);
        overflow: hidden;
    }
    .background::before {
        content: '';
        position: absolute;
        top: -200px;
        left: -200px;
        width: 400%;
        height: 400%;
        background: rgba(255, 255, 255, 0.05);
        opacity: 0.8;
        animation: float 20s infinite;
        border-radius: 50%;
    }
    @keyframes float {
        0% {
            transform: translateY(0) rotate(0deg);
        }
        50% {
            transform: translateY(-20px) rotate(45deg);
        }
        100% {
            transform: translateY(0) rotate(0deg);
        }
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 1em;
    }
    .selectbox-label {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .selectbox {
        font-size: 1.2em;
        margin-bottom: 1.5em;
    }
    .recommendation-card {
        font-size: 1.2em;
        font-weight: bold;
        color: #ffffff;
        background: linear-gradient(145deg, #ff7a7a, #ff4b4b);
        box-shadow: 5px 5px 15px #1f1f1f, -5px -5px 15px #ff9f9f;
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        text-align: center;
        transition: transform 0.2s;
        cursor: pointer;
    }
    .recommendation-card:hover {
        transform: scale(1.05);
        background: linear-gradient(145deg, #ff4b4b, #ff7a7a);
    }
    .columns {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .footer {
        text-align: center;
        margin-top: 2em;
        font-size: 0.8em;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="background"></div>', unsafe_allow_html=True)
st.markdown('<div class="title">Movie Recommender System</div>', unsafe_allow_html=True)

# Load the movies and similarity matrices
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Get the list of movie titles
movie_list = movies['title'].values

# Create a selectbox for movie selection with a label
st.markdown('<div class="selectbox-label">Select a Movie</div>', unsafe_allow_html=True)
selected_movie = st.selectbox(
    "",
    movie_list,
    help="Select a movie to get recommendations.",
    key="movie_select",
    index=0
)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)  # Capture the return value

    # Check if recommendations were successfully generated
    if recommended_movie_names:
        st.markdown('<div class="columns">', unsafe_allow_html=True)
        for movie_name in recommended_movie_names:
            st.markdown(f'<div class="recommendation-card">{movie_name}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("No recommendations found. Please try a different movie.")

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
