from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import FormulaSerializer
from .models import History

class CheckFormula(APIView):
    
    def validate_formula(self, string):
        stack = []
        letters = {'(': ')', '[': ']', '{': '}'}
        
        for char in string:
            if char in letters.keys():
                stack.append(char)

            elif char in letters.values():
                if not stack or letters[stack[-1]] != char:
                    return False
                stack.pop()
                
        if stack:
            return False
        
        return True
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    
    @swagger_auto_schema(request_body=FormulaSerializer)
    def post(self, request, *args, **kwargs):
        formula = request.data.get("string", "")
        result = self.validate_formula(formula)
        ip = self.get_client_ip(request)

        History.objects.create(data=formula, ip=ip, result=result)

        return Response({"result": result}, status=status.HTTP_200_OK)
