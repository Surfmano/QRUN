import pytest
from datetime import datetime
from flask_qrcode_association import create_app, db
from flask_qrcode_association.models import User, Member

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    with app.app_context():
        yield app.test_client()

def test_user_creation(app, client):
    """Test la création d'un utilisateur"""
    with app.app_context():
        user = User(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        db.session.add(user)
        db.session.commit()
        
        assert user.id is not None
        assert user.date_created <= datetime.utcnow()

def test_member_creation(app, client):
    """Test la création d'un membre"""
    with app.app_context():
        member = Member(
            uuid="550e8400-e29b-41d4-a716-446655440000",
            name="Jean Dupont",
            email="jean@example.com"
        )
        db.session.add(member)
        db.session.commit()
        
        assert member.id is not None
        assert member.date_joined <= datetime.utcnow()
