@app.route("/products", methods=["GET"])

def list_products():

    """Returns a list of Products"""



    name = request.args.get("name")

    category = request.args.get("category")

    available = request.args.get("available")



    if name:

        products = Product.find_by_name(name)



    elif category:

        category_value = getattr(

            Category,

            category.upper()

        )

        products = Product.find_by_category(

            category_value

        )



    elif available:

        available_value = available.lower() in [

            "true", "yes", "1"

        ]

        products = Product.find_by_availability(

            available_value

        )



    else:

        products = Product.all()



    results = [

        product.serialize()

        for product in products

    ]



    return results, status.HTTP_200_OK