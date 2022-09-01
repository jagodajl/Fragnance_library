from flask import Flask, request, render_template, redirect
from app import app, db
from app.models import Brand, Fragnance


@app.route("/")
def fragnance_list():
    fragnances = Fragnance.query.all()
    brands = Brand.query.all()
    return render_template("fragnances.html", fragnances=fragnances, brands=brands)


@app.route("/fragnance/", methods=["POST"])
def add_fragnance():
    name = request.form["name"]
    year = request.form["year"]
    price = request.form["price"]
    if not name:
        return "Error"

    fragnance = Fragnance(name=name, year=year, price=price)
    db.session.add(fragnance)
    db.session.commit()
    return redirect("/")


@app.route("/brand/", methods=["POST"])
def add_brand():
    name = request.form["name"]
    surname = request.form["surname"]
    birth = request.form["birth"]
    if not name:
        return "Error"

    brand = Brand(name=name, surname=surname, birth=birth)
    db.session.add(Brand)
    db.session.commit()
    return redirect("/")


@app.route("/assign/", methods=["POST"])
def assign_fragnance():  # assign fragnance to brand
    fragnance_id = request.form["fragnances_id"]
    brand_id = request.form["brand_id"]

    fragnance = Fragnance.query.get(fragnance_id)
    fragnance.brand_id = brand_id

    db.session.add(fragnance)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:fragnance_id>")
def delete_fragnance(fragnance_id):
    fragnance = Fragnance.query.get(fragnance_id)
    if not fragnance:
        return redirect("/")

    db.session.delete(fragnance)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:brand_id>")
def delete_brand(brand_id):
    brand = Brand.query.get(brand_id)
    if not brand:
        return redirect("/")

    db.session.delete(brand)
    db.session.commit()
    return redirect("/")


@app.route("/out_stock/<int:fragnance_id>")
def fragnance_in_stock(fragnance_id):
    fragnance = Fragnance.query.get(fragnance_id)
    print(f"def fragnance:  ", fragnance)
    if not fragnance:
        return redirect("/")
    if not fragnance.stock:
        fragnance.stock = True

    db.session.add(fragnance)
    db.session.commit()
    return redirect("/")


@app.route("/in_stock/<int:fragnance_id>")
def fragnance_out_of_stock(fragnance_id):
    fragnance = Fragnance.query.get(fragnance_id)
    print(f"def fragnance:  ", fragnance)
    if not fragnance:
        return redirect("/")
    if fragnance.stock:
        fragnance.stock = False

    db.session.add(fragnance)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
