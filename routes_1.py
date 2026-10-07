@app.route("/products/<int:product_id>", methods=["PUT"])

def update_products(product_id):

    """Update a Product"""



    check_content_type("application/json")



    product = Product.find(product_id)



    if not product:

        abort(

            status.HTTP_404_NOT_FOUND,

            f"Product with id '{product_id}' was not found."

        )



    product.deserialize(request.get_json())

    product.id = product_id

    product.update()



    return product.serialize(), status.HTTP_200_OK