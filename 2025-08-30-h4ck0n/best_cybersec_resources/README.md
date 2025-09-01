# Best Cybersec Resources
## Introduction
We get the following:
* [ZIP-file](deliverables.zip) 
* d4rkc0de.in:4424

## Exploitation
When extracting and having a look at the zip-file we can see it contains a website. We therefore assume d4rkc0de.in:4424 is a website and search for it in our browser. Here we find a standard /login screen with username and password fields. 

We access the registration page but when filling in random information we get back a "Something went wrong" message. We search for this in the zip and look in the registration section.  

```python
def register():
  ...
  if not username or not password or not email:
  flash("Something went wrong")
  return redirect(url_for("register"))

  if not allowed_domain(email):
    flash("Something went wrong")
    return redirect(url_for("register"))
  ...
```

First is just checks for fields not being empty, which we know they weren't. Second case is more interesting since it presumably checks for allowed domains for the email.

```python
ALLOWED_BASE_DOMAIN = "d4rkc0de.in"
d4rkc0de.in = re.compile(
    rf"@{re.escape(ALLOWED_BASE_DOMAIN)}\.?$", re.IGNORECASE)
ENC_WORD = re.compile(
    r"=\?(?:utf-8|iso-8859-1)\?(?:q|b)\?.+?\?=", re.IGNORECASE)
LOCAL_OK = re.compile(r"^[A-Za-z0-9._+\"@()-]+$")

def allowed_domain(addr: str) -> bool:
    if ENC_WORD.search(addr or ""):
        return False
    if not LOCAL_OK.search(addr or ""):
        pass
    return bool(DOMAIN_RE.search(addr or ""))
```
Here we see that `ENC_WORD` is properly implemented, but `LOCAL_OK` simply passes meaning it has no effect. Lastly and most interesting is that `DOMAIN_RE` specifies that the domain must be `@d4rkc0de.in` or `d4rkc0de.in.`.

We in the other files and find a file where the paths of the website are listed. Here we see the following regarding the admin path:

```python
@app.route("/admin")
def admin():
    require_login()
    u = get_current_user()
    if not (u and u.staff):
        abort(403)
    return render_template("admin.html")
```

Meaning if we want to see the admin page we ave to be staff. Looking in the register function from before we find a reference to a `is_staff` function:

```python
def register():
    ...
    staff = is_staff(email)
    ...

def is_staff(user_email_visible: str) -> bool:
    if not allowed_domain(user_email_visible):
        return False
    try:
        local = user_email_visible.split('@', 1)[0]
    except Exception:
        return False
    local_norm = normalize_email(local)
    if re.search(r"[A-Za-z]{6,}", local_norm):
        return True
    return False

def normalize_email(local: str) -> str:
    if local.startswith('"') and local.endswith('"'):
        local = local[1:-1]
    if '+' in local:
        local = local.split('+', 1)[0]
    local = local.replace('.', '')
    return local
```

Our goal is essentially to get the `is_staff` function to return True in order to create a staff account. First, we know `d4rkc0de.in.` is an allowed domain. Second, the local part of our email when normalized must be 6 letters long. The normalization removes quotes, drops everything after a +, and deletes all dots.

Knowing this we try to create a user with the email `tester@d4rkc0de.in`. We successfully create the account. After logging in and going to our profile page we can access the Admin-page where we see:

```
Maintenance task completed
Flag: d4rk{B3_bett3r_0r_m4yb3_l3t_th3_B1g_t3ch_h4ndl3_1T}c0de
```