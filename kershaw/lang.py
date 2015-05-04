from contextlib import contextmanager


@contextmanager
def ephemeral_value(obj, property_name, value):
    prev_property_value = object.__getattribute__(obj, property_name)
    object.__setattr__(obj, property_name, value)
    yield
    object.__setattr__(obj, property_name, prev_property_value)