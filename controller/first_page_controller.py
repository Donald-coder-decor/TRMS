from controller import employee_controller, course_controller, tuition_controller,role_controller,home_contoller,login_controller


def route(app):
    # Calls all controllers
    home_contoller.route(app)
    login_controller.route(app)
    employee_controller.route(app)
    course_controller.route(app)
    tuition_controller.route(app)
    # role_controller.route(app)
