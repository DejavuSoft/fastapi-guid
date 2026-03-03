from sqlalchemy.orm import Session
from datetime import datetime
from ..models.posts import Posts
from ..models.tags import Tags
from ..database import SessionLocal  # ← подставь правильный импорт своей сессии

def fill_test_data():
    db: Session = SessionLocal()

    try:
        # 1. Теги (5 штук)
        tags_list = [
            Tags(name="Python",     slug="python"),
            Tags(name="FastAPI",    slug="fastapi"),
            Tags(name="Vue.js",     slug="vuejs"),
            Tags(name="Tailwind",   slug="tailwind"),
            Tags(name="SQLAlchemy", slug="sqlalchemy"),
        ]

        # Добавляем теги и получаем их id
        db.add_all(tags_list)
        db.flush()  # сохраняем теги, чтобы появились id

        tag_map = {t.slug: t for t in tags_list}

        # 2. Посты (5 штук)
        posts_list = [
            Posts(
                autor="alice",
                name="Быстрый старт с FastAPI",
                tags_id=tag_map["fastapi"].id,
                description="Минимальный проект на FastAPI за 10 минут",
                content="# Быстрый старт\n\n```bash\npip install fastapi uvicorn\n```\n\n```python\nfrom fastapi import FastAPI\napp = FastAPI()\n```",
                image_url="https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
                created_at=datetime.utcnow()
            ),
            Posts(
                autor="bob",
                name="Composition API в Vue 3 — лучшие практики",
                tags_id=tag_map["vuejs"].id,
                description="ref, reactive, computed — когда что использовать",
                content="# Composition API\n\nconst count = ref(0)\nconst double = computed(() => count.value * 2)",
                image_url=None,
                created_at=datetime.utcnow()
            ),
            Posts(
                autor="carol",
                name="Tailwind за 15 минут — основные паттерны",
                tags_id=tag_map["tailwind"].id,
                description="flex, grid, hover, focus, dark: и многое другое",
                content="```css\n.btn {\n  @apply px-6 py-3 bg-indigo-600 text-white rounded-lg;\n}\n```",
                image_url="https://images.unsplash.com/photo-1555066931-bf19c65fd1df",
                created_at=datetime.utcnow()
            ),
            Posts(
                autor="alice",
                name="Как правильно работать с отношениями в SQLAlchemy",
                tags_id=tag_map["sqlalchemy"].id,
                description="relationship, back_populates, cascade и join",
                content="```python\nposts = relationship(\"Posts\", back_populates=\"tags\")\n```",
                image_url=None,
                created_at=datetime.utcnow()
            ),
            Posts(
                autor="dave",
                name="Python в 2026 году — что нового",
                tags_id=tag_map["python"].id,
                description="match-case, улучшенные type hints, faster CPython",
                content="# Что нового в Python 3.12+\n\n- match-case\n- улучшенный traceback",
                image_url="https://images.unsplash.com/photo-1526379095098-d400fd0bf935",
                created_at=datetime.utcnow()
            ),
        ]

        db.add_all(posts_list)
        db.commit()

        print("Успешно добавлено:")
        print(f"  • Тегов:     {len(tags_list)}")
        print(f"  • Постов:    {len(posts_list)}")

    except Exception as e:
        db.rollback()
        print("Ошибка при заполнении:", str(e))
        raise
    finally:
        db.close()


if __name__ == "__main__":
    fill_test_data()