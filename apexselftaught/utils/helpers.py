def setattr_helper(model_instance, **kwargs):
    for (key, value) in kwargs.items():
        if key is not None:
            setattr(model_instance, key, value)
