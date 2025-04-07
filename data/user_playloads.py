def create_user_payload(name, job):
    return {
        "name": name,
        "job": job
    }

def update_user_playload(name,job):
    return {
        "name": name,
        "job": job
    }

def suc_register(email,password):
    return {
        "email": email,
        "password": password
    }

def unsuc_register(email):
    return  {
        "email":email
    }

