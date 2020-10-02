from app import db


class Movie(db.Model):
    '''
    TODO: create the database for the movies 
    '''
    __tablename__ = 'movie'

    id = db.Column(Integer, primary_key = True)
    title = db.Column(String)
    actors = db.relationship('Actor', backref='movies', lazy=True)

    def fomat(self):
        return({
            'id': self.id,
            'title': self.title,
            'actors': self.actors
        })



        '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()



class Actor(db.Model):

    __tablename__ = 'actor'

    id = db.Column(Integer, primary_key = True)
    name = db.Column(String)
    surname = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(String)
    movie_id = db.Column(Integer, ForeignKey('movie.id'))

    def fomat(self):
        return({
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id
        })



        '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()