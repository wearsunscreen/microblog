import datetime
from flask import Blueprint, render_template, request
from flask import current_app as app

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries_with_date = [
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"),
        )
        for entry in app.db.entries.find({})
    ]
    return render_template("home.html", entries=entries_with_date)
