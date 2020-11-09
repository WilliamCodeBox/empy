# empy

Fundamentals of Electromagnetic with Python

## Vector

## Coordinates

## Electrostatic

### Electrostatic Charge

## Testing

`empy` is tested by using the `pytest`[https://pypi.org/project/pytest/] package, and the test coverage is checked by using the `coverage`[https://pypi.org/project/coverage/] package.

A `.coveragerc` config file is created and located in the `empy` package root dir. This config file stores the sub commands `run` and `report` of `coverage`.

Run the following command to test coverage

```bash
coverage run -m pytest
```

Run the following command to show the test coverage report

```bash
coverage report
```
