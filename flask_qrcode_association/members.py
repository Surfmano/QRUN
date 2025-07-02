from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import Member
from app import db
import uuid
import qrcode
from flask_login import login_required

members = Blueprint('members', __name__)

@members.route('/register_member', methods=['GET', 'POST'])
@login_required
def register_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        member_uuid = str(uuid.uuid4())
        member = Member(uuid=member_uuid, name=name, email=email)
        db.session.add(member)
        db.session.commit()

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(member_uuid)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'static/qrcodes/{member_uuid}.png')

        flash('Member registered successfully!', 'success')
        return redirect(url_for('members.member_profile', uuid=member_uuid))

    return render_template('register_member.html', title='Register Member')

@members.route('/member_profile/<uuid>', methods=['GET'])
@login_required
def member_profile(uuid):
    member = Member.query.filter_by(uuid=uuid).first_or_404()
    return render_template('member_profile.html', title=member.name, member=member)
