class RatingRepository:
    def __init__(self, driver):
        self.driver = driver

    # Quitamos user_model y movie_model de los parámetros
    def create_rating(self, rating_model):
        with self.driver.session() as session:
            query = """
            MATCH (u:USER {userId: $u_id})
            MATCH (m:MOVIE {movieId: $m_id})
            MERGE (u)-[r:RATED]->(m)
            SET r.rating = $rating_val, 
                r.timestamp = $time_val
            RETURN u, r, m
            """

            parameters = {
                "u_id": rating_model.user_id,
                "m_id": rating_model.movie_id,
                "rating_val": rating_model.rating,
                "time_val": rating_model.timestamp
            }
        
            result = session.run(query, parameters)
            return result.single()
        
    def find_rating(self, user_id, movie_id):
            with self.driver.session() as session:
                query = """
                MATCH (u:USER {userId: $u_id})-[r:RATED]->(m:MOVIE {movieId: $m_id})
                RETURN u.name AS user, m.title AS movie, r.rating AS rating
                """
                result = session.run(query, u_id=user_id, m_id=movie_id)
                return result.single() 
    def update_rating(self, user_id, movie_id, new_rating):
            with self.driver.session() as session:
                query = """
                MATCH (u:USER {userId: $u_id})-[r:RATED]->(m:MOVIE {movieId: $m_id})
                SET r.rating = $new_val
                RETURN r
                """
                result = session.run(query, u_id=user_id, m_id=movie_id, new_val=new_rating)
                return result.single()