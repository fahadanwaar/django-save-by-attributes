# djangosavebyattributes

djangosavebyattributes is a Python library for assisting models in saving attributes based on hash which is mapped on attributes of a model on Django ORM. The Project aims to save only attributes which are given as dict_hash. Only those attributes would be saved which are given in the hash.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install djangosavebyattributes
```
## Procedure
import library and pass into the model as a parameter in models.py
## models.py

```python
from django.db import models
from djangosavebyattributes import _CustomSaveByAttributes


class Car(models.Model, _CustomSaveByAttributes):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)


```
## Usage
```python
from sample.models import Car


def update_intance():
    c = Car.objects.get(id=1)
    s.save_by_hash(
      match_field_hash={"name": "Honda"}
    )

#output would be "Honda"
def get_car():
    c = Car.objects.get(id=1)
    print(c.name)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)