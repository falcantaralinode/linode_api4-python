from .base import Base, Property

class Kernel(Base):
    api_endpoint="/kernels/{id}"
    properties = {
        "created": Property(is_datetime=True),
        "deprecated": Property(),
        "description": Property(),
        "id": Property(identifier=True),
        "kvm": Property(),
        "label": Property(),
        "updates": Property(),
        "version": Property(),
        "x64": Property(),
        "xen": Property(),
    }

    def __init__(self, id):
        Base.__init__(self)

        self._set('id', id)

    def __repr__(self):
        return "Kernel {}".format(self.id)
