from ninja import NinjaAPI


api=NinjaAPI()


@api.get('/')
def basic(request):
    return {'result':'Hello World'}
