from fastapi import APIRouter, HTTPException
from models.article_models import ArticleThumbnail,ArticleDetail

public_router = APIRouter()

ARTICLE_THUMBNAILS: list[ArticleThumbnail] = [
    ArticleThumbnail(
        title="Sleep",
        description="It's over rated",
        slug="Sleep",
        link="article/Sleep"
    ),
        ArticleThumbnail(
        title="Nurtition",
        description="Yum Yum",
        slug="nutrition",
        link="article/nutrition"
    )
]

ARTICLE_DETAILS: dict[str, ArticleDetail] = {
    "Sleep": ArticleDetail(
    title="Sleep",
    content_html="""
        <h1>Sleep: And why it's over rated</h1>
        <p>Programming > Sleep</p>
    """
),
"nutrition": ArticleDetail(
    title="Nutrition",
    content_html="""
        <h1>Nutrition</h1>
        <p>The major food groups: Wendys, MCkies, Wingstop</p>
    """
)
}

@public_router.get("/articles", response_model=list[ArticleThumbnail])
def get_article():
    return ARTICLE_THUMBNAILS

@public_router.get("/articles/{slug}", response_model=ArticleDetail)
def get_article(slug: str):
    article = ARTICLE_DETAILS.get(slug)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article