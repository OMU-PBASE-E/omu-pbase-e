from django.views.generic import TemplateView

# 施設一覧を表示するためのクラス
class FacilityListClass(TemplateView):
    template_name = "facility_list.html"

# 森ノ宮キャンパスを表示するためのクラス
class MorinomiyaClass(TemplateView):
    template_name = "morinomiya.html"

# 工学新棟を表示するためのクラス
class EngineeringClass(TemplateView):
    template_name = "engineering.html"

# 理学新棟を表示するためのクラス
class ScienceClass(TemplateView):
    template_name = "science.html"