from contextlib import contextmanager


@contextmanager
def ephemeral_value(obj, property_name, value):
    prev_property_value = getattr(obj, property_name)
    setattr(obj, property_name, value)
    yield
    setattr(obj, property_name, prev_property_value)