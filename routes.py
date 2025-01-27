from flask import render_template, request, jsonify
from forms import CheckInOutForm
from models import User, Tools
from extensions import db
from atems import app
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logger = logging.getLogger(__name__)

@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

@app.route('/checkinout', methods=['GET', 'POST'])
def checkinout():
    form = CheckInOutForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            tool = Tools.query.filter_by(tool_id_number=form.tool_id_number.data).first()
            if user and tool:
                if form.badge_id.data == user.badge_id:
                    if tool.checked_out_by == user.username:
                        tool.checked_out_by = None
                        tool.checkin_time = datetime.now()
                        db.session.commit()
                        logger.info(f"Tool {tool.tool_id_number} checked in by {user.username}")
                        return jsonify(status="success", message="Tool checked in")
                    else:
                        tool.checked_out_by = user.username
                        tool.checkout_time = datetime.now()
                        db.session.commit()
                        logger.info(f"Tool {tool.tool_id_number} checked out by {user.username}")
                        return jsonify(status="success", message="Tool checked out")
                else:
                    logger.warning(f"Badge ID mismatch for user {user.username}")
                    return jsonify(status="error", message="Badge ID does not match username")
            else:
                logger.warning(f"User or tool not found: username={form.username.data}, tool_id={form.tool_id_number.data}")
                return jsonify(status="error", message="User or tool not found")
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"Database error: {str(e)}")
            return jsonify(status="error", message=f"Database error: {str(e)}")
    elif request.method == 'POST':
        logger.warning(f"Form validation failed: {form.errors}")
    return render_template('checkinout.html', form=form, datetime=datetime)
