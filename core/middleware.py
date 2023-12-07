
class AdminCORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = ["https://mfmadmin-izldar4i.b4a.run", "https://camfront.vercel.app"]
        return response
