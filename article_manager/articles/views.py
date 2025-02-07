from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from google import genai
from django.conf import settings
from .models import Article

# Configure Google Gemini API
client = genai.Client(api_key=settings.GOOGLE_GEMINI_API_KEY)



# Create your views here.

class ArticleListCreateView(generics.ListCreateAPIView):
    """ • List Articles:
        GET /api/articles/
        Returns a list of all articles.

        • Create Article:
        POST /api/articles/
        Accepts JSON payload to create a new article. 
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ • Retrieve Article:
        GET /api/articles/<id>/
        Returns the details of a single article.

        • Update Article:
        PUT/PATCH /api/articles/<id>/
        Updates an existing article.

        • Delete Article:
        DELETE /api/articles/<id>/
        Deletes an article. 
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleSummaryView(APIView):
    """ 
        • Generate Summary:
        GET /api/articles/<id>/summary/

        This endpoint should:
        • Retrieve the article by its ID.
        • Use LLM to generate a summary of the article content.
        • Return the summary in JSON format. 
    """
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            content = article.content
            response = client.models.generate_content(model="gemini-2.0-flash", contents = f"Summarize this article: {content}")
            summary = response.text if response else "Summary could not be generated."

            return Response({"summary": summary})
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=404)
        
