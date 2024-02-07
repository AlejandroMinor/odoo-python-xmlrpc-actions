import odoo_actions
def main():
    username = "admin"
    password = "password"
    db = "Ene_2024"
    url = "http://localhost:8069"

    try:
        odoo = odoo_actions.OdooActions(url, db, username, password)
        # record_id = odoo.search_record('res.users', [('name','=',"Alejandro Minor")])
        # print(record_id)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
