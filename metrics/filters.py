from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from tests.models import Test, TestType
from locations.models import Province

class FilterField():
    def validate():
        pass

    def query():
        pass

class ProvinceFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class TestCenterFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class DrivingSchoolFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class SectionCodeFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class DateFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class TestTypeFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class PermissionFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class MetricFilterField(FilterField):
    def validate():
        pass

    def query():
        pass

class QueryFilter():
    def __init__(self, filters, query_params):
        self.query_params = query_params
        self.filters = filters

    def validate_params():
        for x in filters:
            x.validate()

    def make_query():
        for x in filters:
            x.query()

    def filter():
        if not self.validate_params(): Exception("Not validated")
        return self.make_query
