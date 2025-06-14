from sqlalchemy.orm import Session
from infrastructure.database.models import UserModel, PostModel, CommentModel
from datetime import datetime, timedelta

def seed_database(session: Session):
    # Очищаем таблицы
    session.query(CommentModel).delete()
    session.query(PostModel).delete()
    session.query(UserModel).delete()
    session.commit()

    # Создаем пользователей
    users = [
        UserModel(
            username="Kirill_SOZINOV",
            email="KIRA@example.com",
            password_hash="hashed_password_1",
            is_active=True,
            created_at=datetime.utcnow() - timedelta(days=10)
        ),
        UserModel(
            username="anna_Petrova",
            email="anna@example.com",
            password_hash="hashed_password_2",
            is_active=True,
            created_at=datetime.utcnow() - timedelta(days=7)
        ),
        UserModel(
            username="alex_Sidorov",
            email="alex@example.com",
            password_hash="hashed_password_3",
            is_active=True,
            created_at=datetime.utcnow() - timedelta(days=5)
        ),
        UserModel(
            username="SofyaMaksimova",
            email="maksimovassofya@yandex.ru",
            password_hash="qwertyui",
            is_active=True,
            created_at=datetime.utcnow() - timedelta(days=0)
        )
    ]

    session.add_all(users)
    session.commit()

    # Создаем посты
    posts = [
        PostModel(
            title="Мой первый пост",
            content="Это содержание моего первого поста о выпечке.",
            author_id=users[0].id,
            created_at=datetime.utcnow() - timedelta(days=3)
        ),
        PostModel(
            title="Путешествие в горы",
            content="В выходные я решил приготовить котлеты в панировке...",
            author_id=users[1].id,
            created_at=datetime.utcnow() - timedelta(days=2)
        ),
        PostModel(
            title="Рецепт домашнего хлеба",
            content="Сегодня я испекла вкуснейший домашний хлеб по новому рецепту...",
            author_id=users[1].id,
            created_at=datetime.utcnow() - timedelta(days=1)
        )
    ]
    session.add_all(posts)
    session.commit()

    # Создаем комментарии
    comments = [
        CommentModel(
            content="Отличный пост, Кирилл!",
            author_id=users[1].id,
            post_id=posts[0].id,
            created_at=datetime.utcnow() - timedelta(hours=5)
        ),
        CommentModel(
            content="Согласен с Анной, очень информативно!",
            author_id=users[2].id,
            post_id=posts[0].id,
            created_at=datetime.utcnow() - timedelta(hours=3)
        ),
        CommentModel(
            content="Какие красивые фотографии в вашем посте!",
            author_id=users[0].id,
            post_id=posts[1].id,
            created_at=datetime.utcnow() - timedelta(hours=2)
        )
    ]
    session.add_all(comments)
    session.commit()

    print("База данных успешно заполнена тестовыми данными!")
