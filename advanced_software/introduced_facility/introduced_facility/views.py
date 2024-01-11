from django.views.generic import TemplateView

# 施設一覧を表示するためのクラス
class FacilityListClass(TemplateView):
    template_name = "facility_list.html"

# 施設1を表示するためのクラス
class Facility1Class(TemplateView):
    template_name = "facility_1.html"

# 施設2を表示するためのクラス
class Facility2Class(TemplateView):
    template_name = "facility_2.html"