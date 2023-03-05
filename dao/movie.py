from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, movies):
        return movies.all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movies = Movie(**data)
        self.session.add(movies)
        self.session.commit()

        return movies

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie


    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()