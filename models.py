from sqlalchemy import Column, Integer, String, Float

class HousingPricesTrain(Base):
    __tablename__ = 'housing_prices_train'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year_built = Column(Integer)
    neighborhood = Column(String(100))
    house_style = Column(String(50))
    overall_condition = Column(Integer)
    sale_price = Column(Float)  #  'Sale Price' is a float?

class HousingPricesTest(Base):
    __tablename__ = 'housing_prices_test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year_built = Column(Integer)
    neighborhood = Column(String(100))
    house_style = Column(String(50))
    overall_condition = Column(Integer)
    sale_price = Column(Float)  # Assuming 'Sale Price' is also in this table 

from sqlalchemy import func

def get_average_sale_price_by_year():
    result = session.query(
        HousingPricesTrain.year_built,
        func.avg(HousingPricesTrain.sale_price).label('average_sale_price')
    ).group_by(HousingPricesTrain.year_built)\
     .order_by(HousingPricesTrain.year_built)\
     .all()

    return result




