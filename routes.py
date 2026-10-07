@app.route("/products/<int:product_id>", methods=["GET"])

def get_products(product_id):

    """Retrieve a single Product"""



    product = Product.find(product_id)



    if not product:

        abort(

            status.HTTP_404_NOT_FOUND,

            f"Product with id '{product_id}' was not found."

        )



    return product.serialize(), status.HTTP_200_OK