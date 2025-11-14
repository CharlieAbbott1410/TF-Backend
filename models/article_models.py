from pydantic import BaseModel

class ArticleThumbnail(BaseModel):
    title: str
    description: str
    slug: str
    link: str

class ArticleDetail(BaseModel):
    title: str
    content_html: str