from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from chromdriver.db import engine


Base = automap_base()
Base.prepare(engine, reflect=True)

Automobile = Base.classes.Automobiles
Order = Base.classes.Orders
