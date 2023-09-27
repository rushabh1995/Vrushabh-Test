from cube import template
from cube_dbt import Dbt

context = template.JinjaContext()

dbt = (
  Dbt
  .from_file('model/manifest.json')
  .filter(paths=['dimensions', 'fact'])
)

@context.function
def dbt_models():
  return dbt.models

@context.function
def dbt_model(name):
  return dbt.model(name)