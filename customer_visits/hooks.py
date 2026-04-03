app_name = "customer_visits"
app_title = "Customer Visits"
app_publisher = "Ahmed"
app_description = "App for scheduling customer visits"
app_email = "ahmed@test.com"
app_license = "mit"

doc_events = {
    "Customer": {
        "on_change": "customer_visits.customer_visit_request.cancel_visits_on_territory_change"
    }
}

fixtures = [
	"Workflow State",
	{"doctype": "Workflow", "filters": [["document_type", "=", "Customer Visit Request"]]},
    "Custom Field",
    "Client Script",
]

override_doctype_class = {
    "Customer": "customer_visits.custom_overrides.customer.CustomCustomer"
}

after_migrate = ["customer_visits.install.ensure_workflow_actions"]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "customer_visits",
# 		"logo": "/assets/customer_visits/logo.png",
# 		"title": "Customer Visits",
# 		"route": "/customer_visits",
# 		"has_permission": "customer_visits.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customer_visits/css/customer_visits.css"
# app_include_js = "/assets/customer_visits/js/customer_visits.js"

# include js, css files in header of web template
# web_include_css = "/assets/customer_visits/css/customer_visits.css"
# web_include_js = "/assets/customer_visits/js/customer_visits.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "customer_visits/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "customer_visits/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "customer_visits.utils.jinja_methods",
# 	"filters": "customer_visits.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "customer_visits.install.before_install"
# after_install = "customer_visits.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "customer_visits.uninstall.before_uninstall"
# after_uninstall = "customer_visits.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "customer_visits.utils.before_app_install"
# after_app_install = "customer_visits.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "customer_visits.utils.before_app_uninstall"
# after_app_uninstall = "customer_visits.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customer_visits.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customer_visits.tasks.all"
# 	],
# 	"daily": [
# 		"customer_visits.tasks.daily"
# 	],
# 	"hourly": [
# 		"customer_visits.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customer_visits.tasks.weekly"
# 	],
# 	"monthly": [
# 		"customer_visits.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "customer_visits.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customer_visits.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "customer_visits.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["customer_visits.utils.before_request"]
# after_request = ["customer_visits.utils.after_request"]

# Job Events
# ----------
# before_job = ["customer_visits.utils.before_job"]
# after_job = ["customer_visits.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"customer_visits.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

