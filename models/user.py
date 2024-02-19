#   user.py


from extensions import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin
from flask_admin.model.ajax import AjaxModelLoader




class User(db.Model, UserMixin):
    """Model for users"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    badge_id = db.Column(db.String(10), index=True, unique=True, nullable=False)
    phone = db.Column(db.String(10), index=True, unique=True, nullable=False)
    department = db.Column(db.String(64), index=True, unique=False, nullable=False)
    supervisor_username = db.Column(db.String(64), index=True, unique=False, nullable=False)
    supervisor_email = db.Column(db.String(80), index=True, unique=False, nullable=False)
    supervisor_phone = db.Column(db.String(10), index=True, unique=False, nullable=False)
    manager_username = db.Column(db.String(64), index=True, unique=False,)
    manager_email = db.Column(db.String(80), index=True, unique=False,)
    manager_phone = db.Column(db.String(10), index=True, unique=False,)


    def __repr__(self):
        return '<User {}, Username: {}, Email: {}, Badge ID: {}, Phone: {}, Department: {}, Supervisor Username: {}, Supervisor Email: {}, Supervisor Phone: {}, Manager Username: {}, Manager Email: {}, Manager Phone: {}>'.format(self.first_name, self.username, self.email, self.badge_id, self.phone, self.department, self.supervisor_username, self.supervisor_email, self.supervisor_phone, self.manager_username, self.manager_email, self.manager_phone)

class UserView(ModelView):
    """View for users"""
    column_searchable_list = ['first_name','last_name','username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_filters = ['first_name','last_name', 'username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_editable_list = ['first_name','last_name', 'username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_default_sort = ('first_name','last_name', 'username', True)
    column_sortable_list = ['first_name','last_name', 'username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_labels = dict(first_name='First Name', last_name='Last Name', username='Username', email='Email', badge_id='Badge ID', phone='Phone', department='Department', supervisor_username='Supervisor Username', supervisor_email='Supervisor Email', supervisor_phone='Supervisor Phone', manager_username='Manager Username', manager_email='Manager Email', manager_phone='Manager Phone')
    column_descriptions = dict(first_name='First Name', last_name='Last Name', username='Username', email='Email', badge_id='Badge ID', phone='Phone', department='Department', supervisor_username='Supervisor Username', supervisor_email='Supervisor Email', supervisor_phone='Supervisor Phone', manager_username='Manager Username', manager_email='Manager Email', manager_phone='Manager Phone')
    column_details_list = ['first_name','last_name', 'username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_export_list = ['first_name','last_name', 'username', 'email', 'badge_id', 'phone', 'department', 'supervisor_username', 'supervisor_email', 'supervisor_phone', 'manager_username', 'manager_email', 'manager_phone']
    column_choices = dict(department=[('ATEMS', 'ATEMS'), ('Engineering', 'Engineering'), ('Manufacturing', 'Manufacturing'), ('Quality', 'Quality'), ('Supply Chain', 'Supply Chain'), ('Test', 'Test')])

class FirstNameLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.first_name.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.first_name}
    
class LastNameLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.last_name.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.last_name}
    
    
    
class UsernameLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.username.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.username}
    
    
class EmailLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.email.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.email}
    
    
class BadgeIdLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.badge_id.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.badge_id}
    
    
class PhoneLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.phone.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.phone}
    

class DepartmentLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.department.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.department}
    
    
class SupervisorUsernameLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.supervisor_username.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.supervisor_username}
    
    
class SupervisorEmailLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.supervisor_email.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.supervisor_email}
    
    
class SupervisorPhoneLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.supervisor_phone.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.supervisor_phone}
    
    
class ManagerUsernameLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.manager_username.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.manager_username}
    
    
class ManagerEmailLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.manager_email.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.manager_email}
    
    
class ManagerPhoneLoader(AjaxModelLoader):
    def get_one(self, id):
        return db.session.query(User).get(id)

    def get_list(self, term, offset=0, limit=10):
        return db.session.query(User).filter(User.manager_phone.like('%' + term + '%')).all()

    def format(self, model):
        return {"id": model.id, "text": model.manager_phone}
    
    
form_ajax_refs = {
    'first_name': FirstNameLoader('first_name', db.session),
    'last_name': LastNameLoader('last_name', db.session),
    'username': UsernameLoader('username', db.session),
    'email': EmailLoader('email', db.session),
    'badge_id': BadgeIdLoader('badge_id', db.session),
    'phone': PhoneLoader('phone', db.session),
    'department': DepartmentLoader('department', db.session),
    'supervisor_username': SupervisorUsernameLoader('supervisor_username', db.session),
    'supervisor_email': SupervisorEmailLoader('supervisor_email', db.session),
    'supervisor_phone': SupervisorPhoneLoader('supervisor_phone', db.session),
    'manager_username': ManagerUsernameLoader('manager_username', db.session),
    'manager_email': ManagerEmailLoader('manager_email', db.session),
    'manager_phone': ManagerPhoneLoader('manager_phone', db.session)
}
 
 
 
admin.add_view(ModelView(User, db.session, name='Add User'))
