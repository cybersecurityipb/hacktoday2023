#!/usr/bin/env python3

import jinja2
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    abort
)
from secret import get_secret
app = Flask(__name__, template_folder="./templates/", static_folder="./static/")
app.secret_key = get_secret(0x100)


msg = """
Hello, This is Maru.

We have a new individual who has expressed a strong interest in joining our community. Could you please schedule an interview to evaluate their potential fit with us?
Here are the details of the applicant:

- Name: {{ name_member }}
- Role: {{ role_member }}

I have attached the application details in the following file:
- 'Details: {{ maru }}{{ maru_notes }}{{ name_member }}{{ role_member }}.xlsx'
Your prompt attention to this matter is greatly appreciated.

Best regards,
Maru
"""

def newmember(address, content):
    try:
        content += "\n\n{{ signature }}"
        _signature = """---\n<b>Tempest Village:</b>\nmaru@slime.com"""
        content = jinja2.Template(content).render(signature=_signature)
    except Exception as e:
        pass
    return None

def sanitize(value):
    blacklist = ['{{','}}','{%','%}','import','eval','builtins','class','[',']', 'cycler', "\"", "`", "[", "]", "+", "init", "subprocess", "config", "update", "mro", "subclasses", "class", "base", "builtins"]
    for word in blacklist:
        if word in value:
            value = value.replace(word,'')
    if any([bool(w in value) for w in blacklist]):
        value = sanitize(value)
    return value

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html'), 400

@app.errorhandler(404)
def bad_request_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500


# Custom decorator to check if the user is an admin
def admin_required(func):
    def wrapper(*args, **kwargs):
        print(session)
        if session.get('admin'):
            return func(*args, **kwargs)
        else:
            abort(403)

    return wrapper

@app.route("/admin", methods=["GET", "POST"])
@admin_required
def admin():
    admin_name = session.get('admin')
    if admin_name is not None:
        global msg
        notes = session.get('notes')
        if request.method == "POST":
            if "notes" in request.form.keys() and len(request.form["notes"]) != 0 and "name" in request.form.keys() and len(request.form["name"]) != 0  and "role" in request.form.keys() and len(request.form["role"]) != 0 :
                if len(admin_name) > 5:
                    return render_template("admin.html", error="Wait... why admin has such long name")
                if len(request.form["notes"]) >= 50: # notes
                    return render_template("admin.html", error="notes is too long.")
                if len(request.form["name"]) >= 50: # name
                    return render_template("admin.html", error="name is too long.")
                if len(request.form["role"]) > 10: # role
                    return render_template("admin.html", error="role is too long.")
                try:
                    register_mail = jinja2.Template(msg).render(
                        maru=sanitize(admin_name),
                        maru_notes=sanitize(request.form["notes"]),
                        name_member=sanitize(request.form["name"]),
                        role_member=sanitize(request.form["role"])
                    )
                except Exception as e:
                    pass
                newmember("maru@slime.com", register_mail)
                print(register_mail) # help your debugger
                return render_template("admin.html", success="Thank you! Your application will be reviewed within a week.")
            else:
                return render_template("admin.html", error="Missing fields in the application form!")
        elif request.method == 'GET':
            return render_template("admin.html")        
    else:
        abort(400)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["user"] = username
        return redirect(url_for("index"))
    return render_template("login.html")    

@app.route("/", methods=["GET"])
def index():
        username = session.get("user")
        return render_template("main.html", username=username)

@app.route("/logout")
def logout():
    # Clear the session to log the user out
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route('/article', methods=['GET'])
def article():
    return render_template('article.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
