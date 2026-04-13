class MovieRepository:
    def __init__ (self, driver):
        self.driver = driver
    def create_movie(self, movie_model):
        with self.driver.session() as session:
            query = """
            MERGE (m:MOVIE {movieId: $m_id})
            SET m.title = $m_title
            SET m.year = $m_year
            SET m.plot = $m_plot
            RETURN m
            """

            parameters = {
                "m_id": movie_model.movieId,
                "m_title": movie_model.title,
                "m_year": movie_model.year,
                "m_plot": movie_model.plot
            }

            result = session.run(query, parameters)
            return result.single()
        def find_movie_by_id(self, movie_id):
            with self.driver.session() as session:
                query = "MATCH (m:MOVIE {movieId: $m_id}) RETURN m"
                result = session.run(query, m_id=movie_id)
                record = result.single()
                return record["m"] if record else None
        pass
