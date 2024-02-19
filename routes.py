# routes.py

from flask import render_template, request, jsonify
from forms import CheckInOutForm
from models import User, Tools
from extensions import db
from atems import app, create_app
from datetime import datetime


app = create_app()

@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

@app.route('/checkinout', methods=['GET', 'POST'])
def checkinout():
    form = CheckInOutForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        tool = Tools.query.filter_by(tool_id_number=form.tool_id_number.data).first()
        if user and tool:
            if form.badge_id.data == user.badge_id:
                if tool.checked_out_by == user.username:
                    tool.checked_out_by = None
                    tool.checkin_time = datetime.now()
                    db.session.commit()
                    return jsonify(status="success", message="Tool checked in")
                else:
                    tool.checked_out_by = user.username
                    tool.checkout_time = datetime.now()
                    db.session.commit()
                    return jsonify(status="success", message="Tool checked out")
            else:
                return jsonify(status="error", message="Badge ID does not match username")
        else:
            return jsonify(status="error", message="User or tool not found")    
    return render_template('checkinout.html', form=form, datetime=datetime)