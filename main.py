import time
from models.user import User
from models.movie import Movie
from models.rating import Rating
from config.database import driver
from repository.movie_repository import MovieRepository
from repository.rating_repository import RatingRepository
from repository.user_repository import UserRepository

import time

def main():
    user_repo = UserRepository(driver)
    movie_repo = MovieRepository(driver)
    rating_repo = RatingRepository(driver)

    status = True
    menu = """
    \n          MENU - LAB 07
    --------------------------------
    1. Crear un nodo usuario
    2. Crear un nodo movie
    3. Crear una relación RATED
    4. BUSCAR: Usuario por ID
    5. BUSCAR: Película por ID
    6. BUSCAR: Relación (Usuario -> Película)
    7. Salir del programa
    """

    while status:
        print(menu)
        option = input("Seleccione la opción que desee: ")

        if option == "1":
            username = input("Ingrese el nombre del usuario: ")
            user_id = input("Ingrese el id del usuario: ")
            nuevo_usuario = User(user_id, username)
            user_repo.create_user(nuevo_usuario)
            print(f"Usuario {username} creado.")

        elif option == "2":
            movie_id = int(input("Ingrese el id de la película (int): "))
            title = input("Ingrese el título: ")
            year = int(input("Ingrese el año (int): "))
            plot = input("Ingrese el plot: ")
            nueva_peli = Movie(movie_id, title, year, plot)
            movie_repo.create_movie(nueva_peli)
            print(f"Película {title} creada.")

        elif option == "3":
            u_id = input("ID del usuario: ")
            m_id = int(input("ID de la película: "))
            val_rating = int(input("Rating (0-5): "))
            ts = int(time.time())
            nuevo_rating = Rating(u_id, m_id, val_rating, ts)
            rating_repo.create_rating(nuevo_rating)
            print("Relación creada exitosamente.")

        # --- INCISO 3: FUNCIONES DE BÚSQUEDA ---
        elif option == "4":
            u_id = input("Ingrese el ID del usuario a buscar: ")
            user = user_repo.find_user_by_id(u_id)
            if user:
                print(f"\n[ENCONTRADO] Nombre: {user['name']}, ID: {user['userId']}")
            else:
                print("\nUsuario no encontrado.")

        elif option == "5":
            m_id = int(input("Ingrese el ID de la película a buscar: "))
            movie = movie_repo.find_movie_by_id(m_id)
            if movie:
                print(f"\n[ENCONTRADO] Título: {movie['title']}, Año: {movie['year']}")
            else:
                print("\nPelícula no encontrada.")

        elif option == "6":
            u_id = input("ID del usuario: ")
            m_id = int(input("ID de la película: "))
            rel = rating_repo.find_rating(u_id, m_id)
            if rel:
                print(f"\n[RELACIÓN] El usuario '{rel['user']}' calificó '{rel['movie']}' con {rel['rating']} estrellas.")
            else:
                print("\nNo existe una relación entre ese usuario y esa película.")

        elif option == "7":
            print("Cerrando conexión...")
            driver.close()
            status = False

if __name__ == "__main__":
    main()