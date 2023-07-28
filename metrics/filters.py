from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from tests.models import Test, TestType, TestCenter
from locations.models import Province

class FilterField():
    def validate(self, query_params):
        pass

    def query(self):
        pass

class DateFilterField(FilterField):
    def validate(self, query_params):
        pass

    def query(self):
        pass

class DrivingSchoolFilterField(FilterField):
    def validate(self, query_params):
        autoescuelas = query_params.getlist('driving_school', '')
        if len(autoescuelas) > 0:
            autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas)
            self.sections = DrivingSchoolSection.objects.filter(driving_school__in=autoescuelas_obj) 
        else:
            self.sections = None

    def query(self):
        if self.sections:
            return {'school_section__in': self.sections}
        return {}

class MetricFilterField(FilterField):
    def validate(self, query_params):
        pass

    def query(self):
        pass

class PermissionFilterField(FilterField):
    def validate(self, query_params):
        self.values = query_params.getlist('permission_type')

    def query(self):
        if self.values:
            return {'permission_type__in': self.values}
        return {}

class ProvinceFilterField(FilterField):
    def validate(self, query_params):
        provinces = query_params.getlist('province', '')
        if len(provinces) > 0:
            provinces_obj = Province.objects.filter(id__in=provinces)
            self.test_center = TestCenter.objects.filter(province__in=provinces_obj) 
        else:
            self.test_center = None

    def query(self):
        if self.test_center:
            return {'test_center__in': self.test_center}
        return {}

class TestCenterFilterField(FilterField):
    def validate(self, query_params):
        self.values = query_params.getlist('test_center')

    def query(self):
        if self.values:
            return {'test_center__in': self.values}
        return {}

class TestTypeFilterField(FilterField):
    def validate(self, query_params):
        self.values = query_params.getlist('test_type')

    def query(self):
        if self.values:
            return {'test_type__in': self.values}
        return {}

class QueryFilter():
    def __init__(self, filters, query_params):
        self.query_params = query_params
        self.filters = filters

    def validate_params(self):
        for x in self.filters:
            x.validate(self.query_params)

    def make_query(self):
        query = {}
        for x in self.filters:
            query.update(x.query())
        return query

    def combine_filters(self):
        combined_filters = {}
        for x in self.filters:
            combined_filters.update(x.query())
        return combined_filters

    def filter(self):
        self.validate_params()
        return self.make_query()