from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .chatbot import ask_gemeni

class ChatbotAPIView(APIView):
    def post(self, request):
        question=request.data.get("question")
        if not question:
            return Response({'error':'The question has not been send'}, status=status.HTTP_400_BAD_REQUEST)
        
        answer = ask_gemeni(question)
        return Response({"answer": answer})
