def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def Welcome():
        return "Welcome to Tuition Reimbursement Management System @Revature Training!"
