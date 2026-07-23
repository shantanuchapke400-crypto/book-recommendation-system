import os
import sys
import pickle
import streamlit as st
import numpy as np
from Books_recommendor.logger.log import logging
from Books_recommendor.config.configuration import AppConfiguration
from Books_recommendor.pipeline.training_pipeline import TrainingPipeline
from Books_recommendor.exception.exception_handler import AppException
# from Books_recommendor.entity.config_entity import ModelRecommendationConfig


class Recommendation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException (e, sys) from e
        

    def fetch_poster(self, suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []

            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, "rb"))
            final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_objects, "rb"))

            for book_id in suggestion[0]:
                book_name.append(book_pivot.index[book_id])

            for name in book_name:
                match = np.where(final_rating['title'] == name)[0]
                if len(match) > 0:
                    ids_index.append(match[0])

            for ids in ids_index:
                url = final_rating.iloc[ids]['image_url']
                poster_url.append(url)

            return poster_url

        except Exception as e:
            raise AppException(e, sys) from e
        

    def recommend_books(self,book_name):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1, -1), n_neighbors = 6)

            poster_url = self.fetch_poster(suggestion)

            for i in suggestion[0]:
                books_list.append(book_pivot.index[i])
            return books_list, poster_url

        except Exception as e:
            raise AppException(e, sys) from e 


    def train_pipeline(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training Completed✅")
            logging.info(f"Recommended successfully!")
        except Exception as e:
            raise AppException(e, sys) from e


    def recommendations_engine(self, selected_books):
        try:
            recommended_books, poster_url = self.recommend_books(selected_books)

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.text(recommended_books[1])
                st.image(poster_url[1])

            with col2:
                st.text(recommended_books[2])
                st.image(poster_url[2])

            with col3:
                st.text(recommended_books[3])
                st.image(poster_url[3])

            with col4:
                st.text(recommended_books[4])
                st.image(poster_url[4])

            with col5:
                st.text(recommended_books[5])
                st.image(poster_url[5])

        except Exception as e:
            raise AppException(e, sys) from e


if __name__ == "__main__":
    st.header("Books Recommendation System")
    st.text("This is a collaborative filtering based recommender system")

    obj = Recommendation()

    if st.button("Train Recommender System"):
        obj.train_pipeline()

    books_name = pickle.load(open(os.path.join("templates","book_names.pkl"), "rb"))

    selected_books = st.selectbox(
        "Type or select a book from the dropdown",
        books_name
    )

    if st.button("Show Recommendation"):
        obj.recommendations_engine(selected_books)        
                            

                    