from dataclasses import dataclass

from dateutil.parser import parse


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    birthdate = parse(actor.born)
    moviedate = parse(movie.release_date)
    age = (moviedate - birthdate)
    age_years = int((age.total_seconds() // (60*60*24*365)))
    return f'{actor.name} was {age_years} years old when {movie.title} came out.'