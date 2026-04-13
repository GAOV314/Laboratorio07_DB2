class UserRepository:
    def __init__ (self, driver):
        self.driver = driver
    def create_user(self, user_model):
        with self.driver.session() as session:
            query = """
            MERGE (u:USER {userId: $u_id})
            SET u.name = $u_name
            RETURN u
            """
            parameters = {
                "u_id": user_model.userId,
                "u_name": user_model.name
            }

            result = session.run(query, parameters)
            return result.single()
        def find_user_by_id(self, user_id):
            with self.driver.session() as session:
                query = "MATCH (u:USER {userId: $u_id}) RETURN u"
                result = session.run(query, u_id=user_id)
                record = result.single()
                return record["u"] if record else None

        pass
