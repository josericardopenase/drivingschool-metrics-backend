from drivingschools.models import DrivingSchool

class BaseFilter:
    name = ""

    def validate(self, params):
        pass

    def query(self, params):
        pass

class ModelFilter(BaseFilter):
    def __init__(self, model, name, show_all = False, keyword="") -> None:
        self.name = name
        self.model = model
        self.show_all = show_all
        self.keyword = keyword

    def validate(self, params):
        return True
    
    def query(self, params):
        filt = {
            self.keyword : self.name
        }
        result = self.model.objects.filter(**filt)
        if self.show_all and len(result) == 0:
            return self.model.objects.all()
        return result


class QueryFilters:

    def __init__(self, filters : list[BaseFilter]):
        self.filters = filters

    def validate(self, params):
        for filter in self.filters:
            if params[filter.name] in params:
                if filter.validate(params) == False:
                    return False

    def query(self, params):
        response = {}

        for filter in self.filters:
            if params[filter.name] in params:
                response[filter.name] = filter.query(params)
        
        return response


    def filter(self, query_params):
        if self.validate(query_params):
            return self.query(query_params)
