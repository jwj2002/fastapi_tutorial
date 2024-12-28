from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db: Session, author_id: int=1):
    blog = Blog(
        title = blog.title,
        slug = blog.slug,
        content = blog.content,
        author_id = author_id,
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def delete_blog(id: int, author_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        return {'error', f'Could not find blog with id {id}'}
    blog.delete()
    db.commit()
    return {'msg': f'Deleted blog with id {id}'}