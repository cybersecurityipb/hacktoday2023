import jinja2
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    render_template_string
)
# from pin import get_pin_for_secret()
app = Flask(__name__)
app.secret_key = 'Secret' # pin_urandom()



mail = """
Hello team,

A new hacker wants to join our private Bug bounty program! Mary, can you schedule an interview?

 - Name: {{ maru }}
 - Surname: {{ hacker_surname }}
 - Email: {{ hacker_email }}
 - Birth date: {{ hacker_bday }}

I'm sending you the details of the application in the attached CSV file:

 - '{{ maru }}{{ hacker_surname }}{{ hacker_email }}{{ hacker_bday }}.csv'

Best regards,
"""

def sendmail(address, content):
    try:
        content += "\n\n{{ signature }}"
        _signature = """---\n<b>Offsec Team</b>\noffsecteam@hackorp.com"""
        content = jinja2.Template(content).render(signature=_signature)
    except Exception as e:
        pass
    return None

def sanitize(value):
    blacklist = ['{{','}}','{%','%}','import','eval','builtins','class','[',']']
    for word in blacklist:
        if word in value:
            value = value.replace(word,'')
    if any([bool(w in value) for w in blacklist]):
        value = sanitize(value)
    return value

# Custom decorator to check if the user is an admin
def admin_required(func):
    def wrapper(*args, **kwargs):
        print(session)
        if session.get('admin'):
            return func(*args, **kwargs)
        else:
            return "Forbidden - Admin access required", 403

    return wrapper

@app.route("/admin", methods=["GET", "POST"])
@admin_required
def admin():
    admin_name = session.get('admin')
    if admin_name is not None:
        global mail
        if request.method == "POST":
            if "name" in request.form.keys() and len(request.form["name"]) != 0 and "surname" in request.form.keys() and len(request.form["surname"]) != 0 and "email" in request.form.keys() and len(request.form["email"]) != 0 and "bday" in request.form.keys() and len(request.form["bday"]) != 0 :
                if len(admin_name) > 20:
                    return render_template("admin.html", error="Field 'name' is too long.")
                if len(request.form["surname"]) >= 50:
                    return render_template("admin.html", error="Field 'surname' is too long.")
                if len(request.form["email"]) >= 100:
                    return render_template("admin.html", error="Field 'email' is too long.")
                if len(request.form["bday"]) > 10:
                    return render_template("admin.html", error="Field 'bday' is too long.")
                try:
                    register_mail = jinja2.Template(mail).render(
                        maru=sanitize(admin_name),
                        hacker_surname=sanitize(request.form["surname"]),
                        hacker_email=sanitize(request.form["email"]),
                        hacker_bday=sanitize(request.form["bday"])
                    )
                except Exception as e:
                    pass
                sendmail("offsecteam@hackorp.com", register_mail)
                print(register_mail)
                return render_template("admin.html", success="Thank you! Your application will be reviewed within a week.")
            else:
                return render_template("admin.html", error="Missing fields in the application form!")
        elif request.method == 'GET':
            return render_template("admin.html")        
    else:
        return 'Session value not found.', 400

    

@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")

# Done
@app.route('/article', methods=['GET'])
def article():
    error = 0

    if 'name' in request.args:
        page = request.args.get('name')
    else:
        page = 'file/blank.txt'

    if 'flag' in page:
        page = 'file/notallowed.txt'

    try:
        with open(f'templates/{page}', 'r') as f:
            template = f.read()
    except Exception as e:
        template = str(e)

    return render_template('article.html', template=template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
