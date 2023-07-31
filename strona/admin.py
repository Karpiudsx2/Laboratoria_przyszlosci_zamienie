# from flask import Blueprint, render_template, flash
# from flask_login import login_required, current_user
#
# admin = Blueprint("admin", __name__)
# admin_id = 1
#
# @admin.route("/admin", methods=['GET', 'POST'])
# @login_required
# def index():
#     if current_user.id == admin_id:
#         return render_template("admin.html", user=current_user)
#     else:
#         return flash("Nie masz uprawnień do przeglądania tej strony", category="error",)
