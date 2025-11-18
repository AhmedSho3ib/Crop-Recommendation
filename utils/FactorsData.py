from pydantic import BaseModel, Field
from typing import Literal

class FactorsData(BaseModel):
    N: float = Field(ge=0, description='Nitrogen')
    P: float = Field(ge=0, description='Phosphorus')
    K: float = Field(ge=0, description='Potassium')
    temperature:float = Field(ge=8, le=50, description='Temperature of the environment.')
    humidity: float = Field(le=100, description='Atmospheric moisture level')
    ph: float = Field(description='Soil acidity/alkalinity')
    rainfall: float = Field(description='Annual or seasonal rainfall')